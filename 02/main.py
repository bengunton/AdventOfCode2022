import sys

ROCK_O = 'A'
PAPER_O = 'B'
SCISSORS_O = 'C'

ROCK_P = 'X'
PAPER_P = 'Y'
SCISSORS_P = 'Z'

WIN_P = 'Z'
DRAW_P = 'Y'
LOSE_P = 'X'

WIN = 6
DRAW = 3

ROCK = 1
PAPER = 2
SCISSORS = 3

def calculate_score(opponent, player):
    if opponent == ROCK_O:
        if player == ROCK_P:
            return DRAW + ROCK
        elif player == PAPER_P:
            return WIN + PAPER
        elif player == SCISSORS_P:
            return SCISSORS
    elif opponent == PAPER_O:
        if player == ROCK_P:
            return ROCK
        elif player == PAPER_P:
            return DRAW + PAPER
        elif player == SCISSORS_P:
            return WIN + SCISSORS
    elif opponent == SCISSORS_O:
        if player == ROCK_P:
            return WIN + ROCK
        elif player == PAPER_P:
            return PAPER
        elif player == SCISSORS_P:
            return DRAW + SCISSORS
    return 0

def calculate_score_2(opponent, player):
    if opponent == ROCK_O:
        if player == WIN_P:
            return WIN + PAPER 
        elif player == DRAW_P:
            return DRAW + ROCK 
        elif player == LOSE_P:
            return SCISSORS
    elif opponent == PAPER_O:
        if player == WIN_P:
            return WIN + SCISSORS 
        elif player == DRAW_P:
            return DRAW + PAPER
        elif player == LOSE_P:
            return ROCK
    elif opponent == SCISSORS_O:
        if player == WIN_P:
            return WIN + ROCK
        elif player == DRAW_P:
            return DRAW + SCISSORS
        elif player == LOSE_P:
            return PAPER
    return 0

filename = str(sys.argv[1])

with open(filename, 'r') as f:
    contents = f.readlines()

sum = 0
sum2 = 0
for line in contents:
    if len(line) == 4:
        sum += calculate_score(line[0], line[2])
        sum2 += calculate_score_2(line[0], line[2])
print(sum)
print(sum2)
