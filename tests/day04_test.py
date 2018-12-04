from puzzle.day04 import *
import os
from pandas import DataFrame


def test_should_parse_example_observations():
    observed = observations(example.splitlines())
    assert observed


def test_should_summarize_guard_patterns():
    observed = observations(example.splitlines())
    patterns = guard_pattern(observed)
    assert isinstance(patterns, DataFrame)


def test_solve_part1():
    input = sorted_input_data()
    observed = observations(input)
    pattern = guard_pattern(observed)
    assert strategy1(pattern) == 104764


def test_solve_part2():
    input = sorted_input_data()
    observed = observations(input)
    pattern = guard_pattern(observed)
    assert strategy2(pattern) == 128617


def sorted_input_data():
    lines = open(os.path.join(os.path.dirname(__file__), 'day04_input.txt')).read().splitlines()
    return sorted(lines)


example = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
