import sys

coords = [x.strip().split(", ") for x in sys.stdin]

pixel_coords = {}
for x in range(int(min(coords, key=lambda i: int(i[0]))[0]), int(max(coords, key=lambda i: int(i[0]))[0])):
    for y in range(int(min(coords, key=lambda i: int(i[1]))[1]), int(max(coords, key=lambda i: int(i[1]))[1])):
        pairs = {}
        for c in coords:
            pairs[coords.index(c)] = abs(x - int(c[0])) + abs(y - int(c[1]))
        winner = min(pairs, key=lambda p: pairs[p])
        if sum(v == pairs[winner] for v in pairs.values()) == 1:
            pixel_coords[winner] = pixel_coords.get(winner, 0) + 1

print(pixel_coords[max(pixel_coords, key=lambda k: pixel_coords[k])])
