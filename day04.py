import re

from util.filereader import FileReader


class Passport:
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields = ["cid"]

    def __init__(self, lines):
        blobs = lines.replace('\n', ' ').split(' ')
        self.data = {}
        for blob in blobs:
            parsed = blob.split(':')
            self.data[parsed[0]] = parsed[1]

        print(self.data)

    def validate_field(self, field, value):
        if field == "byr":
            return int(value) >= 1920 and int(value) <= 2002

        elif field == "iyr":
            return int(value) >= 2010 and int(value) <= 2020

        elif field == "eyr":
            return int(value) >= 2020 and int(value) <= 2030

        elif field == "hgt":
            pattern = re.compile('(?P<height>[0-9]*)(?P<height_type>[a-z]*)')
            height, height_type = pattern.match(value).groups()
            height = int(height)

            if height_type == "cm":
                return height >= 150 and height <= 193

            elif height_type == "in":
                return height >= 59 and height <= 76

            else:
                return False

        elif field == "hcl":
            pattern = re.compile('#(?P<colour>[0-9a-f]*)')
            match = pattern.match(value)

            if not match:
                return False
            else:
                colour = match.groupdict()["colour"]
                return colour and len(colour) == 6

        elif field == "ecl":
            return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        elif field == "pid":
            pattern = re.compile('(?P<id>[0-9]*)')
            match = pattern.match(value)

            if not match:
                return False
            else:
                id = match.groupdict()["id"]
                return id and len(id) == 9

        elif field == "cid":
            return True

        else:
            raise Exception(
                f'Fatal error, unrecognized field {field} with value {value}')

    def validate(self, strict=False):
        if not strict:
            if all(field in self.data for field in Passport.required_fields):
                return True

            else:
                return False

        else:
            if not all(field in self.data for field in Passport.required_fields):
                return False

            if not all(self.validate_field(field, value) for field, value in self.data.items()):
                return False

            return True


passports = [Passport(entry)
             for entry in FileReader(path='inputs/04.txt', split=False).data.split('\n\n')]

valid_1 = len([passport for passport in passports if passport.validate()])
print("part1: ", valid_1)

valid_2 = len(
    [passport for passport in passports if passport.validate(strict=True)])
print("part2:", valid_2)
