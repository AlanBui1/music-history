from datetime import date
today = str(date.today())
username = "Alan"

AnsFile = "_posts/2022-12-24-practice1.md"
questions = []
answers = []
FILENAME = "_posts/"+today+"-sub1.md"

with open(AnsFile.replace(".md", "answers.md"), "r") as inFile:
    ind = 0
    while True:
        line = inFile.readline().strip()
        if line == "":
            break
    
        if ind:
            answers.append(line)
        else:
            questions.append(line)
        ind ^= 1

ans = "Multiple texts sungs at the same time[]	Single line of melody[]	Syllables that make no sense[]	2 or more melodic lines at the same time[]"	
allAns = ans.split("[]")
for i in range(len(allAns)):
    allAns[i] = allAns[i].strip()

outFile = open(FILENAME, "w")

outFile.write('''---
title: Practice Exam 1 Sub 1
categories: [Practice Exams]
permalink: /practice1/sub1/
---

### Date: '''+today+'''

### Submitted by: '''+username+'''

## Submission:

| Question | Your Answer | Score | Intended Answer |
| :---        |    :----:   |  :----: |        ---: |
'''
) 

wrong = []
correct = 0
for i in range(len(questions)):
    score = "0/1"
    if allAns[i].strip() == answers[i].strip():
        score = "1/1"
        correct += 1
    else:
        wrong.append(questions[i])
    outFile.write("| "+questions[i]+" | "+allAns[i] + " | " + score + " | " + answers[i] + " |\n")

outFile.write('''

## Final Score: '''+str(correct)+"/"+str(len(questions)) +'''

'''
)

outFile.close()