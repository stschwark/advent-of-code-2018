from collections import Counter


def letters_occur_exactly(box_id, count):
    occurrences = Counter(box_id)
    return count in occurrences.values()


def checksum(box_ids):
    exactly_two = sum(letters_occur_exactly(box_id, 2) for box_id in box_ids)
    exactly_three = sum(letters_occur_exactly(box_id, 3) for box_id in box_ids)

    return exactly_two * exactly_three


def common_letters(box_id1, box_id2):
    return ''.join(c if box_id2[i] == c else '' for i, c in enumerate(box_id1))


def common_letters_of_two_similar_ids(box_ids):
    for i, box_id in enumerate(box_ids):
        for j in range(i+1, len(box_ids) - 1):
            result = common_letters(box_id, box_ids[j])
            if len(result) == len(box_id) - 1:
                return result
