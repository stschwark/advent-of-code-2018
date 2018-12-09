from puzzle.day09 import *


def test_should_play_example1():
    scores = play(players=9, rounds=25)
    assert max(scores.values()) == 32


def test_should_play_example2():
    scores = play(players=10, rounds=1618)
    assert max(scores.values()) == 8317


def test_should_play_example3():
    scores = play(players=13, rounds=7999)
    assert max(scores.values()) == 146373


def test_should_play_example4():
    scores = play(players=17, rounds=1104)
    assert max(scores.values()) == 2764


def test_should_play_example5():
    scores = play(players=21, rounds=6111)
    assert max(scores.values()) == 54718


def test_should_play_example5():
    scores = play(players=30, rounds=5807)
    assert max(scores.values()) == 37305


def test_should_solve_part1():
    scores = play(players=470, rounds=72170)
    assert max(scores.values()) == 388024


def test_should_solve_part2():
    scores = play(players=470, rounds=7217000)
    assert max(scores.values()) == 3180929875
