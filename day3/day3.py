import sys
import re

fabric = [[0]*1000] * 1000

for line in sys.stdin:
    m = re.search(r".+@ (\d+),(\d+): (\d+)x(\d+)", line)
    for p, x in enumerate(fabric):
        if int(m.group(1)) <= p < int(m.group(1)) + int(m.group(3)):
            fabric[p] = ([(v + 1 if int(m.group(2)) <= i < int(m.group(2)) + int(m.group(4)) else v) for i,v in enumerate(x)])

total = 0
for x in fabric:
    for y in x:
        if y > 1:
            total += 1 if y > 1 else 0

print(total)
