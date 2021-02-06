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


seats = [BinarySpaceLocator(bsp_string).id()
         for bsp_string in FileReader("inputs/05.txt").data]

seats.sort()

print("part1: ", seats.pop())
