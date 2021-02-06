from util.filereader import FileReader

data = FileReader('inputs/01.txt').parseInt()
found = False
for index_1, data_1 in enumerate(data):
    for index_2, data_2 in enumerate(data):
        if not found and index_1 != index_2 and data_1 + data_2 == 2020:
            print("part1: ", data_1, data_2, data_1 * data_2)
            found = True

found = False
for index_1, data_1 in enumerate(data):
    for index_2, data_2 in enumerate(data):
        for index_3, data_3 in enumerate(data):
            if not found and data_1 + data_2 + data_3 == 2020:
                found = True
                print("part2:", data_1 * data_2 * data_3)
