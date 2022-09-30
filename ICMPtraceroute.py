# Attribution: this assignment is based on ICMP Traceroute Lab from Computer Networking: a Top-Down Approach by Jim Kurose and Keith Ross. 
# It was modified for use in CSC249: Networks at Smith College by R. Jordan Crouser in Fall 2022

from socket import *
from ICMPpinger import checksum
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
# To solve "timeout must be non-negative" error
# We can increase TIMEOUT, to allow more time to trace route
# TIMEOUT = 2.0
TIMEOUT = 3.0
TRIES = 2

# The packet that we shall send to each router along the path is the ICMP echo
# request packet, which is exactly what we had used in the ICMP ping exercise.
# We shall use the same packet that we built in the Ping exercise
def build_packet():
    # In the sendOnePing() method of the ICMP Ping exercise, firstly the header of our
    # packet to be sent was made, secondly the checksum was appended to the header and
    # then finally the complete packet was sent to the destination.

    #---------------#
    # Fill in start #
    #---------------#

    # Task: Make the header in a similar way to the ping exercise.

    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    myChecksum = 0
    myID = os.getpid() & 0xFFFF

    # Question: What is "bbHHh"
    # Answer: It's format characters
    # https://docs.python.org/3/library/struct.html#format-characters

    # Question: We don't need ID in this header?
    # Answer: We do need because otherwise pack method is not happy
    
    # Make a dummy header with a 0 checksum
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, myID, 1) 
    data = struct.pack("d", time.time())

    # Task: Append checksum to the header.

    # Calculate the checksum on the data and the dummy header. 
    # myChecksum = checksum(str(header + data))
    myChecksum = checksum(''.join(map(chr, header+data)))

    # Get the right checksum, and put in the header 
    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network byte order 
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, myID, 1) 
        
    #-------------#
    # Fill in end #
    #-------------#

    # Don’t send the packet yet , just return the final packet in this function.
    packet = header + data
    return packet

def get_route(hostname):
    timeLeft = TIMEOUT
    for ttl in range(1,MAX_HOPS):
        for tries in range(TRIES):
            destAddr = gethostbyname(hostname)

            #---------------#
            # Fill in start #
            #---------------#

            # Task: Make a raw socket named mySocket

            # Question: What's icmp here?
            # Answer: icmp is a protocol which provides a common ground for computers to communicate
            # A network protocol is an established set of rules 
            # that determine how data is transmitted between different devices in the same network. 
            # Essentially, it allows connected devices to communicate with each other, 
            # regardless of any differences in their internal processes, structure or design.
            icmp = getprotobyname("icmp") 

            # SOCK_RAW is a powerful socket type. For more details:	
            # http://sock-raw.org/papers/sock_raw

            mySocket = socket(AF_INET, SOCK_RAW, icmp)

            #-------------#
            # Fill in end #
            #-------------#

            mySocket.setsockopt(IPPROTO_IP, IP_TTL, struct.pack('I', ttl))
            mySocket.settimeout(TIMEOUT)

            try:
                d = build_packet()
                mySocket.sendto(d, (hostname, 0))
                t= time.time()
                startedSelect = time.time()
                whatReady = select.select([mySocket], [], [], timeLeft)
                howLongInSelect = (time.time() - startedSelect)

                if whatReady[0] == []: # Timeout
                    print(" * * * Request timed out.")

                recvPacket, addr = mySocket.recvfrom(1024)
                timeReceived = time.time()
                timeLeft = timeLeft - howLongInSelect

                if timeLeft <= 0:
                    print(" * * * Request timed out.")

            except timeout:
                continue

            else:
                #---------------#
                # Fill in start #
                #---------------#

                #Task: Fetch the icmp type from the IP packet
                header = recvPacket[20:28]
                types, code, checksum, packetID, sequence= struct.unpack("bbHHh", header)

                #-------------#
                # Fill in end #
                #-------------#
                
                # Question: Why are there different types?
                # Answer: https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages
                if types == 11:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 +bytes])[0]
                    print(" %d rtt=%.0f ms %s" %(ttl, (timeReceived -t)*1000, addr[0]))

                elif types == 3:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    print(" %d rtt=%.0f ms %s" %(ttl, (timeReceived-t)*1000, addr[0]))

                elif types == 0:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    print(" %d rtt=%.0f ms %s" %(ttl, (timeReceived - timeSent)*1000, addr[0]))
                    return

                else:
                    print("error")

                break

            finally:
                mySocket.close()

if __name__ == '__main__':
    print("www.google.com in North America")
    get_route("www.google.com")
    print("")
    print("www.baidu.com in Asia")
    get_route("www.yahoo.co.in")
    print("")
    print("www.louvre.fr in Europe")
    get_route("www.louvre.fr")
    print("")
    print("www.iziko.org.za in Africa")
    get_route("www.ru.ac.za")
