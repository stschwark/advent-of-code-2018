from puzzle.day12 import *
import os


def test_should_parse_rules():
    conditions = growing_conditions(EXAMPLE_RULES)
    assert len(conditions) == 14


def test_should_parse_initial_state():
    filled = filled_pots(EXAMPLE_INITIAL_STATE)
    assert filled == [0, 3, 5, 8, 9, 16, 17, 18, 22, 23, 24]


def test_should_calculate_first_generation():
    assert calculate_generation(
        initial=filled_pots(EXAMPLE_INITIAL_STATE),
        conditions=growing_conditions(EXAMPLE_RULES),
        generations=20) == 325

def test_should_solve_part1():
    initial_state = '#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............'
    input = open(os.path.join(os.path.dirname(__file__), 'day12_input.txt')).read()

    assert calculate_generation(
        initial=filled_pots(initial_state),
        conditions=growing_conditions(input),
        generations=20) == 1696

def test_should_solve_part2():
    initial_state = '#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............'
    input = open(os.path.join(os.path.dirname(__file__), 'day12_input.txt')).read()

    assert calculate_generation(
        initial=filled_pots(initial_state),
        conditions=growing_conditions(input),
        generations=50000000000) == 1799999999458


EXAMPLE_INITIAL_STATE = "#..#.#..##......###...###"
EXAMPLE_RULES = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""
