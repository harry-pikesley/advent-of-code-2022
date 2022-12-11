with open("03input.txt", "r") as f:
    input = f.readlines()
    input = [i.replace("\n", "") for i in input]

# Function to find common letters in two strings
def findCommon(str1, str2):
    com_str = ''.join(set(str1).intersection(str2))
    return(com_str)

# Function to convert letters to their value
def letterToNumber(l):
    if l.isupper():
        return ord(l) - 38
    else:
        return ord(l) - 96

# --- PART 1 ---
total = 0

for line in input:
    lineTotal = 0
    firstHalf, secondHalf = line[:len(line)//2], line[len(line)//2:]
    common = findCommon(firstHalf, secondHalf)
    for i in firstHalf:
        if i in secondHalf:
            if letterToNumber(i) > lineTotal:
                lineTotal = letterToNumber(i)
    total += lineTotal

print("Total: ", total)

# --- PART 2 ---
# Splitting the input into batches of 3 lines
chunks = []

for i in range(0, len(input), 3):
    chunks.append(input[i:i+3])

newTotal = 0

for chunk in chunks:
    ruck1, ruck2, ruck3 = chunk[0], chunk[1], chunk[2]
    chunkTotal = 0
    for i in ruck1:
        if i in ruck2 and i in ruck3:
            chunkTotal = letterToNumber(i)
    newTotal += chunkTotal

print("Total: ", newTotal)