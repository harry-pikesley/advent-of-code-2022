import time
import numpy as np

startTime = time.monotonic_ns()

with open("09input.txt", "r") as f:
    moves = [line.split() for line in f.readlines()]

posHead, posTail = [0, 0], [0, 0] # Head and Tail start overlapping on the same cell
visited = []

def directionToVector(direction):
    if direction == "L":
        return [0, -1]
    elif direction == "R":
        return [0, 1]
    elif direction == "U":
        return [1, 0]
    elif direction == "D":
        return [-1, 0]

def updateHead(vector, currentPosHead):
    currentPosHead[0] += vector[0]
    currentPosHead[1] += vector[1]
    return currentPosHead

def updateTail(currentPosHead, currentPosTail, previousPosHead):
    deltaHead = [currentPosHead[0] - previousPosHead[0], currentPosHead[1] - previousPosHead[1]]

    if abs(currentPosHead[0] - currentPosTail[0]) > 1 or abs(
            currentPosHead[1] - currentPosTail[1]) > 1:

        if (previousPosHead[0] == currentPosTail[0]) or (previousPosHead[1] == currentPosTail[1]):
            return [currentPosTail[0] + deltaHead[0], currentPosTail[1] + deltaHead[1]]

        else:
            diff = [currentPosHead[0] - currentPosTail[0], currentPosHead[1] - currentPosTail[1]]

            return [currentPosTail[0] + (np.sign(diff[0]) * min(abs(diff[0]), 1)),
                    currentPosTail[1] + (np.sign(diff[1]) * min(abs(diff[1]), 1))]

    else:
        return list(currentPosTail)

def solve(moveList, numLinks=2):
    currentPositions = [[0, 0] for _ in range(numLinks)]
    lastLinkHistory = [(0, 0)]
    for move, i in moveList:
        for moveNumber in range(int(i)):
            vector = directionToVector(move)
            prevTailPosition = tuple(currentPositions[0])
            currentPositions[0] = updateHead(vector, currentPositions[0])
            for tail_num in range(numLinks - 1):
                nextPrevTailPosition = tuple(currentPositions[tail_num + 1])
                currentPositions[tail_num + 1] = updateTail(currentPositions[tail_num],
                                                              currentPositions[tail_num + 1],
                                                              prevTailPosition)
                prevTailPosition = nextPrevTailPosition
                if tail_num == numLinks - 2:
                    lastLinkHistory.append(tuple(currentPositions[numLinks - 1]))
    return len(set(lastLinkHistory))

print("1. Unique Positions Visited:", solve(moves, 2)) # 5883
print("2. Unique Positions Visited:", solve(moves, 10)) # 2367 

endTime = time.monotonic_ns()

print("Time Taken: ", f'{(endTime - startTime)/(10**9):.5f}', "s", sep = "")