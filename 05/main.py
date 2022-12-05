import sys
import re

filename = sys.argv[1]
with open(filename, 'r') as f:
    contents = f.readlines()

towers = [[] for i in range(9)]
moves = []

move_regex = re.compile("move (\\d+) from (\\d+) to (\\d+)")

def parse_move(line):
    result = move_regex.match(line)   
    groups = result.groups()
    n1 = int(groups[0])
    n2 = int(groups[1])
    n3 = int(groups[2])
    return (n1, n2, n3)

def parse_contents(contents):
    for line in contents:
        for i in range(len(line)):
            if line[i] == '[':
                letter = line[i + 1]
                towers[i//4].insert(0, letter)
            i += 4

        if line.startswith("move"):
            moves.append(parse_move(line))

parse_contents(contents)

# Version 1
# for m in moves:
#     repeats = m[0]
#     source = m[1] - 1
#     target = m[2] - 1
# 
#     for i in range(repeats):
#         letter = towers[source].pop()
#         towers[target].append(letter)

# Version 2
for m in moves:
    repeats = m[0]
    source = m[1] - 1
    target = m[2] - 1

    letters = []
    for i in range(repeats):
        letters.append(towers[source].pop())

    for i in range(repeats):
        towers[target].append(letters.pop())

line = ""
for tower in towers:
    if len(tower) > 0:
        line += str(tower[-1])

print(line)
