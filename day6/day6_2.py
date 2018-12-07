import sys

coords = [x.strip().split(", ") for x in sys.stdin]

pixel_coords = {}
size = 0
for x in range(int(min(coords, key=lambda i: int(i[0]))[0]), int(max(coords, key=lambda i: int(i[0]))[0])):
    for y in range(int(min(coords, key=lambda i: int(i[1]))[1]), int(max(coords, key=lambda i: int(i[1]))[1])):
        total = 0
        for c in coords:
            total += abs(x - int(c[0])) + abs(y - int(c[1]))
        size += 1 if total < 10000 else 0

print(size)
