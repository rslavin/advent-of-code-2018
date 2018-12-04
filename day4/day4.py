import sys
import re

pattern = re.compile(r"\[(.*)\] (.*)")
lines = dict()
for line in sys.stdin:
    mo = pattern.search(line)
    lines[mo.group(1)] = mo.group(2)

lines = sorted(lines.items(), key=lambda t: t[0])

minutes = dict()
guard = start = end = None
for k, v in lines:
    mo = re.search(r"#(\d+)", v)

    if start and end:
        if guard not in minutes:
            minutes[guard] = [0] * 60
        minutes[guard][start:end] = [v + 1 for v in minutes[guard][start:end]]
        start = end = None
    if mo:
        guard = mo.group(1)
        start = end = None
    elif start is None:
        start = int(re.search(r":(\d+)", k).group(1))
    elif end is None:
        end = int(re.search(r":(\d+)", k).group(1))

g = max(minutes.keys(), key=(lambda i: max(minutes[i])))
print(minutes[str(g)].index(max(minutes[str(g)])) * int(g))
