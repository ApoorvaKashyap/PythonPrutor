num=int(input())
numstr=str(num)
reversed=int(0)
if numstr[0]=="-":
	reversed=int("-"+numstr[-1:0:-1])
else:
	reversed=int(numstr[::-1])
print("Reverse: "+str(reversed))
sum=int(reversed)+num
print("Sum: "+str(sum))