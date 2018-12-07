import sys
import re

children = {}
for line in sys.stdin:
    mo = re.search(r"Step (.).*(.) can", line)
    if mo.group(1) not in children:
        children[mo.group(1)] = []
    children[mo.group(1)].append(mo.group(2))

map(lambda c: sorted(c), children)

ordered = []
end = None
def find_order(root):
    print(f"root: {root}")
    if root not in children.keys():
        print(f"skipping: {root}")
        global end
        end = root
        return()
    ordered.append(root) # maybe move this
    for n in children[root]:
        # if all of its parents are in ordered
        if n in children.keys() and not [p for p in children.keys() if p in ordered and n in p]:
            print(f"checking: {n}") # these are getting skipped in ordered
            # ordered.append(n) # appending it doesn't help
            # find_order(n)
            for m in children[n]:
                find_order(m)
        # else:
        #     ordered.append(m)


find_order(next(iter(children)))
print("".join(ordered) + end)


# for last node, when you check for if you need to do the node,
# if it has no entry in children, it is the last one in the branch
# (recurse back up)


