import time

startTime = time.monotonic_ns()

with open("01input.txt", "r") as f:
    data = f.readlines()
    lines = [i.replace("\n", "") for i in data]
    f.close()

calories, calorieCounts = 0, []

for line in lines:
    if len(line) == 0:
        calorieCounts.append(calories)
        calories = 0
    else:
        calories += int(line)

calorieCounts.sort()

print("Highest Individual Calories:", sum(calorieCounts[-1:]))
print("Sum of Three Highest Individual Calories:", sum(calorieCounts[-3:]))

endTime = time.monotonic_ns()

print("Time Taken: ", f'{(endTime - startTime)/(10**9):.5f}', "s", sep = "")