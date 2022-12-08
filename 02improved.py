import time

startTime = time.monotonic_ns()

with open("02input.txt", "r") as f:
    lines = [i for i in f.read().strip().split("\n")]
    f.close()

# --- ALL POSSIBLE OUTCOMES FOR PART 1 ---
# OPPONENT VS USER | OUTCOME | (CHOICE + OUTCOME) = TOTAL
# A vs X | DRAW | 1 + 3 = 4
# A vs Y | WIN | 2 + 6 = 8
# A vs Z | LOSS | 3 + 0 = 3
# B vs X | LOSS | 1 + 0 = 1
# B vs Y | DRAW | 2 + 3 = 5
# B vs Z | WIN | 3 + 6 = 9
# C vs X | WIN | 1 + 6 = 7
# C vs Y | LOSS | 2 + 0 = 2
# C vs Z | DRAW  | 3 + 3 = 6

outcomes = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

# --- ALL POSSIBLE OUTCOMES FOR PART 2 ---
# OPPONENT VS REQUIRED OUTCOME | USER | (CHOICE + OUTCOME) = TOTAL
# A vs X | SCISSORS | 3 + 0 = 3
# A vs Y | ROCK | 1 + 3 = 4
# A vs Z | PAPER | 2 + 6 = 8
# B vs X | ROCK | 1 + 0 = 1
# B vs Y | PAPER | 2 + 3 = 5
# B vs Z | SCISSORS | 3 + 6 = 9
# C vs X | PAPER | 2 + 0 = 2
# C vs Y | SCISSORS | 3 + 3 = 6
# C vs Z | ROCK  | 1 + 6 = 7

desiredOutcomes = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}

totalPointsP1, totalPointsP2 = 0, 0

for line in lines:
    totalPointsP1 += outcomes[line]
    totalPointsP2 += desiredOutcomes[line]

print("Solution to Part 1: ", totalPointsP1)
print("Solution to Part 2: ", totalPointsP2)

endTime = time.monotonic_ns()

print("Time Taken: ", f'{(endTime - startTime)/(10**9):.5f}', "s", sep = "")