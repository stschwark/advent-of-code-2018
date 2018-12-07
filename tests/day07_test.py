from puzzle.day07 import *
import os


def test_should_read_instructions():
    assert all_instructions(EXAMPLE_INPUT) == EXAMPLE_INSTRUCTIONS


def test_should_list_steps_in_assembly_order():
    assert steps_in_assembly_order(EXAMPLE_INSTRUCTIONS) == ['C', 'A', 'B', 'D', 'F', 'E']


def test_should_solve_part1():
    lines = open(os.path.join(os.path.dirname(__file__), 'day07_input.txt')).read().splitlines()
    instructions = all_instructions(lines)
    assert ''.join(steps_in_assembly_order(instructions)) == 'ABDCJLFMNVQWHIRKTEUXOZSYPG'


def test_should_calculate_time_to_assembly():
    assert time_to_assembly(EXAMPLE_INSTRUCTIONS, effort=lambda step: ord(step) - ord('A') + 1, number_of_workers=2) == 15


def test_should_solve_part2():
    lines = open(os.path.join(os.path.dirname(__file__), 'day07_input.txt')).read().splitlines()
    instructions = all_instructions(lines)
    assert time_to_assembly(instructions, effort=lambda step: ord(step) - ord('A') + 1 + 60, number_of_workers=5) == 896


EXAMPLE_INSTRUCTIONS = [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]

EXAMPLE_INPUT = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".splitlines()
