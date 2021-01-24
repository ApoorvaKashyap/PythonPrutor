def read_int():
    try:
        x = input()
        x = int(x)
    except Exception as e:
        print('Bad Input {}.'.format(x))
        print('Try Again.')
        x = read_int()
        return x
    else:
        return x

## Code to read __VendingItems__.csv
def readItems():
  temp = []
  itemsList = {}
  
  with open('./Lab 5/__VendingItems__.csv', 'r') as vendingItems:
    for i in vendingItems:
      temp.append(i)

  i=int(0)
  while i < len(temp):
    atemp = temp[i].split('|')
    btemp = atemp[1].split(',')
    itemsList[atemp[0].strip()] = int(btemp[0].strip())
    i+=2

  return itemsList

## Code to read user inputs
## Enforce the constraints using Exception Handling
def inputItem(itemsList):
  lst=[]
  for i in itemsList:
    lst.append(i)
  
  try:
    item = str(input())
    if not(item in itemsList):
      raise Exception 
  except Exception as e:
    print('Available Items are %s.\nTry Again.'%lst)
    item = inputItem(itemsList)
    return item
  else:
    return item

## Act once the inputs are OK.
itemsList = readItems()
item = inputItem(itemsList)
money = read_int()

if money < int(itemsList[item]):
  print('Sorry, can not buy item. Not enough money')
elif money == int(itemsList[item]):
  print('Thank you for your purchase. Enjoy')
else:
  print('Thank you for your purchase. Enjoy')
  print('Do not forget to collect your change,{} Rs.'.format(money - itemsList[item]))