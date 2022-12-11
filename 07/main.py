import sys
import re

filename = sys.argv[1]

f = open(filename, 'r')

line = f.readline()

class Dir:
    def __init__(self):
        self.level = 0
        self.children = []
        self.parent = None
        self.name = "/"
        self.size = 0

    def __str__(self):
        s = f"{self.name}: {self.level}, {self.size}\n"
        for c in self.children:
            s += "  " + str(c) + "\n"
        return s

    def sum(self):
        total = 0
        for c in self.children:
            c.sum()
            total += c.size
        self.size = self.level + total

    def sum_big(self):
        total = 0
        for c in self.children:
            total += c.sum_big()

        if self.size <= 100000:
            total += self.size

        return total

    def get_smallest_child(self, min_size):
        smallest_size = sys.maxsize
        smallest_child = None

        for c in self.children:

            if c.size >= min_size and c.size < smallest_size :
                smallest_size = c.size
                smallest_child = c

            c2 = c.get_smallest_child(min_size)

            if c2 != None and c2.size >= min_size and c2.size < smallest_size:
                smallest_size = c2.size
                smallest_child = c2

        return smallest_child


directory = Dir()
topDir = directory

while line != "":

    if line.startswith("$ cd"):
        parts = line.split(" ")
        name = parts[2].strip()
        if name == "/":
            directory = topDir
        elif name == "..":
            directory = directory.parent
        else:
            newDir = Dir()
            newDir.parent = directory
            newDir.name = name
            directory.children.append(newDir)
            directory = newDir


    if line.startswith("$ ls"):

        line = f.readline()
        level = 0

        while line != "" and not line.startswith("$"):

            match = re.search("^\\d+", line)

            if match != None:
                level += int(match.group())

            line = f.readline()

        directory.level = level

        continue

    line = f.readline()

f.close()

topDir.sum()

print("part 1: ", topDir.sum_big())

total_space = 70000000

free_space = total_space - topDir.size
needed_space = 30000000 - free_space
print("needed: ", needed_space, " top: ", topDir.size)

smallest_child = topDir.get_smallest_child(needed_space)
print(smallest_child.name, ": ", smallest_child.size)
