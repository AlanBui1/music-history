from random import randint, shuffle

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

outFile = open("_posts/practice1.md", "w")

for i in range(NUMQUESTIONS):
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