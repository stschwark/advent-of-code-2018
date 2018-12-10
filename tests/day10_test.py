from puzzle.day10 import *
import os


def test_should_parse_input():
    point = parse_input(EXAMPLE_INPUT)[0]
    assert point.position == (9, 1)
    assert point.velocity == (0, 2)


def test_should_calculate_next_position():
    points = [Point((9, 1), (0, 2))]
    tick(points)
    assert points[0].position == (9, 3)
    assert points[0].velocity == (0, 2)


def test_should_not_find_letters_in_initial_example():
    points = parse_input(EXAMPLE_INPUT)
    assert might_contain_letters(points) is False


def test_should_find_letters_in_example_after_3_seconds():
    points = parse_input(EXAMPLE_INPUT)
    tick(points, repetitions=3)
    assert might_contain_letters(points) is True


def test_should_solve_example():
    assert time_to_message(EXAMPLE_INPUT) == 3


def test_should_solve_part_1_and_2():
    input = open(os.path.join(os.path.dirname(__file__), 'day10_input.txt')).read()
    assert time_to_message(input) == 10459


EXAMPLE_INPUT = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""
