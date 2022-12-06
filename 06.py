import timeit
start = timeit.default_timer()

with open("06input.txt", "r") as f:
    input = f.readlines()
    input = [i.replace("\n", "") for i in input]
    input = input[0]

def areDistinct(a, b, c, d):
    if (a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d):
        return True
    else:
        return False

partOneAnswer = 0
i = 0

while i < len(input) - 4:
    if areDistinct(str(input[i]), str(input[i + 1]), str(input[i + 2]), str(input[i + 3])):
        partOneAnswer = i + 4
        break
    i += 1

partTwoAnswer = 0
i = 0

while i < len(input) - 14:
    if len(set(input[i:i+14])) == 14:
        partTwoAnswer = i + 14
        break
    i += 1

print("Length of Input =", len(input))
print("Part 1 Answer =", partOneAnswer) # ANSWER = 1275
print("Part 2 Answer =", partTwoAnswer) # ANSWER = 3605

stop = timeit.default_timer()
print("Runtime:", 1000* (stop - start), "ms")