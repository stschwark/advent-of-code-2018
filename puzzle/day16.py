import re


class Sample:
    def __init__(self, before, opcode, params, after):
        self.before = before
        self.opcode = opcode
        self.params = params
        self.after = after

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def parse_samples(input):
    lines = input.splitlines()
    result = []
    for index in range(0, len(lines), 4):
        result.append(Sample(
            before=[int(reg) for reg in re.findall(r'\d+', lines[index])],
            opcode=int(lines[index + 1].split(' ')[0]),
            params=[int(s) for s in lines[index + 1].split(' ')][1:4],
            after=[int(reg) for reg in re.findall(r'\d+', lines[index + 2])]
        ))
    return result


def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]


def addi(reg, a, b, c):
    reg[c] = reg[a] + b


def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]


def muli(reg, a, b, c):
    reg[c] = reg[a] * b


def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]


def bani(reg, a, b, c):
    reg[c] = reg[a] & b


def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]


def bori(reg, a, b, c):
    reg[c] = reg[a] | b


def setr(reg, a, b, c):
    reg[c] = reg[a]


def seti(reg, a, b, c):
    reg[c] = a


def gtir(reg, a, b, c):
    reg[c] = 1 if a > reg[b] else 0


def gtri(reg, a, b, c):
    reg[c] = 1 if reg[a] > b else 0


def gtrr(reg, a, b, c):
    reg[c] = 1 if reg[a] > reg[b] else 0


def eqir(reg, a, b, c):
    reg[c] = 1 if a == reg[b] else 0


def eqri(reg, a, b, c):
    reg[c] = 1 if reg[a] == b else 0


def eqrr(reg, a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0


all_operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


def number_of_samples_that_behave_like_at_least_three_opcodes(samples):
    candidates = candidate_operations_per_sample(samples)
    return len(list(filter(lambda ops: len(ops) > 3, candidates.values())))


def learn_operations_by_opcode(samples):
    remaining_operations = all_operations.copy()
    relevant_samples = samples.copy()
    mapping = {}

    while len(remaining_operations) > 0:
        candidates = candidate_operations_per_sample(relevant_samples, remaining_operations)

        for index in candidates.keys():
            if len(candidates[index]) == 1:
                opcode = relevant_samples[index].opcode
                operation = candidates[index][0]
                mapping[opcode] = operation
                remaining_operations = list(filter(lambda o: o != operation, remaining_operations))
                relevant_samples = list(filter(lambda s: s.opcode != opcode, relevant_samples))
                break

    return mapping


def run(input, operations_by_opcode):
    regs = [0, 0, 0, 0]
    for line in input.splitlines():
        opcode, a, b, c = [int(s) for s in line.split(' ')]
        operation = operations_by_opcode[opcode]
        operation(regs, a, b, c)

    return regs


def candidate_operations_per_sample(samples, operations=all_operations):
    result = dict()
    for index, sample in enumerate(samples):
        result[index] = []
        for operation in operations:
            regs = sample.before.copy()
            operation(regs, *sample.params)
            if regs == sample.after:
                result[index].append(operation)

    return result
