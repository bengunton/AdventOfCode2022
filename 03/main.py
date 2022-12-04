import sys

def get_priority(char):
    p = ord(char.swapcase()) - 64

    if p > 26:
        return p - 6
    return p

def find_duplicate(first, second):
    for char in first:
        if char in second:
            return char

def find_duplicate2(first, second, third):
    inBoth = [c for c in first if c in second]
    return find_duplicate(inBoth, third)


filename = str(sys.argv[1])

with open(filename, 'r') as f:
    contents = f.readlines()

sum = 0
for backpack in contents:
    first = backpack[:len(backpack)//2]
    second = backpack[len(backpack)//2:-1]

    if len(first) > 0:
        dup = find_duplicate(first, second)
        sum += get_priority(dup)

print(sum)

sum = 0
for i in [i * 3 for i in range(len(contents) // 3)]:
    elf1 = contents[i]
    elf2 = contents[i + 1]
    elf3 = contents[i + 2]

    sum += get_priority(find_duplicate2(elf1, elf2, elf3))

print(sum)
