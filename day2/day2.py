import sys
import re

c = [0]*2
for line in sys.stdin:
    c[0] += 1 if [w for w in list(line) if len(re.findall(w, line)) == 2] else 0
    c[1] += 1 if [w for w in list(line) if len(re.findall(w, line)) == 3] else 0

print(c[0]*c[1])
