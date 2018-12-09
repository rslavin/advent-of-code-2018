import sys
import re

children = {}
steps = set()
for line in sys.stdin:
    mo = re.search(r"Step (.).*(.) can", line)
    if mo.group(1) not in children:
        children[mo.group(1)] = []
    children[mo.group(1)].append(mo.group(2))
    steps.add(mo.group(2))

complete = []
ready = sorted([x for x in children if x not in [y for sublist in children.values() for y in sublist]])
complete.append(ready.pop(0))
queue = sorted(list(steps) + ready)

i = 0
while i < len(queue):
    step = queue[i]
    i += 1
    if step in ready or not [p for p in children if p not in complete and step in children[p]]:
        if step not in ready + complete:
            ready.append(step)
        queue.remove(step)
        i = 0
        ready.sort()
        complete.append(ready.pop(0))

print("".join(complete))
