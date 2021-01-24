'''def read_int():
    try:
        x = input()
        x = int(x)
    except Exception as e:
        print('Bad Input {}.'.format(x))
        print('Try Again.')
        x = read_int()
        return x
    else:
        return x'''

## Code to read __VendingItems__.csv
vendingItems = open('__VendingItems__.csv', 'r')
for i in vendingItems:
print(i)
## Code to read user inputs
## Enforce the constraints using Exception Handling


## Act once the inputs are OK.