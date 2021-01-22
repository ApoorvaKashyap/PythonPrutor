txt=str(input())
lst=txt.split(',')
count=0
for i in range(len(lst)):
	if len(lst[i]) >= 2:
		str=lst[i]
		if str[0]==str[-1]:
			count+=1
print(count)
