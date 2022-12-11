data = []
delimiter = " "

with open("05input.txt", "r") as f:
    for line in f.readlines():
        element = []
        for token in line.strip().split(delimiter):
            element.append(token)
        data.append(element)

import numpy as np

stacks1 = [[""], ["Z", "P", "B", "Q", "M", "D", "N"].reverse(), 
["V", "H", "D", "M", "Q", "Z", "L", "C"].reverse(),
["G", "Z", "F", "V", "D", "R", "H", "Q"].reverse(),
["N", "F", "D", "G", "H"].reverse(),
["Q", "F", "N"].reverse(),
["T", "B", "F", "Z", "V", "Q", "D"].reverse(),
["H", "S", "V", "D", "Z", "T", "M", "Q"].reverse(),
["Q", "N", "P", "F", "G", "M"].reverse(),
["M", "R", "W", "B"].reverse()]

stacks = [[""], ["N", "D", "M", "Q", "B", "P", "Z"],
["C", "L", "Z", "Q", "M", "D", "H", "V"],
["Q", "H", "R", "D", "V", "F", "Z", "G"],
["H", "G", "D", "F", "N"],
["N", "F", "Q"],
["D", "Q", "V", "Z", "F", "B", "T"],
["Q", "M", "T", "Z", "D", "V", "S", "H"],
["M", "G", "F", "P", "N", "Q"],
["B", "W", "R", "M"]]

print(data)

for item in data:
    f = int(item[3])
    t = int(item[5])
    for times in range(int(item[1])):
        letter = stacks[f][-1]
        stacks[f].pop(-1)
        stacks[t].append(letter)
    
solution = ""
for stack in stacks:
    solution += stack[-1]

print(solution)

stacks = [[""], ["N", "D", "M", "Q", "B", "P", "Z"],
["C", "L", "Z", "Q", "M", "D", "H", "V"],
["Q", "H", "R", "D", "V", "F", "Z", "G"],
["H", "G", "D", "F", "N"],
["N", "F", "Q"],
["D", "Q", "V", "Z", "F", "B", "T"],
["Q", "M", "T", "Z", "D", "V", "S", "H"],
["M", "G", "F", "P", "N", "Q"],
["B", "W", "R", "M"]]

for item in data:
    f = int(item[3])
    t = int(item[5])
    x = []
    for times in range(int(item[1])):
        letter = stacks[f][-1]
        stacks[f].pop(-1)
        x.insert(0, letter)
    for letter in x:
        stacks[t].append(letter)

solution = ""
for stack in stacks:
    solution += stack[-1]

print(solution)