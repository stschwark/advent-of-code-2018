def growing_conditions(input):
    all_rules = [line.split(' => ') for line in input.splitlines()]
    return [rule[0] for rule in all_rules if rule[1] == '#']


def filled_pots(input):
    return [number for (number, content) in enumerate(input) if content == '#']


def calculate_generation(initial, conditions, generations):
    current_state = initial
    for generation in range(generations):
        next_state = []
        for index in range(min(current_state) - 2, max(current_state) + 2):
            if pattern(current_state, index - 2, index + 2) in conditions:
                next_state.append(index)

        # take a shortcut once the state has stabilised
        if normalised(current_state) == normalised(next_state):
            offset = min(next_state) - min(current_state)
            end_state = [number - 1 + offset * (generations - generation) for number in next_state]
            return sum(end_state)

        current_state = next_state

    return sum(current_state)


def pattern(state, start, end):
    return ''.join(['#' if index in state else '.' for index in range(start, end + 1)])


def normalised(state):
    return [number - min(state) for number in state]





