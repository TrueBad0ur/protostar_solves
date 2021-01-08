# start net0 binary and then run script
from socket import *
from struct import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 2999))
strm = s.recv(1024)

begin = strm.find("'") + 1
end = strm.find("'", begin)
number = int(strm[begin:end])
print "Before: " + str(hex(number))
done = pack("<I", number)
print "After:  0x" + done.encode("hex")
s.send(done)
print s.recv(1024)