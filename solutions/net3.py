from socket import *
from struct import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 2996))

resource = "net3"
resource = pack("B", len(resource)+1) + resource + "\x00"

user = "awesomesauce"
user = pack("B", len(user)+1) + user + "\x00"

password = "password"
password = pack("B", len(password)+1) + password + "\x00"

auth = "\x17" + resource + user + password # \x17 magic number in protocol
length = pack(">H",len(auth))

packet = length + auth

print packet.encode("hex")
s.sendall(packet)

print s.recv(1024)
s.close()