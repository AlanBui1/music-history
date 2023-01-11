from datetime import date
today = str(date.today())
username = "Alan"

AnsFile = "_posts\practice2-answers.txt" #answer key
questions = []
answers = []
FILENAME = "_posts/"+today+"-sub1.md" #output file

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
ans = "Organum[]	Chanson[]	Concerto grosso[]	Water Music: Suite in D major, HWV 349[]	Sonata Cycle[]	suite[]	Symphony No.104 in D Major(“London”)[]	suite[]	Piano Concerto in G Major, K453[]	Piano Sonata in C Minor, op.13[]	A capella[]	The Carman’s Whistle[]	Franz Joseph Haydn[]	Thomas Morley[]	Giovanni Pierluigi da Palestrina[]	Franz Joseph Haydn[]	Mozart[]	Jean-Philippe Rameau[]	Josquin des Prez[]	George Frederic Handel[]	Guillaume de Machaut[]	Claudio Monteverdi[]	Giovanni Pierluigi da Palestrina[]	L’Orfeo[]	Organum[]	Chanson[]	Sonata Cycle[]	Henry Purcell[]	Franz Joseph Haydn[]	Haec dies (chant)[]	Symphony[]	My Bonny Lass She Smileth[]	Johann Sebastian Bach[]	O mitissima/Virgo/Haec dies[]	Estampie[]	A capella[]	String Quartet in C sharp Minor, op.131[]	Estampie[]	Symphony[]	Johann Sebastian Bach[]	William Byrd[]	La poule from Nouvelle suites de pieces de clavecin[]	Concerto grosso[]	Gloria from Missa Papae Marcelli[]	Carlo Gesualdo[]	Guillanme de Machaut[]	Dido ans Aeneas[]	The Creation[]	Mozart[]"
ans = ans.replace('”', '"').replace('“', '"').replace('’', "'")
allAns = ans.split("[]")
for i in range(len(allAns)):
    allAns[i] = allAns[i].strip()

outFile = open(FILENAME, "w")

outFile.write('''---
title: Practice Exam 2 Sub 1
categories: [Practice Exams]
permalink: /practice2/sub1/
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