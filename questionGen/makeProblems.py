from random import randint, shuffle

class Problem:
    def __init__(self, q, a, era, categories, theme):
        self.question = q
        self.answer = a
        self.era = era
        self.categories = categories
        self.choices = set()
        self.choices.add(a)
        self.options = []
        self.theme = theme

problemsByTheme = {}
allProblems = []

with open("questionGen/questions.txt", "r") as questionFile, open("questionGen/answers.txt", "r") as answerFile, open("questionGen/era.txt", "r") as eraFile, open("questionGen/categories.txt", "r") as categoryFile, open("questionGen/themes.txt", "r") as themeFile:
    while 1:
        q = questionFile.readline()
        a = answerFile.readline()
        e = eraFile.readline()
        cats = categoryFile.readline().split()
        theme = themeFile.readline().strip()

        if q == "":
            break

        if theme not in problemsByTheme:
            problemsByTheme[theme] = []

        problemsByTheme[theme].append(Problem(q, a, e, cats, theme))
        allProblems.append(Problem(q, a, e, cats, theme))

shuffle(allProblems)

#setting random answers
with open("questionGen/allProblems.txt", "w") as outFile:
    for i in range(len(allProblems) - 1):
        while len(allProblems[i].choices) < 4:
            randNum = randint(0, len(problemsByTheme[allProblems[i].theme])-1)
            allProblems[i].choices.add(problemsByTheme[allProblems[i].theme][randNum].answer)

        for op in allProblems[i].choices:
            allProblems[i].options.append(op)

        shuffle(allProblems[i].options)

        outFile.write(allProblems[i].theme.strip() +"\n")
        outFile.write(allProblems[i].era.strip() + "\n")
        outFile.write(allProblems[i].question.strip() + "\n")
        for op in allProblems[i].options:
            outFile.write(op.strip()+"[]\n")
        outFile.write(allProblems[i].answer.strip() + "\n")