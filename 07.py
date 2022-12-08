import sys
from collections import defaultdict

# --- PART 1 FOLLOWED A YOUTUBE VIDEO AS THIS IS TOO HARD FOR ME ---
infile = sys.argv[1] if len(sys.argv) > 1 else "07input.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

path = []
SZ = defaultdict(int)

for line in lines:
    words = line.strip().split()
    if words[1] == "cd":
        if words[2] == "..":
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == "ls":
        continue
    else:
        try:
            sz = int(words[0])
            print(path, sz)
            for i in range(len(path) + 1):
                SZ["/".join(path[:i])] += sz
        except:
            pass

"""
ans = 0
for k, v in SZ.items():
    print(k, v)
    if v <= 100000:
        ans += v
print(ans)
"""

# --- PART 2 ---
maxUsed = 70000000 - 30000000
totalUsed = SZ["/"]
needToFree = totalUsed - maxUsed
best = 1e9
ans2 = 0
for k, v in SZ.items():
    if v >= needToFree:
        best = min(best, v)
        print(k, v)
    if v <= 100000:
        ans2 += v
print(ans2)
print(best)