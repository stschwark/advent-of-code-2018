from puzzle.day03 import *
import os


def test_should_parse_claim():
    assert claim_from_string("#123 @ 3,2: 5x4") == Claim(123, 3, 2, 5, 4)


def test_should_determine_area():
    assert Claim(123, 3, 2, 3, 2).area() == frozenset(
        [(3, 2), (4, 2), (5, 2),
         (3, 3), (4, 3), (5, 3)])


def test_should_calculate_overlap():
    claims = [claim_from_string('#1 @ 1,3: 4x4'),
              claim_from_string('#2 @ 3,1: 4x4'),
              claim_from_string('#3 @ 5,5: 2x2')]

    assert locations_with_overlap(claims) == 4


def test_should_solve_part1():
    claims = claims_from_file('day03_input.txt')
    assert locations_with_overlap(claims) == 118539


def test_should_solve_part2():
    claims = claims_from_file('day03_input.txt')
    assert first_claim_without_overlap(claims).id == 1270


def claims_from_file(name):
    input = open(os.path.join(os.path.dirname(__file__), name)).read().splitlines()
    return [claim_from_string(s) for s in input]
