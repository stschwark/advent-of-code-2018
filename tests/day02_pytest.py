from puzzle.day02 import *


def test_should_not_count_example1():
    assert letters_occur_exactly('abcdef', 2) is False
    assert letters_occur_exactly('abcdef', 3) is False


def test_should_count_example2_twice():
    assert letters_occur_exactly('bababc', 2) is True
    assert letters_occur_exactly('bababc', 3) is True


def test_should_count_example3_once():
    assert letters_occur_exactly('abbcde', 2) is True
    assert letters_occur_exactly('abbcde', 3) is False


def test_should_count_example4_once():
    assert letters_occur_exactly('abcccd', 2) is False
    assert letters_occur_exactly('abcccd', 3) is True


def test_should_count_example5_once():
    assert letters_occur_exactly('aabcdd', 2) is True
    assert letters_occur_exactly('aabcdd', 3) is False


def test_should_count_example6_once():
    assert letters_occur_exactly('abcdee', 2) is True
    assert letters_occur_exactly('abcdee', 3) is False


def test_should_count_example6_once():
    assert letters_occur_exactly('ababab', 2) is False
    assert letters_occur_exactly('ababab', 3) is True


def test_should_solve_part1():
    ids = open('day02_input.txt').read().splitlines()
    assert checksum(ids) == 6474


def test_should_find_common_letters_example1():
    assert common_letters('abcde', 'axcye') == 'ace'


def test_should_find_common_letters_example2():
    assert common_letters('fghij', 'fguij') == 'fgij'


def test_should_solve_part2():
    ids = open('day02_input.txt').read().splitlines()
    assert common_letters_of_two_similar_ids(ids) == 'mxhwoglxgeauywfkztndcvjqr'


