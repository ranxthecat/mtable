#!/usr/bin/python
#
# mtables.py
#
# Gregory Ecker
# 8/13
#
# usage: mtables.py <lowend> <highend> <numquestions> <filename> <<musthave1>> <<musthave2>>
#  generates multiplication tables between lowend and highend in a file named "filename.txt", also generates answers in filename.answers 
# optional parameters <<musthave1>> .. <<musthaven>> indicate numbers which must be present in questions
#

import sys
import random

if len(sys.argv) < 5:
    print 'usage: mtables.py <lowend> <highend> <numquestions> <filename> <<musthave1..musthaveN>>\n'
    print 'generates multiplication tables between lowend and highend in a file named \"filename.txt\"'
    print 'also generates answers in <filename>.answers'
    print ' optional parameters <<musthave1>> .. <<musthaven>> indicate numbers which must be present in questions'
    sys.exit(1)

lowend = int(sys.argv[1])
highend = int(sys.argv[2])
numquestions = int(sys.argv[3])
filename = sys.argv[4]
musthaves = []   # list of numbers which must be present in question set (optional) 
if len(sys.argv) > 5:
    for i in range(5, len(sys.argv)):
        musthaves.append(int(sys.argv[i]))
    print "musthaves: " + str(musthaves)

assert lowend < highend
assert numquestions > 0

answers = []
all_questions = []

# generate all questions:

for i in range(lowend, highend+1):
    for j in range(lowend, highend+1):
        all_questions.append((i,j))

random.seed()  # seed with system time

if len(musthaves) > 0:
    tmpquestions = []
    for i in all_questions:
        if (i[0] in musthaves) or (i[1] in musthaves) :
            tmpquestions.append(i)
    random.shuffle(tmpquestions)
    # dbg print " tmpquestions : " + str(tmpquestions)
    all_questions = tmpquestions

if numquestions > len(all_questions):
    print  "Sample Greater than population : " + str(len(all_questions))
    sys.exit(1)

print "num possible questions: " + str(len(all_questions))
questions = random.sample(all_questions, numquestions)
random.shuffle(questions)
    
for i in questions:
    answers.append(i[0]*i[1])

f = open(filename, 'w')
for i in questions:
    f.write(str(i[0]) + " * " + str(i[1]) + " = \n")
f.close() 



