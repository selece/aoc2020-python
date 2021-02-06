import re

from util.filereader import FileReader

pattern = re.compile(
    '(?P<min>[0-9]*)-(?P<max>[0-9]*) (?P<letter>[a-z]): (?P<password>[a-z]*)')


def parse(input):
    processed = pattern.match(input)

    return {
        "min": int(processed.group('min')),
        "max": int(processed.group('max')),
        "letter": processed.group('letter'),
        "password": processed.group('password')
    }


def validate_part1(obj):
    count = len([char for char in obj["password"] if char == obj["letter"]])
    return count >= obj["min"] and count <= obj["max"]


def validate_part2(obj):
    match_min = obj["password"][obj["min"] - 1] == obj["letter"]
    match_max = obj["password"][obj["max"] - 1] == obj["letter"]

    if match_min and match_max:
        return False

    elif match_min or match_max:
        return True

    else:
        return False


valids_part1 = [line for line in FileReader(
    'inputs/02.txt').data if validate_part1(parse(line))]
print(len(valids_part1))

valids_part2 = [line for line in FileReader(
    'inputs/02.txt').data if validate_part2(parse(line))]
print(len(valids_part2))
