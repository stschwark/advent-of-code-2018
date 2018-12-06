from puzzle.day06 import *
import os

EXAMPLE_POINTS = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]


def test_should_calculate_distance():
    p1 = (1, 1)
    p2 = (1, 6)
    assert distance(p1, p2) == 5


def test_should_calculate_reverse_distance():
    p1 = (1, 1)
    p2 = (1, 6)
    assert distance(p2, p1) == 5


def test_should_calculate_top_left_of_bounding_box():
    top_left, bottom_right = bounding_box(EXAMPLE_POINTS)
    assert top_left == (1, 1)


def test_should_calculate_bottom_right_of_bounding_box():
    top_left, bottom_right = bounding_box(EXAMPLE_POINTS)
    assert bottom_right == (8, 9)


def test_should_find_closest_neighbour():
    assert closest_neighbour((3, 2), EXAMPLE_POINTS) == (3, 4)


def test_should_return_no_closest_neighbour_in_a_tie():
    assert closest_neighbour((0, 4), EXAMPLE_POINTS) is None


def test_should_calculate_area_sizes():
    areas = area_sizes([(1, 1), (8,9)], EXAMPLE_POINTS)
    assert sorted(areas.values()) == [7, 9, 9, 10, 12, 17]


def test_should_calculate_largest_enclosed_area():
    assert largest_enclosed_area(EXAMPLE_POINTS) == 17


def test_should_solve_part1():
    coors = read_coordinates_from_file('day06_input.txt')
    assert largest_enclosed_area(coors) == 4171


def test_calculate_total_distance_to_neighbours():
    assert total_distance_to_neighbours((4, 3), EXAMPLE_POINTS) == 30


def test_should_calculate_densest_area():
    assert densest_area_size(EXAMPLE_POINTS, 32) == 16


def test_should_solve_part2():
    coors = read_coordinates_from_file('day06_input.txt')
    assert densest_area_size(coors, 10000) == 39545


def read_coordinates_from_file(file_name):
    return [tuple(map(int, line.split(', '))) for line in
            open(os.path.join(os.path.dirname(__file__), file_name)).read().splitlines()]
