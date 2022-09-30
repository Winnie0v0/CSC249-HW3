Use this file to record your reflection on this assignment and answer the prompts.

What worked, what didn't, what advice would you give someone taking this course in the future?
* At the time of writing this reflection, I couldn't successfully fetch TTL form the packet. However, all elements from icmp header were successfully fetched. I also managed to successfully create my socket and pack a packet. 
* For someone taking this course in the future, I would advice reading the slack messages. I missed the tiny error we need to correct, and the format for icmp header which is a little annoying.

Test your `ping` and `traceroute` programs on 4 target hosts, each on a different continent and include the output below.
* ping
www.google.com in North America
Pinging 142.250.80.100 using Python:
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=13.951 ms
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=17.402 ms
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=17.756 ms
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=17.664 ms
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=14.875 ms
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=19.182 ms
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=19.454 ms
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=18.329 ms
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=19.324 ms
 8 bytes from 142.250.80.100: icmp_seq=1 ttl=1 time=18.818 ms

www.baidu.com in Asia
Pinging 74.6.136.150 using Python:
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=24.010 ms
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=25.265 ms
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=27.064 ms
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=26.234 ms
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=26.488 ms
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=23.571 ms
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=43.370 ms
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=23.347 ms
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=27.302 ms
 8 bytes from 74.6.136.150: icmp_seq=1 ttl=1 time=26.497 ms

www.louvre.fr in Europe
Pinging 89.185.38.196 using Python:
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=96.257 ms
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=96.447 ms
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=99.761 ms
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=100.879 ms
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=99.643 ms
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=97.584 ms
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=98.461 ms
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=99.868 ms
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=99.577 ms
 8 bytes from 89.185.38.196: icmp_seq=1 ttl=1 time=100.866 ms

www.iziko.org.za in Africa
Pinging 146.231.128.43 using Python:
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=278.083 ms
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=327.728 ms
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=332.646 ms
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=325.216 ms
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=324.647 ms
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=230.307 ms
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=318.950 ms
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=224.668 ms
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=325.266 ms
 8 bytes from 146.231.128.43: icmp_seq=1 ttl=1 time=328.647 ms

* traceroute
www.google.com in North America
 1 rtt=8 ms 131.229.195.254
 2 rtt=12 ms 131.229.11.105
 3 rtt=18 ms 131.229.10.104
 4 rtt=6 ms 134.241.249.33
 5 rtt=6 ms 69.16.1.33
 6 rtt=7 ms 18.2.136.89
 7 rtt=14 ms 192.5.89.42
 8 rtt=14 ms 18.2.145.18
 9 rtt=12 ms 108.170.248.97
 10 rtt=11 ms 142.251.65.115
 11 rtt=17 ms 142.250.80.100

www.baidu.com in Asia
 1 rtt=19 ms 131.229.195.254
 2 rtt=13 ms 131.229.11.105
 3 rtt=23 ms 131.229.10.104
 4 rtt=16 ms 134.241.249.33
 5 rtt=8 ms 69.16.1.33
 6 rtt=11 ms 18.2.136.89
 7 rtt=12 ms 192.5.89.57
 8 rtt=19 ms 206.53.143.34
 9 rtt=34 ms 209.191.64.155
 10 rtt=26 ms 74.6.227.63
 11 rtt=27 ms 74.6.122.41
 12 rtt=23 ms 74.6.123.239
 13 rtt=21 ms 74.6.98.136
 14 rtt=23 ms 74.6.136.150

www.louvre.fr in Europe
 1 rtt=14 ms 131.229.195.254
 2 rtt=14 ms 131.229.11.105
 3 rtt=27 ms 131.229.10.104
 4 rtt=6 ms 134.241.249.33
 5 rtt=6 ms 69.16.1.33
 6 rtt=9 ms 63.159.137.237
 7 rtt=15 ms 67.14.45.222
 8 rtt=15 ms 4.68.110.153
 9 rtt=97 ms 4.69.143.178
 10 rtt=97 ms 213.242.120.70
 11 rtt=99 ms 212.43.193.205
 12 rtt=98 ms 212.43.193.145
 13 rtt=96 ms 89.185.58.93
 14 rtt=100 ms 89.185.38.196

www.iziko.org.za in Africa
 1 rtt=10 ms 131.229.195.254
 2 rtt=14 ms 131.229.11.105
 3 rtt=27 ms 131.229.10.104
 4 rtt=5 ms 134.241.249.33
 5 rtt=4 ms 69.16.1.33
 6 rtt=8 ms 18.2.8.89
 7 rtt=10 ms 192.5.89.57
 8 rtt=18 ms 192.5.89.222
 9 rtt=41 ms 163.253.1.42
 10 rtt=40 ms 163.253.1.116
 11 rtt=40 ms 163.253.1.107
 12 rtt=38 ms 163.253.1.135
 13 rtt=42 ms 163.253.1.100
 14 rtt=48 ms 163.253.2.33
 15 rtt=206 ms 155.232.71.2
 16 rtt=241 ms 155.232.64.144
 17 rtt=206 ms 155.232.64.86
 18 rtt=300 ms 155.232.6.42
 19 rtt=294 ms 155.232.5.5
 20 rtt=227 ms 192.42.99.252
 21 rtt=247 ms 192.42.99.231
 22 rtt=243 ms 146.231.135.21
 23 rtt=304 ms 146.231.128.43
