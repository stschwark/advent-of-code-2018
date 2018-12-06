from collections import Counter


def largest_enclosed_area(coors):
    bounds = bounding_box(coors)
    areas = area_sizes(bounds, coors)
    for x in range(bounds[0][0], bounds[1][0] + 1):
        for y in range(bounds[0][1], bounds[1][1] + 1):
            if x == bounds[0][0] or y == bounds[0][1] or x == bounds[1][0] or y == bounds[1][1]:
                closest = closest_neighbour((x, y), coors)
                del areas[closest]
    return areas.most_common(1)[0][1]


def bounding_box(points):
    xs, ys = zip(*points)
    return [(min(xs), min(ys)), (max(xs), max(ys))]


def area_sizes(bounds, coors):
    result = Counter()
    for x in range(bounds[0][0], bounds[1][0] + 1):
        for y in range(bounds[0][1], bounds[1][1] + 1):
            closest = closest_neighbour((x, y), coors)
            if closest:
                result.update([closest])
    return result


def closest_neighbour(p, neighbours):
    distances = [(distance(p, neighbour), neighbour) for neighbour in neighbours]
    distances = sorted(distances, key=lambda d: d[0])
    return distances[0][1] if distances[0][0] != distances[1][0] else None


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def total_distance_to_neighbours(p, neighbours):
    return sum([distance(p, neighbour) for neighbour in neighbours])


def densest_area_size(coors, density):
    bounds = bounding_box(coors)
    area_size = 0
    for x in range(bounds[0][0], bounds[1][0] + 1):
        for y in range(bounds[0][1], bounds[1][1] + 1):
            total_distance = total_distance_to_neighbours((x, y), coors)
            if total_distance < density:
                area_size += 1
    return area_size
