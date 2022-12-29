from random import randint, shuffle
from datetime import date
today = str(date.today())

questions = []
answers = []
allLines = []
categories = []
answersByCategory = {}

with open('_posts/questions.txt', "r") as QUESTIONS, open('_posts/answers.txt', "r") as ANSWERS, open('_posts/newCategories.txt', "r") as CATS:
    while True:
        line1 = QUESTIONS.readline()
        line2 = ANSWERS.readline()
        line3 = CATS.readline().strip()
        if line1 == "":
            break
        allLines.append([line1, line2, line3])

shuffle(allLines)

for q, a, c in allLines:
    questions.append(q)
    answers.append(a)
    categories.append(c)
    if c not in answersByCategory:
        answersByCategory[c] = []
    answersByCategory[c].append(a)

NUMQUESTIONS = 40

outFile = open("_posts/"+today+"-practice2.md", "w")
qanda = open("_posts/"+today+"-practice2answers.md", "w")

outFile.write('''---
title: Practice Exam 2 Raw Questions
categories: [Practice Exams]
permalink: /practice2qs/
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
        randNum = randint(0, len(answersByCategory[categories[i]])-1)
  
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