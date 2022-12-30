from random import shuffle
from datetime import date
today = str(date.today())

FILENAMETOOUTPUT = '_posts/practice2.md'
PAGETITLE = "Practice Exam 2 Questions"
PERMALINK = "/practice2qs/"
ANSWERKEYFILENAME = '_posts/practice2-answers.txt'

with open("questionGen/allProblems.txt") as inFile, open(FILENAMETOOUTPUT, "w") as outFile, open(ANSWERKEYFILENAME, "w") as ansFile:
    outFile.write('''---
title: '''+PAGETITLE+'''
categories: [Practice Exams]
permalink: '''+PERMALINK+'''
---

''')

    while True:
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