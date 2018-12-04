import sys
import re

f = [[0] * 1000 for i in range(1000)]

for line in sys.stdin:
    m = re.search(r".+@ (\d+),(\d+): (\d+)x(\d+)", line)
    for p in range(int(m.group(1)), int(m.group(1)) + int(m.group(3))):
            f[p][int(m.group(2)):int(m.group(2))+int(m.group(4))] = \
                [v + 1 for v in f[p][int(m.group(2)):int(m.group(2)) + int(m.group(4))]]

print(sum(1 if y > 1 else 0 for x in f for y in x))
