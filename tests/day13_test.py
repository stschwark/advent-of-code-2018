from puzzle.day13 import *
import os


def test_should_parse_tracks():
    tracks = parse_tracks(EXAMPLE_INPUT)
    assert tracks[0] == ['/', '-', '-', '-', '\\']


def test_should_parse_carts():
    carts = parse_carts(EXAMPLE_INPUT)
    assert carts == [Cart(2, 0, '>'), Cart(9, 3, 'v')]


def test_should_find_first_crash_location():
    tracks = parse_tracks(EXAMPLE_INPUT)
    carts = parse_carts(EXAMPLE_INPUT)
    assert first_crash_location(tracks, carts) == (7, 3)


def test_should_solve_part1():
    input = open(os.path.join(os.path.dirname(__file__), 'day13_input.txt')).read()
    tracks = parse_tracks(input)
    carts = parse_carts(input)
    assert first_crash_location(tracks, carts) == (86, 118)


def test_should_solve_part2():
    input = open(os.path.join(os.path.dirname(__file__), 'day13_input.txt')).read()
    tracks = parse_tracks(input)
    carts = parse_carts(input)
    assert last_remaining_cart_location(tracks, carts) == (2, 81)


EXAMPLE_INPUT = """/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/   """
