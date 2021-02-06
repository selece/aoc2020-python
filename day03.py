from util.filereader import FileReader


class Slope:
    tree = '#'
    empty = '.'

    def __init__(self, lines):
        self.lines = lines
        self.x = 0
        self.y = 0
        self.hits = 0
        self.line_length = len(lines[0])

    def traverse_to_bottom(self, delta_x, delta_y):
        while not self.traverse(delta_x, delta_y):
            pass

        return self.hits

    def traverse(self, delta_x, delta_y):
        # if we're past the bottom of the slope, then end
        if self.y >= len(self.lines) or self.y + delta_y >= len(self.lines):
            return True

        else:
            # always descend
            self.y += delta_y

            # check x bounds
            if self.x + delta_x >= self.line_length:
                self.x = (self.x + delta_x) - (self.line_length)

            else:
                self.x += delta_x

            # check tree bonk
            current = self.lines[self.y][self.x]

            if current == Slope.tree:
                self.hits += 1
            elif current != Slope.empty:
                raise Exception(f'Invalid input: {current}')
            else:
                pass

            return False


data = [line.strip() for line in FileReader('inputs/03.txt').data]
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
traversals = [Slope(data).traverse_to_bottom(slope[0], slope[1])
              for slope in slopes]

result = 1
for res in traversals:
    result *= res

print(traversals, result)
