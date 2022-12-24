from random import randint, shuffle
from datetime import date
today = str(date.today())

questions = []
answers = []

with open('_posts/questions.txt', "r") as inputFile:
    while True:
        line = inputFile.readline()
        if line == "":
            break
        questions.append(line.strip())

with open('_posts/answers.txt', "r") as inputFile:
    while True:
        line = inputFile.readline()
        if line == "":
            break
        answers.append(line.strip())

NUMQUESTIONS = 4

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
    qanda.write(questions[i]+"\n")
    qanda.write(answers[i]+"\n")

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
        outFile.write("- "+op+"\n")

    outFile.write("\n")

outFile.close()
qanda.close()