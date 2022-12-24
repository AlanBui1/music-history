from datetime import date
today = str(date.today())

AnsFile = "_posts/2022-12-24-practice1.md"
questions = []
answers = []
FILENAME = today+"-sub1.md"

with open(AnsFile.replace(".md", "answers.md"), "r") as inFile:
    ind = 0
    while True:
        line = inFile.readline()
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




outFile.close()