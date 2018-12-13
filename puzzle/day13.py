from collections import Counter


class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.intersections_visited = 0
        self.crashed = False

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def location(self):
        return self.x, self.y

    def move(self, track):
        if track == '|':
            if self.direction == '^':
                self.north()
            elif self.direction == 'v':
                self.south()
            else:
                raise RuntimeError('Invalid direction')
        elif track == '-':
            if self.direction == '>':
                self.east()
            elif self.direction == '<':
                self.west()
            else:
                raise RuntimeError('Invalid direction')
        elif track == '/':
            if self.direction == '^':
                self.east()
            elif self.direction == 'v':
                self.west()
            elif self.direction == '<':
                self.south()
            elif self.direction == '>':
                self.north()
            else:
                raise RuntimeError('Invalid direction')
        elif track == '\\':
            if self.direction == '^':
                self.west()
            elif self.direction == 'v':
                self.east()
            elif self.direction == '<':
                self.north()
            elif self.direction == '>':
                self.south()
            else:
                raise RuntimeError('Invalid direction')
        elif track == '+':
            if self.intersections_visited % 3 == 0:
                if self.direction == '^':
                    self.west()
                elif self.direction == 'v':
                    self.east()
                elif self.direction == '<':
                    self.south()
                elif self.direction == '>':
                    self.north()
                else:
                    raise RuntimeError('Invalid direction')
            elif self.intersections_visited % 3 == 1:
                if self.direction == '^':
                    self.north()
                elif self.direction == 'v':
                    self.south()
                elif self.direction == '<':
                    self.west()
                elif self.direction == '>':
                    self.east()
                else:
                    raise RuntimeError('Invalid direction')
            elif self.intersections_visited % 3 == 2:
                if self.direction == '^':
                    self.east()
                elif self.direction == 'v':
                    self.west()
                elif self.direction == '<':
                    self.north()
                elif self.direction == '>':
                    self.south()
                else:
                    raise RuntimeError('Invalid direction')

            self.intersections_visited += 1
        else:
            raise RuntimeError('Invalid direction')

    def north(self):
        self.direction = '^'
        self.y -= 1

    def east(self):
        self.direction = '>'
        self.x += 1

    def south(self):
        self.direction = 'v'
        self.y += 1

    def west(self):
        self.direction = '<'
        self.x -= 1


def parse_tracks(input):
    input_without_carts = input.replace('<', '-').replace('>', '-').replace('^', '|').replace('v', '|')
    return [list(line.rstrip()) for line in input_without_carts.splitlines()]


def parse_carts(input):
    lines = [list(line) for line in input.splitlines()]
    carts = list()
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if cell in ['v', '^', '<', '>']:
                carts.append(Cart(x, y, cell))
    return carts


def first_crash_location(tracks, carts):
    while True:
        tick(tracks, carts)

        for cart in carts:
            if cart.crashed:
                return cart.location()


def tick(tracks, carts):
    for cart in carts:
        if not cart.crashed:
            cart.move(tracks[cart.y][cart.x])
            location, number_of_carts = Counter([cart.location() for cart in carts]).most_common(1)[0]
            if number_of_carts > 1:
                for crashed_cart in [cart for cart in carts if cart.location() == location]:
                    crashed_cart.crashed = True


def last_remaining_cart_location(tracks, carts):
    while True:
        tick(tracks, carts)

        carts = [cart for cart in carts if not cart.crashed]

        if len(carts) == 1:
            return carts[0].location()

