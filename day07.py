import re

from util.filereader import FileReader


class BaggageRule:
    full_pattern = re.compile(
        '(?P<bag_type>.*) (?:bag|bags) contain (?P<contents>.*).')
    contents_pattern = re.compile(
        '(?P<bag_count>[0-9]*) (?P<bag_type>.*) (?:bag|bags)')

    def __init__(self, raw):
        bag_type, contents = BaggageRule.full_pattern.match(raw).groups()
        self.bag_type = bag_type
        self.contents = dict()

        for contained in contents.split(','):
            contents_matches = BaggageRule.contents_pattern.match(
                contained.strip())

            contained_bag_count, contained_bag_type = contents_matches.groups(
            ) if contents_matches else (None, None)

            if contained_bag_count and contained_bag_type:
                self.contents[contained_bag_type] = int(contained_bag_count)


class BaggageNetwork:
    def __init__(self, rules):
        self.network = dict()

        for rule in rules:
            self.network[rule.bag_type] = []

            for contained_bag in rule.contents.keys():
                self.network[rule.bag_type].append(contained_bag)

    def contains(self, search_for):
        results = set()

        for colour, contents in self.network.items():
            if search_for in contents:
                results.add(colour)

        return list(results)

    def recurse_upwards(self, starting_node, gen=0):
        parents = self.contains(starting_node)

        if len(parents) == 0:
            return [starting_node]

        else:
            appended_results = [starting_node] if gen > 0 else []
            for node in parents:
                appended_results += self.recurse_upwards(node, gen + 1)

            return appended_results


baggage_rules = [BaggageRule(raw)
                 for raw in FileReader(path="inputs/07.txt", split=True).data]

baggage_network = BaggageNetwork(baggage_rules)
gold_containers = set(baggage_network.recurse_upwards('shiny gold'))
print("part 1: ", len(gold_containers))
