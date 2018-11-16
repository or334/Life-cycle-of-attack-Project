from scapy.all import * 
from scapy.layers.inet import IP, ICMP

#ttl = 128 -> Windows
#ttl = 64 -> Linux

package = IP(dst="10.195.25.152")/ICMP()
response = sr1 (package, timeout=2)
a = IP(dst="10.195.25.152")/TCP(dport=80)

if response == None:
    print ("No response")
elif IP in response:
    if response.getlayer(IP).ttl <= 64 
        os="Linux"
    else:
        os = "Windows"    
    print "ttl value %d => %s" %(response.getlayer(IP).ttl, os)
