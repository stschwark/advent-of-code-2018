from puzzle.day16 import *
import os


def test_should_parse_samples():
    assert parse_samples(SAMPLE) == [Sample(
        before=[3, 2, 1, 1],
        opcode=9,
        params=[2, 1, 2],
        after=[3, 2, 2, 1]
    )]


def test_should_solve_part1():
    input = open(os.path.join(os.path.dirname(__file__), 'day16_input_1.txt')).read()
    samples = parse_samples(input)
    assert number_of_samples_that_behave_like_at_least_three_opcodes(samples) == 544


def test_should_learn_operations_by_opcodes():
    input = open(os.path.join(os.path.dirname(__file__), 'day16_input_1.txt')).read()
    samples = parse_samples(input)
    mapping = learn_operations_by_opcode(samples)
    assert mapping == OPERATIONS_BY_OPCODE


def test_should_solve_part2():
    input = open(os.path.join(os.path.dirname(__file__), 'day16_input_2.txt')).read()
    assert run(input, OPERATIONS_BY_OPCODE)[0] == 600


SAMPLE = """Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]"""

OPERATIONS_BY_OPCODE = {0: addi, 1: eqrr, 2: borr, 3: gtri, 4: addr, 5: seti, 6: muli, 7: bani,
                      8: banr, 9: gtrr, 10: setr, 11: gtir, 12: bori, 13: eqri, 14: eqir, 15: mulr}
