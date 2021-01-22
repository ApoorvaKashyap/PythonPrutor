str=input()
no=str.find('not')
bad=str.find('bad')
swap=str[no:bad+3:1]
text=str.replace(swap,'good')
if bad>no:
  print(text)
else:
  print(str)