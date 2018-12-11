class Grid:
    def __init__(self, serial, size=300):
        self.serial = serial
        self.size = size
        self.summed_area = None

    def largest_total_power_area(self, size=3):
        largest_power_area = (1, 1)
        largest_power_level = 0
        for y in range(1, self.size - size + 2):
            for x in range(1, self.size - size + 2):
                power_level = self.power_level_for_area(x, y, x + size - 1, y + size - 1)
                if power_level > largest_power_level:
                    largest_power_level = power_level
                    largest_power_area = (x, y)

        return largest_power_area

    def largest_total_power_area_of_any_size(self):
        largest_power_area = (1, 1)
        largest_power_level = 0
        largest_power_area_size = 0
        for size in range(1, 301):
            area = self.largest_total_power_area(size)
            power_level = self.power_level_for_area(area[0], area[1], area[0] + size - 1, area[1] + size - 1)
            if power_level > largest_power_level:
                largest_power_level = power_level
                largest_power_area = area
                largest_power_area_size = size

        return (*largest_power_area, largest_power_area_size)

    def power_level_for_area(self, x1, y1, x2, y2):
        if not self.summed_area:
            self.summed_area = self.summed_area_table()
        return self.summed_area.get((x2, y2), 0) \
            + self.summed_area.get((x1 - 1, y1 - 1), 0) \
            - self.summed_area.get((x2, y1 - 1), 0) \
            - self.summed_area.get((x1 - 1, y2), 0)

    def summed_area_table(self):
        summed_areas = dict()
        for y in range(1, self.size + 1):
            sum_to_left = 0
            for x in range(1, self.size + 1):
                sum_to_left += self.power_level(x, y)
                sum_above = summed_areas.get((x, y - 1), 0)
                summed_areas[(x, y)] = sum_to_left + sum_above
        return summed_areas

    def power_level(self, x, y):
        rack_id = x + 10
        return (rack_id * y + self.serial) * rack_id // 100 % 10 - 5
