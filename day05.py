import re

from util.filereader import FileReader


class BinarySpaceLocator:
    def __init__(self, raw):
        matches = re.compile(
            '(?P<cols>[BF]*)(?P<rows>[LR]*)').match(raw).groupdict()
        self.row_steps = list(matches["cols"])
        self.col_steps = list(matches["rows"])

    @staticmethod
    def partition(l, mode):
        mid_index = len(l) // 2
        lower = l[:mid_index]
        upper = l[mid_index:]

        if mode == 'F' or mode == 'L':
            return lower

        elif mode == 'B' or mode == 'R':
            return upper

    def locate(self):
        # rows first, 0 - 127
        row_location = list(range(128))
        for row_step in self.row_steps:
            row_location = BinarySpaceLocator.partition(
                row_location, row_step)

        # cols next, 0 - 7
        col_location = list(range(8))
        for col_step in self.col_steps:
            col_location = BinarySpaceLocator.partition(
                col_location, col_step)

        return row_location.pop(), col_location.pop()

    def id(self):
        row, col = self.locate()
        return row * 8 + col


seats_part1 = [BinarySpaceLocator(bsp_string).id()
               for bsp_string in FileReader("inputs/05.txt").data]

seats_part1.sort()

print("part1: ", seats_part1[-1])

seats_part2 = [BinarySpaceLocator(bsp_string).locate()
               for bsp_string in FileReader("inputs/05.txt").data]


def trim_seats(seat):
    row, _ = seat
    return not row == 9 and not row == 119


seats_part2.sort()
seats_part2 = list(filter(trim_seats, seats_part2))


def seat_walk(seat):
    _, col = seat
    next_row, next_col = seat

    if col == 7:
        next_col = 0
        next_row += 1

    else:
        next_col += 1

    return (next_row, next_col)


for index, seat in enumerate(seats_part2):
    if seat_walk(seat) != seats_part2[index + 1]:
        print(f'empty seat between {seat} and {seats_part2[index+1]}')
        break
