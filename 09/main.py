import sys

class Instruction:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str((self.direction, self.distance))

def parse_input(lines):
    instructions = []

    for line in lines:
        parts = line.split(' ')

        if len(parts) >= 2:
            direction = parts[0]
            distance = int(parts[1])
            
            instructions.append(Instruction(direction, distance))

    return instructions

def is_next_to(point1, point2):
    return abs(point1[0] - point2[0]) <= 1 and abs(point1[1] - point2[1]) <= 1

def direction_to_move(target, current):
    if target[1] == current[1] and target[0] - current[0] > 1:
        return "R"
    if target[1] == current[1] and current[0] - target[0] > 1:
        return "L"
    if target[0] == current[0] and target[1] - current[1] > 1:
        return "U"
    if target[0] == current[0] and current[1] - target[1] > 1:
        return "D"
    return "Diagonal"

def move(direction, head, tail):
    old_head = head

    if direction == "U":
        head = (head[0], head[1] + 1)
    if direction == "D":
        head = (head[0], head[1] - 1)
    if direction == "L":
        head = (head[0] - 1, head[1])
    if direction == "R":
        head = (head[0] + 1, head[1])

    if not is_next_to(head, tail):
        tail = old_head

    return head, tail

def move_single(direction, knot):

    if direction == "U":
        knot = (knot[0], knot[1] + 1)
    if direction == "D":
        knot = (knot[0], knot[1] - 1)
    if direction == "L":
        knot = (knot[0] - 1, knot[1])
    if direction == "R":
        knot = (knot[0] + 1, knot[1])

    return knot

def get_next_pos(target, current):
    
    t_x = target[0]
    t_y = target[1]
    c_x = current[0]
    c_y = current[1]

    if (t_x - c_x) == 2 and (t_y - c_y) == 1:
        return (c_x + 1, c_y + 1)
    if (t_x - c_x) == 1 and (t_y - c_y) == 2:
        return (c_x + 1, c_y + 1)
    if (t_x - c_x) == 2 and (t_y - c_y) == 2:
        return (c_x + 1, c_y + 1)

    if (t_x - c_x) == 2 and (t_y - c_y) == -1:
        return (c_x + 1, c_y - 1)
    if (t_x - c_x) == 1 and (t_y - c_y) == -2:
        return (c_x + 1, c_y - 1)
    if (t_x - c_x) == 2 and (t_y - c_y) == -2:
        return (c_x + 1, c_y - 1)

    if (t_x - c_x) == -2 and (t_y - c_y) == 1:
        return (c_x - 1, c_y + 1)
    if (t_x - c_x) == -1 and (t_y - c_y) == 2:
        return (c_x - 1, c_y + 1)
    if (t_x - c_x) == -2 and (t_y - c_y) == 2:
        return (c_x - 1, c_y + 1)

    if (t_x - c_x) == -2 and (t_y - c_y) == -1:
        return (c_x - 1, c_y - 1)
    if (t_x - c_x) == -1 and (t_y - c_y) == -2:
        return (c_x - 1, c_y - 1)
    if (t_x - c_x) == -2 and (t_y - c_y) == -2:
        return (c_x - 1, c_y - 1)


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        contents = f.readlines()

    instructions = parse_input(contents)

    head = (0, 0)
    tail = (0, 0)
    tail_positions = {tail}
    for instruction in instructions:
        length = instruction.distance

        for i in range(length):
            head, tail = move(instruction.direction, head, tail)
            tail_positions.add(tail)

    print("part 1")
    print(len(tail_positions))
    print(head, tail)

    knots = [(0, 0) for x in range(10)]
    tail_positions = {(0, 0)}
    for instruction in instructions:
        length = instruction.distance

        for i in range(length):

            knots[0] = move_single(instruction.direction, knots[0])

            for i in range(1, len(knots)):
                if not is_next_to(knots[i], knots[i-1]):
                    dir_to_move = direction_to_move(knots[i-1], knots[i])

                    if dir_to_move == "Diagonal":
                        knots[i] = get_next_pos(knots[i-1], knots[i])
                    else:
                        knots[i] = move_single(dir_to_move, knots[i])

            tail_positions.add(knots[9])

    print("part 2")
    print(len(tail_positions))
    print(knots)

if __name__ == "__main__":
    main()


