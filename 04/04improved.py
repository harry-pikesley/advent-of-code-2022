import time
import re

startTime = time.monotonic_ns()

with open("04input.txt", "r") as f:
    input = f.readlines()
    input = [i.replace("\n", "") for i in input]

part1Total, part2Total = 0, 0

for line in input:
    [a, b, c, d] = re.split('-|,', line)
    a, b, c, d = int(a), int(b), int(c), int(d)
    if (a <= c and d <= b) or (c <= a and b <= d):
        part1Total += 1
    if not((b < c) or (d < a)):
        part2Total += 1

print("Part 1 Solution:", part1Total)
print("Part 2 Solution:", part2Total)

endTime = time.monotonic_ns()

print("Time Taken: ", f'{(endTime - startTime)/(10**9):.5f}', "s", sep = "")