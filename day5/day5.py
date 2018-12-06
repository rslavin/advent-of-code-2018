import regex
import sys
regex.DEFAULT_VERSION = regex.VERSION1

def reduce(str):
    str_reduced = regex.sub(r"(?!(.)\1)(.)((?i)\2)", "", str)
    if str_reduced == str:
        return str
    return reduce(str_reduced)

print(len(reduce(sys.stdin.readline())))
