import re
from itertools import chain, product
from collections import Counter


class Claim:
    def __init__(self, id, x, y, width, height):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def area(self):
        return frozenset(product(range(self.x, self.x + self.width), range(self.y, self.y + self.height)))


def claim_from_string(s):
    id, x, y, w, h = re.findall(r'\d+', s)
    return Claim(int(id), int(x), int(y), int(w), int(h))


def __overlap_counter(claims):
    areas = list(c.area() for c in claims)
    return Counter(chain.from_iterable(areas))


def locations_with_overlap(claims):
    overlap_counter = __overlap_counter(claims)
    return sum(1 if overlap_counter[position] > 1 else 0 for position in overlap_counter)


def first_claim_without_overlap(claims):
    overlap_counter = __overlap_counter(claims)
    locations_with_one_claim = set(location for location in overlap_counter if overlap_counter[location] == 1)

    for claim in claims:
        if claim.area() < locations_with_one_claim:
            return claim




