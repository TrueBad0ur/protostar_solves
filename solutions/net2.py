from socket import *
from struct import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 2997))

sum = 0
for i in range(4):
        got = s.recv(1024)
        number = int(unpack("<I", got)[0])
        print "number " + i + ": " + str(number)
        sum += number
print "sum: " + str(sum)
sum = pack("<I", sum)
s.send(str(sum))

print s.recv(1024)
s.close()