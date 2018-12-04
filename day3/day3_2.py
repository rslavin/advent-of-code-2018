import sys
import re

f = [[0] * 1000 for i in range(1000)]

lines = sys.stdin.readlines()

for line in lines:
    m = re.search(r".+@ (\d+),(\d+): (\d+)x(\d+)", line)
    for p in range(int(m.group(1)), int(m.group(1)) + int(m.group(3))):
        if int(m.group(1)) <= p < int(m.group(1)) + int(m.group(3)):
            f[p][int(m.group(2)):int(m.group(2)) + int(m.group(4))] = \
                [v + 1 for v in f[p][int(m.group(2)):int(m.group(2)) + int(m.group(4))]]

for line in lines:
    m = re.search(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
    n = False
    for x in f[int(m.group(2)):int(m.group(2)) + int(m.group(4))]:
        if sum(1 for y in x[int(m.group(3)):int(m.group(3)) + int(m.group(5))] if y > 1):
            n = True
            break
    if not n:
        print(m.group(1))
        exit()
