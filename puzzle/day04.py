import re
from datetime import datetime
from pandas import DataFrame


class Observation:
    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message

    def datetime(self):
        return datetime.strptime(self.timestamp, '%Y-%m-%d %H:%M')


def observations(input):
    p = re.compile(r'\[(?P<timestamp>.+)\] (?P<message>.+)')

    result = list()
    for line in input:
        m = p.match(line)
        result.append(Observation(m.group('timestamp'), m.group('message')))

    return result


def guard_pattern(observed):
    begins_shift = re.compile(r'Guard #(?P<guard>\d+) begins shift')
    data = list()
    guard = None
    asleep_from = None

    for observation in observed:
        m = begins_shift.match(observation.message)
        if m:
            guard = int(m.group('guard'))
        elif 'falls asleep' in observation.message:
            asleep_from = observation.datetime().minute
        elif 'wakes up' in observation.message:
            asleep_to = observation.datetime().minute - 1
            for minute in range(asleep_from, asleep_to + 1):
                data.append({'guard': guard, 'minute': minute})

    return DataFrame(data)


def strategy1(pattern):
    sleepy_guard = pattern\
        .groupby('guard')\
        .size().to_frame('count').reset_index()\
        .sort_values(by='count', ascending=False)\
        .iloc[0]['guard']

    sleepy_minute = pattern[pattern.guard == sleepy_guard]\
        .groupby('minute')\
        .size().to_frame('count').reset_index()\
        .sort_values(by='count', ascending=False)\
        .iloc[0]['minute']

    return sleepy_guard * sleepy_minute


def strategy2(pattern):
    sleepy_minute = pattern \
        .groupby('minute') \
        .size().to_frame('count').reset_index() \
        .sort_values(by='count', ascending=False) \
        .iloc[0]['minute']

    sleepy_guard = pattern[pattern.minute == sleepy_minute] \
        .groupby('guard') \
        .size().to_frame('count').reset_index() \
        .sort_values(by='count', ascending=False) \
        .iloc[0]['guard']

    return sleepy_guard * sleepy_minute
