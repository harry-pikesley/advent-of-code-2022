with open("04input.txt", "r") as f:
    input = f.readlines()
    input = [i.replace("\n", "") for i in input]

count = 0

for line in input:
    elfOne, elfTwo = line.split(",")
    a, b = elfOne.split("-")
    c, d = elfTwo.split("-")
    a, b, c, d = int(a), int(b), int(c), int(d)
    if (a <= c and d <= b) or (c <= a and b <= d):
        print(line)
        print(a, b, c, d)
        count += 1

print("Total = ", count) # Answer = 485

newCount = 0
lineCount = 0

for line in input:
    lineCount += 1
    elfOne, elfTwo = line.split(",")
    a, b = elfOne.split("-")
    c, d = elfTwo.split("-")
    a, b, c, d = int(a), int(b), int(c), int(d)
    if (b < c) or (d < a):
        newCount += 1
    
print(lineCount - newCount) # Answer = 857