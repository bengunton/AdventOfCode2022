import sys
from collections import deque

filename = sys.argv[1]

# for part 1
def has_duplicates(deq):
    return (deq[0] == deq[1] or deq[0] == deq[2] or deq[0] == deq[3]
        or deq[1] == deq[2] or deq[1] == deq[3]
        or deq[2] == deq[3])

# for part 2
def has_duplicates_2(deq):
    for i in range(len(deq)):
        for j in range(i + 1, len(deq)):
            if deq[i] == deq[j]:
                return True 
    return False 

with open(filename) as f:

    count = 0
    deq = deque([], maxlen=14)

    while count < 4 or has_duplicates_2(deq):

        char = f.read(1)
        deq.append(char)

        count += 1

    print(count)

