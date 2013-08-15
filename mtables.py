#!/usr/bin/python
#
# mtables.py
#
# Gregory Ecker
# 8/13
#
# usage: mtables.py <lowend> <highend> <numquestions> <filename>
#  generates multiplication tables between lowend and highend in a file named "filename.txt", also generates answers in filename.answers 
#

import sys
import random

if len(sys.argv) != 5:
    print 'usage: mtables.py <lowend> <highend> <numquestions> <filename>\n'
    print 'generates multiplication tables between lowend and highend in a file named \"filename.txt\"'
    print 'also generates answers in <filename>.answers'
    sys.exit(1)

lowend = int(sys.argv[1])
highend = int(sys.argv[2])
numquestions = int(sys.argv[3])
filename = sys.argv[4]

assert lowend < highend
assert numquestions > 0

answers = []
all_questions = []

# generate all questions:

for i in range(lowend, highend+1):
    for j in range(lowend, highend+1):
        all_questions.append((i,j))

random.seed()  # seed with system time
questions = random.sample(all_questions, numquestions)
random.shuffle(questions)

for i in questions:
    answers.append(i[0]*i[1])

f = open(filename, 'w')
for i in questions:
    f.write(str(i[0]) + " * " + str(i[1]) + " = \n")
f.close() 



