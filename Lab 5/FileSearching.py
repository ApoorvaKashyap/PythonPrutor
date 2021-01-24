#######################################
## Do not Change
roll = input()
fileA = roll + 'A.txt'
fileB = roll + 'B.txt'
########################################
# Your code goes here

def check(file, txt):
  with open(file, 'r') as f:
    for line in f:
      if txt in line:
        return True
      else:
        return False

txt = input()

if check(fileA, txt) and check(fileB, txt):
  print('Item {} found in both {} and {}'.format(txt,fileA,fileB))
elif check(fileA,txt):
  print('Item {} found in {}'.format(txt,fileA))
elif check(fileB,txt):
  print('Item {} found in {}'.format(txt,fileB))
else:
  print('Item {} found nowhere'.format(txt))