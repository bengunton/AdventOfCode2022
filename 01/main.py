import sys

if len(sys.argv) != 2:
    print("provide file name")
    sys.exit(-1)

print(str(sys.argv[0]))
filename = str(sys.argv[1])

with open(filename, 'r') as f:
    contents = f.readlines()

biggest1 = 0
biggest2 = 0
biggest3 = 0
total = 0
for entry in contents:

    if entry == "\n":
        if biggest1 < total:
            biggest3 = biggest2
            biggest2 = biggest1
            biggest1 = total

        elif biggest2 < total:
            biggest3 = biggest2
            biggest2 = total 

        elif biggest3 < total:
            biggest3 = total

        total = 0
        continue

    num = int(entry)
    total += num 

print(biggest3 + biggest2 + biggest1)


