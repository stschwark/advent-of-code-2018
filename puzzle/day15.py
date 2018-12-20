import networkx as nx
from itertools import chain


class Unit:
    def __init__(self, x, y, type, attack_power=3):
        self.x = x
        self.y = y
        self.type = type
        self.attack_power = attack_power
        self.hitpoints = 200

    def position(self):
        return self.x, self.y

    def reading_order(self):
        return self.y, self.x

    def take_damage(self, points=3):
        self.hitpoints -= points

    def alive(self):
        return self.hitpoints > 0

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class AreaMap:
    def __init__(self, input, attack_power={'E': 3, 'G': 3}):
        self.__area = [list(line) for line in input]
        self.__units = []
        for y in range(len(self.__area)):
            for x in range(len(self.__area[0])):
                type = self.__area[y][x]
                if type in ['E', 'G']:
                    unit = Unit(x, y, type, attack_power[type])
                    self.__units.append(unit)
                    self.__area[y][x] = '.'
        self.elves_at_start = len([unit for unit in self.__units if unit.type == 'E'])

    def units(self):
        return self.__units

    def area(self):
        return self.__area

    def plot(self):
        canvas = self.__area.copy()
        for unit in self.__units:
            canvas[unit.y][unit.x] = unit.type
        return [''.join(row) for row in canvas]

    def position_is_within_area(self, x, y):
        return 0 <= y < len(self.__area) and 0 <= x < len(self.__area[0]) and self.__area[y][x] == '.'

    def shortest_path_to_nearest_in_range_position(self, unit, targets):
        graph = nx.Graph()
        position_of_other_units = [other.position() for other in self.__units if other != unit]
        for y1 in range(len(self.__area)):
            for x1 in range(len(self.__area[0])):
                if self.position_is_within_area(x1, y1) and not (x1, y1) in position_of_other_units:
                    for x2, y2 in neighbours(x1, y1):
                        if self.position_is_within_area(x2, y2) and not (x2, y2) in position_of_other_units:
                            graph.add_edge((x1, y1), (x2, y2))

        if unit.position() not in graph.nodes:
            return None

        in_range_positions = set(chain.from_iterable([neighbours(*target.position()) for target in targets]))
        in_range_positions = set([position for position in in_range_positions if position in graph.nodes()])

        reachable_positions = [position for position in in_range_positions if nx.has_path(graph, unit.position(), position)]

        if reachable_positions:
            nearest_position, distance = min(
                [(position, nx.shortest_path_length(graph, unit.position(), position)) for position in reachable_positions],
                key=lambda t: (t[1], t[0][1], t[0][0])
            )

            shortest_path = min(
                nx.all_shortest_paths(graph, unit.position(), nearest_position),
                key=lambda path: (len(path), path[-1][1], path[-1][0])
            )

            return shortest_path
        else:
            return None

    def remaining_hitpoints(self):
        return sum([unit.hitpoints for unit in self.__units])

    def elves_lost(self):
        return self.elves_at_start - len([unit for unit in self.__units if unit.type == 'E'])

    def remove_dead(self):
        self.__units = sorted([unit for unit in self.__units if unit.alive()], key=lambda unit: unit.reading_order())


def simulate_combat(input, attack_power={'E': 3, 'G': 3}, max_rounds=99):
    rounds = 0

    area = AreaMap(input, attack_power=attack_power)

    while rounds < max_rounds:
        units = area.units()

        for unit in units:
            if not unit.alive():
                continue

            targets = enemies_of(area.units(), of=unit)

            if len(targets) == 0:
                return rounds, area

            if not is_unit_in_range_of_a_target(unit, targets):
                selected_path = area.shortest_path_to_nearest_in_range_position(unit, targets)
                if selected_path:
                    unit.x, unit.y = selected_path[1]

            if is_unit_in_range_of_a_target(unit, targets):
                in_reach = sorted([opposing_unit for opposing_unit in targets if opposing_unit.position() in neighbours(*unit.position())], key=lambda unit: unit.hitpoints)
                if in_reach:
                    in_reach[0].take_damage(unit.attack_power)
                    area.remove_dead()

        rounds += 1

    return rounds, area


def enemies_of(units, of):
    return [unit for unit in units if unit.type == ('G' if of.type == 'E' else 'E')]


def is_unit_in_range_of_a_target(unit, targets):
    target_positions = [unit.position() for unit in targets]
    return any(position in neighbours(*unit.position()) for position in target_positions)


def neighbours(x, y):
    return [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
