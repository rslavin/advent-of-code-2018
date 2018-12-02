import sys
import regex # not in stdlib, needed for regex fuzzing

lines = sys.stdin.readlines()

m = [l for l in lines for p in lines if regex.search(r'(%s){e<=1}'%p, l) and l != p]
print(''.join([j[0] for i, j in enumerate(zip(*m)) if all(j[0] == k for k in j[1:])]))
