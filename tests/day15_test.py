from puzzle.day15 import *
import os


def test_should_find_enemies():
    enemies = enemies_of([Unit(1, 2, 'G'), Unit(3, 4, 'E'), Unit(5, 6, 'G')], of=Unit(3, 4, 'E'))
    assert enemies == [Unit(1, 2, 'G'), Unit(5, 6, 'G')]


def test_should_identify_when_unit_is_in_range_of_target():
    targets = [Unit(1, 2, 'G'), Unit(8, 9, 'G')]
    assert is_unit_in_range_of_a_target(Unit(1, 1, 'E'), targets) is True


def test_should_identify_when_unit_is_not_in_range_of_target():
    targets = [Unit(1, 2, 'G'), Unit(8, 9, 'G')]
    assert is_unit_in_range_of_a_target(Unit(5, 5, 'E'), targets) is False


def test_should_calculate_shortest_path_to_nearest_in_range_position():
    start = [
        "#######",
        "#E..G.#",
        "#...#.#",
        "#.G.#G#",
        "#######"
    ]
    area = AreaMap(start)
    elf = area.units()[0]
    goblins = enemies_of(area.units(), of=elf)

    paths = area.shortest_path_to_nearest_in_range_position(elf, goblins)

    assert paths == [(1, 1), (2, 1), (3, 1)]


def test_should_simulate_combat_round_1():
    start = [
        "#######",
        "#.G...#",
        "#...EG#",
        "#.#.#G#",
        "#..G#E#",
        "#.....#",
        "#######"
    ]

    rounds, area = simulate_combat(start, max_rounds=1)

    assert area.plot() == [
        "#######",
        "#..G..#",
        "#...EG#",
        "#.#G#G#",
        "#...#E#",
        "#.....#",
        "#######"
    ]


def test_should_simulate_combat_round_2():
    start = [
        "#######",
        "#..G..#",
        "#...EG#",
        "#.#G#G#",
        "#...#E#",
        "#.....#",
        "#######"
    ]

    rounds, area = simulate_combat(start, max_rounds=1)

    assert area.plot() == [
        "#######",
        "#...G.#",
        "#..GEG#",
        "#.#.#G#",
        "#...#E#",
        "#.....#",
        "#######"
    ]


def test_should_simulate_combat_round_23():
    start = [
        "#######",
        "#.G...#",
        "#...EG#",
        "#.#.#G#",
        "#..G#E#",
        "#.....#",
        "#######"
    ]

    rounds, area = simulate_combat(start, max_rounds=23)

    print(area.plot())

    assert area.plot() == [
        "#######",
        "#...G.#",
        "#..G.G#",
        "#.#.#G#",
        "#...#E#",
        "#.....#",
        "#######"
    ]


def test_should_simulate_combat_round_47():
    start = [
        "#######",
        "#.G...#",
        "#...EG#",
        "#.#.#G#",
        "#..G#E#",
        "#.....#",
        "#######"
    ]

    rounds, area = simulate_combat(start, max_rounds=47)

    assert area.plot() == [
        "#######",
        "#G....#",
        "#.G...#",
        "#.#.#G#",
        "#...#.#",
        "#....G#",
        "#######"
    ]


def test_should_solve_part1():
    start = open(os.path.join(os.path.dirname(__file__), 'day15_input.txt')).read().splitlines()
    rounds, area = simulate_combat(start)
    assert (rounds, area.remaining_hitpoints()) == (81, 2690)


def test_should_solve_part2():
    start = open(os.path.join(os.path.dirname(__file__), 'day15_input.txt')).read().splitlines()

    rounds, area = simulate_combat(start, attack_power={'G': 3, 'E': 28})

    assert area.elves_lost() == 0
    assert rounds * area.remaining_hitpoints() == 43645


