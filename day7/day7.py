import sys
import re

children = {}
for line in sys.stdin:
    mo = re.search(r"Step (.).*(.) can", line)
    if mo.group(1) not in children:
        children[mo.group(1)] = []
    children[mo.group(1)].append(mo.group(2))

# map(lambda c: sorted(c), children)

end = None
ordered = []
roots = sorted([x for x in children.keys() if x not in [y for sublist in children.values() for y in sublist]])
def find_order(root):
    print(f"root: {root}")
    if root not in ordered:
        print(f"adding {root}")
        ordered.append(root)
    for n in sorted(children[root]):
        print(n)
        print([p for p in children.keys() if p not in ordered and p not in roots and n in children[p]])
        if n not in children.keys():
            global end
            end = n
        if n in children.keys() and not [p for p in children.keys() if p not in ordered and n in children[p]]:
            print(f"checking: {n}") # these are getting skipped in ordered
            # ordered.append(n) # appending it doesn't help
            # if parents in ordered, only call find_order if there are no parents before it
            find_order(n)
            # for m in children[n]:
            #     find_order(m)
        # else:
        #     ordered.append(m)
    print("----------------------")

for p in children.keys():
    print(f"{p} : {sorted(children[p])}")

for y in roots:
    print(y)
    find_order(y)
print("".join(ordered) + end)


# for last node, when you check for if you need to do the node,
# if it has no entry in children, it is the last one in the branch
# (recurse back up)


