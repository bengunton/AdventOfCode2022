import sys

def parse_input(filename):

    rows = []
    for line in contents:
        row = []

        for char in line[:-1]:
            num = int(char)
            row.append(num)

        rows.append(row)

    return rows


def mark_visible(rows):

    visible_trees = [[False] * len(x) for x in rows]

    for i in range(len(rows)):

        max_height = -1
        for j in range(len(rows[i])):
            if j == 0:
                visible_trees[i][j] = True
                max_height = rows[i][j]
                continue
            if rows[i][j] > rows[i][j-1] and rows[i][j] > max_height:
                visible_trees[i][j] = True
                max_height = rows[i][j]
                continue

        max_height = -1
        for j in range(len(rows[i]) - 1, -1, -1):
            if j == (len(rows[i]) - 1):
                visible_trees[i][j] = True
                max_height = rows[i][j]
                continue
            if rows[i][j] > rows[i][j + 1] and rows[i][j] > max_height:
                visible_trees[i][j] = True
                max_height = rows[i][j]
                continue

    for j in range(len(rows[0])):

        max_height = -1
        for i in range(len(rows)):
            if i == 0:
                visible_trees[i][j] = True
                max_height = rows[i][j]
                continue
            
            if rows[i][j] > rows[i - 1][j] and rows[i][j] > max_height:
                visible_trees[i][j] = True
                max_height = rows[i][j]
                continue

        max_height = -1
        for i in range(len(rows) -1, -1, -1):
            if i == (len(rows[i]) - 1):
                visible_trees[i][j] = True
                max_height = rows[i][j]
                continue
            
            if rows[i][j] > rows[i + 1][j] and rows[i][j] > max_height:
                visible_trees[i][j] = True
                max_height = rows[i][j]
                continue

    return visible_trees

def calculate_visibility(rows, i, j):
    height = rows[i][j]

    up = 0
    index = i - 1
    while index >= 0:
        up += 1
        index -= 1

        if rows[index + 1][j] >= height:
            break

    down = 0
    index = i + 1
    while index < len(rows):
        down += 1
        index += 1

        if rows[index - 1][j] >= height:
            break

    left = 0
    index = j - 1
    while index >= 0:
        left += 1
        index -= 1

        if rows[i][index + 1] >= height:
            break

    right = 0
    index = j + 1
    while index < len(rows[i]):
        right += 1
        index += 1
        
        if rows[i][index - 1] >= height:
           break

    return up * down * left * right

def mark_visibility(rows):
    visibility_trees = [[0] * len(x) for x in rows]

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            visibility_trees[i][j] = calculate_visibility(rows, i, j)

    return visibility_trees

def count_true(visible):
    return sum([row.count(True) for row in visible])

def max_visibility(rows):
    return max([max(row) for row in rows])

filename = sys.argv[1]

with open(filename, 'r') as f:
    contents = f.readlines()

rows = parse_input(filename)

visible = mark_visible(rows)

print(count_true(visible))

visibility = mark_visibility(rows)
print(max_visibility(visibility))
