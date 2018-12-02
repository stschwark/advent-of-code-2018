from collections import Counter
import itertools


def letters_occur_exactly(box_id, count):
    occurrences = Counter(box_id)
    return count in occurrences.values()


def checksum(box_ids):
    exactly_two = sum(letters_occur_exactly(box_id, 2) for box_id in box_ids)
    exactly_three = sum(letters_occur_exactly(box_id, 3) for box_id in box_ids)

    return exactly_two * exactly_three


def common_letters(box_id1, box_id2):
    return ''.join(c1 if c1 == c2 else '' for c1, c2 in zip(box_id1, box_id2))


def common_letters_of_two_similar_ids(box_ids):
    for id1, id2 in itertools.combinations(box_ids, 2):
        result = common_letters(id1, id2)
        if len(result) == len(id1) - 1:
            return result
