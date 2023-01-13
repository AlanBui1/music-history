from datetime import date
today = str(date.today())
username = "Alan"

AnsFile = "_posts/practice3-answers.txt" #answer key
questions = []
answers = []
FILENAME = "_posts/"+today+"-sub2.md" #output file

with open(AnsFile, "r") as inFile: #load answers
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

#user answers
ans = "La poule from Nouvelle suites de pieces de clavecin[]	Secular[]	Sacred[]	Mozart[]	Guillaume de Machaut[]	Water Music: Suite in D major, HWV 349[]	My Bonny Lass She Smileth[]	Sonata Cycle[]	Symphony[]	Mozart[]	Sonata Cycle[]	Many notes per syllable of text with melismas[]	String quartet[]	Johann Sebastian Bach[]	La poule from Nouvelle suites de pieces de clavecin[]	William Byrd[]	Secular[]	Sacred[]	Beethoven[]	Guillanme de Machaut[]	Franz Joseph Haydn[]	Single line of melody[]	Johann Sebastian Bach[]	Giovanni Pierluigi da Palestrina[]	Sacred[]	Guillaume de Machaut[]	Beethoven[]	Organum[]	Chanson[]	The Creation[]	Secular[]	Multiple texts sungs at the same time[]	Secular[]	suite[]	Symphony No.104 in D Major(“London”)[]	Secular[]	Carlo Gesualdo[]	Chamber music[]	A capella[]	Haydn[]	Gloria from Missa Papae Marcelli[]	Beethoven[]	Sacred[]	Carl Philip Emmanuel Bach[]	Cant tell[]	One note per syllable of text[]	The Creation[]	Mozart[]	Claudio Monteverdi[]	Secular[]"
ans = ans.replace('”', '"').replace('“', '"').replace('’', "'")
allAns = ans.split("[]")
for i in range(len(allAns)):
    allAns[i] = allAns[i].strip()

outFile = open(FILENAME, "w")

outFile.write('''---
title: Practice Exam 3 Sub 2
categories: [Practice Exams]
permalink: /practice3/sub2/
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