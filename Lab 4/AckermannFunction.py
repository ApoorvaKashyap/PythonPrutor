def ackermann(m,n):
	if m == 0:
		return n+1
	if n == 0:
		return ackermann(m-1, 1)
	return ackermann(m-1, ackermann(m, n-1))

data = str(input())
numList = data.split(',')
m = int(numList[0].strip())
n = int(numList[1].strip())
result = ackermann(m,n)
print(result)