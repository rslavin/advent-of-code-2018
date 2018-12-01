import sys
import re

freq = 0
freqs = set()
while True:
    with open(sys.argv[1]) as f:
        for line in f:
            mo = re.search(r"([+-])(\d+)", line)
            freq = freq + int(mo.group(2)) if mo.group(1) == "+" else freq - int(mo.group(2))
            if freq in freqs:
                print(freq)
                exit()
            freqs.add(freq)
