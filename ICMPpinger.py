# Attribution: this assignment is based on ICMP Pinger Lab from Computer Networking: a Top-Down Approach by Jim Kurose and Keith Ross. 
# It was modified for use in CSC249: Networks at Smith College by R. Jordan Crouser in Fall 2022

from socket import * 
import os
import sys 
import struct 
import time 
import select 
import binascii


ICMP_ECHO_REQUEST = 8

# -------------------------------------
# This method takes care of calculating
#   a checksum to make sure nothing was
#   corrupted in transit.
#  
# You do not need to modify this method
# -------------------------------------
def checksum(string): 
    csum = 0
    countTo = (len(string) // 2) * 2 
    count = 0

    while count < countTo: 
        thisVal = ord(string[count+1]) * 256 + ord(string[count]) 
        csum = csum + thisVal
        csum = csum & 0xffffffff 
        count = count + 2

    if countTo < len(string):
        csum = csum + ord(string[len(string) - 1]) 
        csum = csum & 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff) 
    csum = csum + (csum >> 16)

    answer = ~csum

    answer = answer & 0xffff
 
    answer = answer >> 8 | (answer << 8 & 0xff00) 
    return answer


def receiveOnePing(mySocket, ID, timeout, destAddr): 
    
    timeLeft = timeout
    
    while True:
        startedSelect = time.time()

        whatReady = select.select([mySocket], [], [], timeLeft) 
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []: # Timeout 
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)

        #---------------#
        # Fill in start #
        #---------------#

        # Task: Fetch the ICMP header from the IP packet

        # Question: Where did we learned about the combination of headers?
        # Answer: It's in slack https://smith.enterprise.slack.com/files/U3ZF37THD/F043KU2LE7P/icmp_header_handout.pdf
        header = recPacket[20:28]

        # Here we can fetch the ICMP header from the IP packet
        # But we don't need to return them all according to the assignment instruction.
        type, code, checksum, id, sequence = struct.unpack(
            "bbHHh", header)

        # Question: is timeLeft equivalent to time to live (TTL)?
        # Answer: No, TTT is how many hops left not a time.
        # It is not from icmp header but can be unpacked from other packet
        # In the IPv4 header, TTL is the 9th octet of 20
        # https://en.wikipedia.org/wiki/Time_to_live
        # https://en.wikipedia.org/wiki/IPv4#Header
        # https://docs.python.org/3/library/struct.html#format-characters
        # Get TTL, which returns a tuple
        ttl = struct.unpack("B", recPacket[9:10])[0]
        
        # Delay is just round-trip time (RTT)?
        bytes = struct.calcsize("d")
        timeSent = struct.unpack("d", recPacket[28:28 + bytes])[0]
        rrt = timeReceived - timeSent

        # example from ping google in terminal
        # 64 bytes from 142.251.40.196: icmp_seq=0 ttl=115 time=257.346 ms
        # For python old string formatting
        # https://docs.python.org/3/library/stdtypes.html#old-string-formatting
        return " %d bytes from %s: icmp_seq=%d ttl=%.0f time=%.3f ms" %(bytes, destAddr, sequence, ttl, rrt*1000)

        #-------------#
        # Fill in end #
        #-------------#

        timeLeft = timeLeft - howLongInSelect 
        
        if timeLeft <= 0:
            return "Request timed out."



def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    myChecksum = 0

    # Make a dummy header with a 0 checksum
 
    # struct -- Interpret strings as packed binary data
    # Even though the type is ICMP_ECHO_REQUEST in the request, the reply type is always 0.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1) 
    # multiple icmp packet
    data = struct.pack("d", time.time()) #format string

    # Calculate the checksum on the data and the dummy header. 
    # myChecksum = checksum(''.join(map(chr, header+data)))
    myChecksum = checksum(''.join(map(chr, header+data)))

    # Get the right checksum, and put in the header 

    # Question: What is darwin?
    # Answer: It's to check what's your operating system
    # Interestingly Mac OS x is darwin
    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network byte order 
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    # Can increase the sequence when necessary
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1) 
    packet = header + data

    # Question: What exactly is a socket?
    # Answer: A network socket is a software structure within a network node of a computer network 
    # that serves as an endpoint for sending and receiving data across the network.
    # https://en.wikipedia.org/wiki/Network_socket
    mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str 
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object.



def doOnePing(destAddr, timeout): 
    # Question: What does this do?
    # Answer: https://pythontic.com/modules/socket/getprotobyname
    icmp = getprotobyname("icmp")

    # SOCK_RAW is a powerful socket type. For more details:	
    # http://sock-raw.org/papers/sock_raw

    mySocket = socket(AF_INET, SOCK_RAW, icmp)

    myID = os.getpid() & 0xFFFF # Return the current process i 
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)
 
    mySocket.close() 
    return delay


def ping(host, timeout=1):

    # timeout=1 means: If one second goes by without a reply from the server,

    # the client assumes that either the client's ping or the server's pong is lost 
    dest = gethostbyname(host)
    print("Pinging " + dest + " using Python:") 

    # Send ping requests to a server separated by approximately one second 
    while True :
        delay = doOnePing(dest, timeout) 
        print(delay)
        time.sleep(1) # one second 
    return delay

# Runs program
if __name__ == '__main__':
    # print("www.google.com in North America")
    # ping("www.google.com")
    # print("www.baidu.com in Asia")
    # ping("www.yahoo.co.in")
    # print("www.louvre.fr in Europe")
    # ping("www.louvre.fr")
    print("www.iziko.org.za in Africa")
    ping("www.ru.ac.za")