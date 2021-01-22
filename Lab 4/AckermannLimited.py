count = 0

def ackermann(m,n,T):
	global count
	if count <= T:
		count +=1
		if m == 0:
			return n+1
		if n == 0:
			return ackermann(m-1, 1,T)
		return ackermann(m-1, ackermann(m, n-1, T), T)
	else:
		print('Aborted')
		exit()

data = str(input())
numList = data.split(',')
m = int(numList[0].strip())
n = int(numList[1].strip())
T =  int(numList[2].strip())
result = ackermann(m,n,T)
print('Result = {} in {} calls'.format(result, count))