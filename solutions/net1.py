from socket import *
from struct import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 2998))

got = s.recv(1024)
print "Before: " + got.encode("hex")
strm = unpack("<I", got)[0]
print "After:  " + hex(strm)[2:]
s.send(str(strm))

print s.recv(1024)
s.close()