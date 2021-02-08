from util.filereader import FileReader


class QuestionGroup:
    def __init__(self, people):
        self.questions = set()

        for person in people:
            for question in list(person):
                self.questions.add(question)


class AllQuestionGroup:
    def __init__(self, people):
        self.questions = set()

        for person in people:
            for question in list(person):
                if all(question in questions for questions in people):
                    self.questions.add(question)


data_part1 = [QuestionGroup(group.split('\n')) for group in FileReader(
    path="inputs/06.txt", split=False).data.split('\n\n')]

total_part1 = 0
for qg in data_part1:
    total_part1 += len(qg.questions)

print("part1:", total_part1)

data_part2 = [AllQuestionGroup(group.split('\n')) for group in FileReader(
    path="inputs/06.txt", split=False).data.split('\n\n')]

total_part2 = 0
for qg in data_part2:
    total_part2 += len(qg.questions)

print("part2:", total_part2)
