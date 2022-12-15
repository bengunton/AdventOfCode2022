import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    contents = f.readlines()

signals = [0 for x in range(len(contents) * 2)]
signals[0] = 1

count = 0
for line in contents:
    parts = line.split(' ')

    instruction = parts[0]

    # if instruction == "noop":
        # count += 1
    
    if instruction == "addx":
        signals[count + 2] += int(parts[1])
        count += 2
    else:
        count += 1

for i in range(len(signals)):
    if i > 0:
        signals[i] += signals[i - 1]

print("Part 1")
print("20: ", signals[19], "strength:", 20 * signals[19])
print("60: ", signals[59], "strength:", 60 * signals[59])
print("100: ", signals[99], "strength:", 100 * signals[99])
print("140: ", signals[139], "strength:", 140 * signals[139])
print("180: ", signals[179], "strength:", 180 * signals[179])
print("220: ", signals[219], "strength:", 220 * signals[219])

print(20 * signals[19] + 
        60 * signals[59] +
        100 * signals[99] +
        140 * signals[139] +
        180 * signals[179] +
        220 * signals[219])

crt = ["." for x in signals]

for i in range(len(signals)):
    sprite_pos = i % 40
    if signals[i] - 1 <= sprite_pos and signals[i] + 1 >= sprite_pos:
        crt[i] = "#"

print(signals)

print("".join(crt[0:40]))
print("".join(crt[40:80]))
print("".join(crt[80:120]))
print("".join(crt[120:160]))
print("".join(crt[160:200]))
print("".join(crt[200:240]))
