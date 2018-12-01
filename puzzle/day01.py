def frequency(changes):
    return sum(int(change) for change in changes)


def recurring_frequency(changes):
    result = 0
    seen = {0}

    while True:
        for change in changes:
            result += int(change)

            if result in seen:
                return result

            seen.add(result)
