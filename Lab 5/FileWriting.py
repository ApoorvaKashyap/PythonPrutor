#######################################

# Do Not Change

roll = input()
fileA = roll + 'A.txt'
fileB = roll + 'B.txt'
########################################


########################################
# Your code goes here
inputA = eval(input())
inputB = eval(input())

A, B = open('./Lab 5/'+fileA, 'w'), open('./Lab 5/'+fileB, 'w')

for i in range(len(inputA)):
  A.write(str(inputA[i])+'\n')
  B.write(str(inputB[i])+'\n')

########################################


########################################
# Do Not Change
A, B = open('./Lab 5/'+fileA, 'r'), open('./Lab 5/'+fileB, 'r')
print (A.read())
print (B.read())
A.close()
B.close()
########################################