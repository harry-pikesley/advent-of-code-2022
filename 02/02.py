with open("02input.txt", "r") as f:
    input = f.readlines()
    input = [i.replace("\n", "") for i in input]    

# --- Part 1 ---
decisionPoints = 0
outcomePoints = 0

# Calculate decision points:
for i in input:
    if i == "A X" or i == "B X" or i == "C X":
        decisionPoints += 1
    elif i == "A Y" or i == "B Y" or i == "C Y":
        decisionPoints += 2
    else:
        decisionPoints += 3

# Calculate outcome points:
for i in input:
    if i == "C X" or i == "B Z" or i == "A Y":
        outcomePoints += 6
    elif i == "A X" or i == "B Y" or i == "C Z":
        outcomePoints += 3

totalPoints = decisionPoints + outcomePoints
print("PART 1:")
print("Decision Points = ", decisionPoints)
print("Outcome Points = ", outcomePoints)
print("Total Points = ", totalPoints)

# --- Part 2 ---
decisionPoints = 0
outcomePoints = 0
totalPoints = 0

# Calculate decision points
for i in input:
    if i == "A Y" or i == "B X" or i == "C Z":
        decisionPoints += 1
    elif i == "A Z" or i == "B Y" or i == "C X":
        decisionPoints += 2
    else:
        decisionPoints += 3

# Calculate outcome points
for i in input:
    if i[-1:] == "Z":
        outcomePoints += 6
    elif i[-1:] == "Y":
        outcomePoints += 3

totalPoints = decisionPoints + outcomePoints

print("PART 2:")
print("Decision Points = ", decisionPoints)
print("Outcome Points = ", outcomePoints)
print("Total Points = ", totalPoints)