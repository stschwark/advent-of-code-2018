def sum_meta(input):
    values = [int(x) for x in input.split()]
    meta = meta_from(values)
    return sum(meta)


def meta_from(values):
    result = []

    children = values.pop(0)
    meta_entries = values.pop(0)

    for _ in range(children):
        result.extend(meta_from(values))

    for _ in range(meta_entries):
        result.append(values.pop(0))

    return result


def root_node_value(input):
    values = [int(x) for x in input.split()]
    value = value_of(values)
    return value


def value_of(values):
    children = values.pop(0)
    meta_entries = values.pop(0)
    child_values = [value_of(values) for _ in range(children)]

    if children == 0:
        return sum([values.pop(0) for _ in range(meta_entries)])
    else:
        meta = [values.pop(0) for _ in range(meta_entries)]
        return sum([child_values[i - 1] if 0 <= i - 1 < len(child_values) else 0 for i in meta])
