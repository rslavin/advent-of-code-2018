import sys
import re

freq = 0
for line in sys.stdin:
    mo = re.search(r"([+-])(\d+)", line)
    freq = freq + int(mo.group(2)) if mo.group(1) == "+" else freq - int(mo.group(2))

print(freq)
