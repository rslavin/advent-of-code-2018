import sys
import re

fabric = [[0] * 1000] * 1000

lines = sys.stdin.readlines()

for line in lines:
    m = re.search(r".+@ (\d+),(\d+): (\d+)x(\d+)", line)
    for p, x in enumerate(fabric):
        if int(m.group(1)) <= p < int(m.group(1)) + int(m.group(3)):
            fabric[p] = (
            [(v + 1 if int(m.group(2)) <= i < int(m.group(2)) + int(m.group(4)) else v) for i, v in enumerate(x)])

for line in lines:
    m = re.search(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
    n = False
    for x in fabric[int(m.group(2)):int(m.group(2)) + int(m.group(4))]:
        if sum(1 for y in x[int(m.group(3)):int(m.group(3)) + int(m.group(5))] if y > 1):
            n = True
            break
    if not n:
        print(m.group(1))
        exit()
