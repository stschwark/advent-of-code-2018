from puzzle.day14 import *


def test_should_find_next_ten_recipes_for_example_1():
    assert find_next_ten_recipes_after(9) == '5158916779'


def test_should_find_next_ten_recipes_for_example_2():
    assert find_next_ten_recipes_after(5) == '0124515891'


def test_should_find_next_ten_recipes_for_example_3():
    assert find_next_ten_recipes_after(18) == '9251071085'


def test_should_find_next_ten_recipes_for_example_3():
    assert find_next_ten_recipes_after(2018) == '5941429882'


def test_should_solve_part1():
    assert find_next_ten_recipes_after(440231) == '1052903161'


def test_should_find_number_of_recipes_before_sequence_example_1():
    assert find_number_of_recipes_before_sequence('51589') == 9


def test_should_find_number_of_recipes_before_sequence_example_2():
    assert find_number_of_recipes_before_sequence('01245') == 5


def test_should_find_number_of_recipes_before_sequence_example_3():
    assert find_number_of_recipes_before_sequence('92510') == 18


def test_should_find_number_of_recipes_before_sequence_example_3():
    assert find_number_of_recipes_before_sequence('59414') == 2018


def test_should_solve_part2():
    assert find_number_of_recipes_before_sequence('440231') == 20165504
