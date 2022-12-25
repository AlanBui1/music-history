from datetime import date
today = str(date.today())

def NewFile(ques, author, category, tag, ans):
    toOutput = '''---
title: '''+ques+'''
author: '''+author+'''
date: '''+today+'''
categories: ['''+category+''']
tags: ['''+tag+''']
---

## Question

''' +ques.replace(" - Answer", "")+'''

'''+ans

    return toOutput

def outToFile(fileName, toOutput):
    newFile = open(fileName, "w")
    newFile.write(toOutput)
    newFile.close()

questions = []
answers = []
authors = []
categories = []


with open('_posts/newAnswers.txt', "r") as inputFile, open('_posts/answers.txt', "w") as outFile:
    while True:
        line = inputFile.readline()
        if line == "":
            break
        outFile.write(line)
        answers.append(line.strip())
    outFile.write("\n")
        

with open('_posts/newQuestions.txt', "r") as inputFile, open('_posts/questions.txt', "w") as outFile:
    while True:
        line = inputFile.readline()
        if line == "":
            break
        outFile.write(line)
        questions.append(line.strip())
    outFile.write("\n")

with open('_posts/newAuthors.txt', "r") as inputFile:
    while True:
        line = inputFile.readline().strip()
        if line == "":
            break
        authors.append(line)

with open('_posts/newCategories.txt', "r") as inputFile:
    while True:
        line = inputFile.readline()
        if line == "":
            break
        categories.append(line.strip())

num = len(answers)

for i in range(num):
    answer1 = '''

## Answer

['''+questions[i]+'''-Answer](/music-history/posts/'''+questions[i].replace("?", "").replace(" ", "-")+'''-answer/)'''

    answer2 = '''

## Answer

'''+answers[i]

    fileName = "_posts/Questions/"+today+" "+questions[i].replace("?", "")+".md"
    fileName = fileName.replace(" ", "-")
    output1 = NewFile(questions[i], authors[i], categories[i], authors[i], answer1)
    outToFile(fileName, output1)

    fileName = "_posts/Answers/"+today+" "+questions[i].replace("?", "")+"-answer.md"
    fileName = fileName.replace(" ", "-")
    output2 = NewFile(questions[i]+" - Answer", authors[i], "Answer", authors[i], answer2)
    outToFile(fileName, output2)