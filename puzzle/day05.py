def units_remaining_after_reaction(polymer):
    return len(react(polymer))


def react(polymer):
    previous_polymer = None
    while previous_polymer != polymer:
        previous_polymer = polymer
        for reactive in REACTIVE_UNITS:
            polymer = polymer.replace(reactive, '')
    return polymer


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def units_remaining_after_manipulation_and_reaction(polymer):
    unit_pairs = zip(char_range('a', 'z'), char_range('A', 'Z'))
    all_lengths = [len(react(remove_units_from(polymer, unit_pair))) for unit_pair in unit_pairs]
    return min(all_lengths)


def remove_units_from(polymer, to_be_removed):
    for unit in to_be_removed:
        polymer = polymer.replace(unit, '')
    return polymer


REACTIVE_UNITS = [''.join(pair) for pair in zip(char_range('a', 'z'), char_range('A', 'Z'))] \
                 + [''.join(pair) for pair in zip(char_range('A', 'Z'), char_range('a', 'z'))]


