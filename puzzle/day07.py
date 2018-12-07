import re


def all_instructions(lines):
    p = re.compile(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin\.')
    return [p.match(line).groups() for line in lines]


def steps_in_assembly_order(instructions):
    assembly = Assembly(instructions, lambda step: 0)
    assembly.assemble(1)
    return assembly.completed_steps


def time_to_assembly(instructions, effort, number_of_workers):
    assembly = Assembly(instructions, effort)
    assembly.assemble(number_of_workers)
    return assembly.elapsed_time


class Assembly:
    def __init__(self, instructions, effort_for_step):
        self.remaining_instructions = instructions
        self.effort_for_step = effort_for_step
        self.remaining_steps = self.__remaining_steps_alphabetically()
        self.elapsed_time = 0
        self.work_in_progress = dict()
        self.completed_steps = []

    def assemble(self, number_of_workers):
        while len(self.remaining_steps) > 0 or len(self.work_in_progress) > 0:
            self.__assign_work(number_of_workers)
            self.__finish_next_in_progress_step()

    def __remaining_steps_alphabetically(self):
        return sorted(set([element for tupl in self.remaining_instructions for element in tupl]))

    def __assign_work(self, number_of_workers):
        while len(self.work_in_progress) < number_of_workers:
            next_step = self.__next_available_step()
            if next_step:
                self.work_in_progress[next_step] = self.effort_for_step(next_step)
                self.remaining_steps.remove(next_step)
            else:
                break

    def __next_available_step(self):
        return next((step for step in self.remaining_steps if self.__is_step_ready(step)), None)

    def __is_step_ready(self, step):
        return not any([step == instruction[1] for instruction in self.remaining_instructions])

    def __finish_next_in_progress_step(self):
        next_step = min(self.work_in_progress.keys(), key=lambda key: self.work_in_progress[key])
        time_required = self.work_in_progress[next_step]
        self.work_in_progress = dict([(key, value - time_required) for key, value in self.work_in_progress.items()])
        self.elapsed_time += time_required
        self.completed_steps.append(next_step)
        del self.work_in_progress[next_step]
        self.remaining_instructions = [i for i in self.remaining_instructions if i[0] != next_step]
