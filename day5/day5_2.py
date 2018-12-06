import regex
import sys

regex.DEFAULT_VERSION = regex.VERSION1

line = sys.stdin.readline()
low = len(line)
for l in "abcdefghijklmnopqrstuvwxyz":
    str_reduced = regex.sub(l, '', line, flags=regex.I)
    while True:
        size = len(str_reduced)
        str_reduced = regex.sub(r"(?!(.)\1)(.)((?i)\2)", "", str_reduced)
        if size == len(str_reduced):
            break

    low = min([len(str_reduced), low])

print(low)
