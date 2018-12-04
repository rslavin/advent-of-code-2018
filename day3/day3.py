import sys
import re

f = [[0] * 1000] * 1000

for line in sys.stdin:
    m = re.search(r".+@ (\d+),(\d+): (\d+)x(\d+)", line)
    for p, x in enumerate(f):
        if int(m.group(1)) <= p < int(m.group(1)) + int(m.group(3)):
            f[p] = ([(v + 1 if int(m.group(2)) <= i < int(m.group(2)) + int(m.group(4)) else v) for i,v in enumerate(x)])

print(sum(1 if y > 1 else 0 for x in f for y in x))
