from random import shuffle
from datetime import date
today = str(date.today())

FILENAMETOOUTPUT = '_posts/practice3.md'
PAGETITLE = "Practice Exam 3 Questions"
PERMALINK = "/practice3qs/"
ANSWERKEYFILENAME = '_posts/practice3-answers.txt'

with open("questionGen/allProblems.txt") as inFile, open(FILENAMETOOUTPUT, "w") as outFile, open(ANSWERKEYFILENAME, "w") as ansFile:
    outFile.write('''---
title: '''+PAGETITLE+'''
categories: [Practice Exams]
permalink: '''+PERMALINK+'''
---

''')

    for _ in range(50):
        theme = inFile.readline()
        if theme == "":
            break

        era = inFile.readline()
        question = inFile.readline()
        possible = []
        for i in range(4):
            possible.append(inFile.readline())
        shuffle(possible)

        answer = inFile.readline()

        outFile.write(question + "\n")
        for ans in possible:
            outFile.write("- "+ans)
        outFile.write("\n")

        ansFile.write(question)
        ansFile.write(answer)