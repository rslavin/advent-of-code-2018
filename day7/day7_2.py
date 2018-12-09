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
queue = sorted(list(steps) + [x for x in children if x not in [y for sublist in children.values() for y in sublist]])
ready = []

i = 0
time = 0
workers = [0] * 5
slots = [""] * 5
while True:
    for w in range(len(workers)):
        if not workers[w] and len(ready):
            ready.sort()
            workers[w] = ord(ready[0].lower()) - 36
            slots[w] = ready.pop(0)
        if workers[w] == 1:
            complete.append(slots[w])
            slots[w] = ""

    while i < len(queue):
        step = queue[i]
        i += 1
        if step not in ready + complete + slots and not [p for p in children if p not in complete and step in children[p]]:
            ready.append(step)
            i = 0
    if not len(ready) and not sum(workers):
        break
    workers = list(map(lambda x: x - 1 if x > 0 else x, workers))
    time += 1
    i = 0

print(time + max(workers) - 1)
