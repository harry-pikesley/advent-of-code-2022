import time
import numpy as np

startTime = time.monotonic_ns()

instructions = open("10input.txt", "r").readlines()

cycleValues = [1]

for instruction in instructions:
    if instruction.startswith("a"):
        for i in range(2):
            if i == 0:
                cycleValues.append(cycleValues[-1])
            if i == 1:
                cycleValues.append(cycleValues[-1] + int(instruction.split()[1]))
    elif instruction.startswith("n"):
        cycleValues.append(cycleValues[-1])

output = ""
for i, value in enumerate(cycleValues):
    if cycleValues[i] in range((i % 40) - 1, (i % 40) + 2):
        output += "#"
    else:
        output += "."
    if (i + 1) % 40 == 0:
        output += "\n"

print("Part 1 Solution:", sum([i * cycleValues[i] for i in [20, 60, 100, 140, 180, 220]]))
print("Part 2 Solution:")
print(output)

endTime = time.monotonic_ns()

print("Time Taken: ", f'{(endTime - startTime)/(10**9):.5f}', "s", sep = "")