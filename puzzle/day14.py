def find_next_ten_recipes_after(after_recipes):
    scoreboard = '37'
    elf1 = 0
    elf2 = 1

    while len(scoreboard) < after_recipes + 10:
        scoreboard += str(int(scoreboard[elf1]) + int(scoreboard[elf2]))
        elf1 = (elf1 + int(scoreboard[elf1]) + 1) % len(scoreboard)
        elf2 = (elf2 + int(scoreboard[elf2]) + 1) % len(scoreboard)

    return scoreboard[after_recipes:after_recipes + 10]


def find_number_of_recipes_before_sequence(sequence):
    scoreboard = '37'
    elf1 = 0
    elf2 = 1

    while sequence not in scoreboard[(-1 * len(sequence) - 2):]:
        scoreboard += str(int(scoreboard[elf1]) + int(scoreboard[elf2]))
        elf1 = (elf1 + int(scoreboard[elf1]) + 1) % len(scoreboard)
        elf2 = (elf2 + int(scoreboard[elf2]) + 1) % len(scoreboard)

    return scoreboard.find(sequence)
