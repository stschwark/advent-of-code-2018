import re


def time_to_message(input):
    points = parse_input(input)
    elapsed = 0
    while not might_contain_letters(points):
        tick(points)
        elapsed += 1
    plot(points)
    return elapsed


class Point:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def tick(self, repetitions=1):
        self.position = ((self.position[0] + repetitions * self.velocity[0]),
                         (self.position[1] + repetitions * self.velocity[1]))


def parse_input(input):
    p = re.compile(r'position=<\s*([\d+-]+),\s*([\d+-]+)> velocity=<\s*([\d+-]+),\s*([\d+-]+)>')
    result = list()
    for line in input.splitlines():
        px, py, vx, vy = re.match(p, line).groups()
        result.append(Point((int(px), int(py)), (int(vx), int(vy))))
    return result


def tick(points, repetitions=1):
    for point in points:
        point.tick(repetitions=repetitions)
    return points


def might_contain_letters(points):
    positions = set([point.position for point in points])
    for point in points:
        x, y = point.position
        if not any([
            (x-1, y-1) in positions,
            (x, y-1) in positions,
            (x+1, y-1) in positions,
            (x+1, y) in positions,
            (x+1, y+1) in positions,
            (x, y+1) in positions,
            (x-1, y+1) in positions,
            (x-1, y) in positions
        ]):
            return False
    return True


def plot(points):
    positions = [point.position for point in points]
    xs = [position[0] for position in positions]
    ys = [position[1] for position in positions]
    top_left = min(xs), min(ys)
    bottom_right = max(xs), max(ys)

    print()
    for y in range(top_left[1],  bottom_right[1] + 1):
        for x in range(top_left[0], bottom_right[0] + 1):
            print('#' if (x, y) in positions else '.', end='')
        print()






