from random import randint, shuffle
from datetime import date
today = str(date.today())

questions = []
answers = []
allLines = []

with open('_posts/questions.txt', "r") as QUESTIONS, open('_posts/answers.txt', "r") as ANSWERS:
    while True:
        line1 = QUESTIONS.readline()
        line2 = ANSWERS.readline()
        if line1 == "":
            break
        allLines.append([line1, line2])

shuffle(allLines)

for q, a in allLines:
    questions.append(q)
    answers.append(a)

NUMQUESTIONS = 20

outFile = open("_posts/"+today+"-practice1.md", "w")
qanda = open("_posts/"+today+"-practice1answers.md", "w")

outFile.write('''---
title: Practice Exam 1 Raw Questions
categories: [Practice Exams]
permalink: /practice1qs/
---

'''
)

for i in range(NUMQUESTIONS):
    qanda.write(questions[i])
    qanda.write(answers[i])

    outFile.write(questions[i] +"\n\n")

    #generate options
    options = set()
    options.add(answers[i])

    while len(options) < 4:
        randNum = randint(0, len(answers)-1)
        options.add(answers[randNum])

    opList = []
    for i in options:
        opList.append(i)
    shuffle(opList)

    for op in opList:
        outFile.write("- "+op.strip()+"[]\n")

    outFile.write("\n")

outFile.close()
qanda.close()