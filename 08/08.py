import numpy as np
import time

startTime = time.monotonic_ns()

with open("08input.txt", "r") as f:
    input = f.readlines()
    inputLists = np.array([[int(i) for i in currentList.strip()] for currentList in input])

borderCount = 2 * ((inputLists.shape[0] - 1) + (inputLists.shape[1] - 1))
visible = []

# VISIBLE FROM TOP
for row in range(1, inputLists.shape[0] - 1):
    currentRow = inputLists[row, 1:-1]
    maxHeights = np.max(inputLists[:row, 1:-1], axis = 0)
    visible.extend([(row, el + 1) for el in np.where(currentRow > maxHeights)[0]])

# DOWN
for row in range(inputLists.shape[0] - 1, 1, -1):
    currentRow = inputLists[row - 1, 1:-1]
    maxHeights = np.max(inputLists[row:, 1:-1], axis=0)
    visible.extend([(row - 1, el + 1) for el in np.where(currentRow > maxHeights)[0]])

# LEFT
for column in range(1, inputLists.shape[1] - 1):
    currentColumn = inputLists[1:-1, column]
    maxHeights = np.max(inputLists[1:-1, :column], axis=1)
    visible.extend([(el + 1, column) for el in np.where(currentColumn > maxHeights)[0]])

# RIGHT
for column in range(inputLists.shape[1] - 1, 1, -1):
    currentColumn = inputLists[1:-1, column - 1]
    maxHeights = np.max(inputLists[1:-1, column:], axis=1)
    visible.extend([(el + 1, column - 1) for el in np.where(currentColumn > maxHeights)[0]])

print("Part 1 Solution:", len(set(visible)) + borderCount) #1809

endTime = time.monotonic_ns()

print("Time Taken: ", f'{(endTime - startTime)/(10**9):.5f}', "s", sep = "")