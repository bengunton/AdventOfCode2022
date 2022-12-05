import sys

def parse_line(string):
    assignments = string.split(",")

    sections1 = assignments[0].split("-")
    sections2 = assignments[1].split("-")
    return ((int(sections1[0]), int(sections1[1])), (int(sections2[0]), int(sections2[1][:-1])))

filename = sys.argv[1]

with open(filename, 'r') as f:
    contents = f.readlines()

count = 0
for line in contents:
    if len(line) < 2:
        continue

    sections = parse_line(line)
    if sections[0][0] >= sections[1][0] and sections[0][1] <= sections[1][1]:
        count += 1
        continue

    if sections[1][0] >= sections[0][0] and sections[1][1] <= sections[0][1]:
        count += 1
        continue

print(count)

count = 0
for line in contents:
    if len(line) < 2:
        continue

    sections = parse_line(line)
    if sections[0][0] <= sections[1][0] and sections[0][1] >= sections[1][0]:
        count += 1
        continue

    if sections[1][0] <= sections[0][0] and sections[1][1] >= sections[0][0]:
        count += 1
        continue

print(count)
