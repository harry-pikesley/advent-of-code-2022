with open("01input.txt", "r") as f:
    input = f.readlines()
    input = [i.replace("\n", "") for i in input]

calorieCounts = []

calories = 0
for i in input:
    if len(i) == 0:
        calorieCounts.append(calories)
        calories = 0
    else:
        calories += int(i)

calorieCounts.sort()
top = sum(calorieCounts[-1:])
topThree = sum(calorieCounts[-3:])
print(f"Highest Individual Calories: {top}")
print(f"Total calories: {topThree}")