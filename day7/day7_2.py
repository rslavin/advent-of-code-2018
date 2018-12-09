import day7

steps, children = day7.find_order()

time = 0
complete = []
roots = [x for x in children.keys() if x not in [y for sublist in children.values() for y in sublist]]
workers = [0] * 5
slots = [None] * 5
while len(steps):
    print(steps)
    for i in range(len(workers)):
        # if worker is free and step[0] has complete dependencies
        if workers[i] == 1:
            print(f"completing {slots[i]}")
            complete.append(slots[i]) # can't use pop here because we need to preserve length/order
            slots[i] = None
        print(f"testing {steps[0]}: parents: { [p for p in children if (p not in complete or p not in roots) and steps[0] in children[p]]}")
        if not workers[i] and len(steps) and (steps[0] in roots or not [p for p in children if (p not in complete or p not in roots) and steps[0] in children[p]]):
            print(f"adding {steps[0]} ({ord(steps[0].lower()) - 36}) to worker")
            slots[i] = steps[0]
            workers[i] = ord(steps.pop(0).lower()) - 36

    time += 1
    print(workers)
    workers = list(map(lambda x: x - 1 if x > 0 else x, workers))
    print(workers)
    if sum(workers) ==\
            0:
        exit()


print(time)
time += max(workers)

print(time)