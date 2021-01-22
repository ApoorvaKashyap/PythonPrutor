n = int(input())
m = int(input())
edge = {}

for i in range(n):
    edge[i] = set()

for i in range(m):
    nodes = input().split(',')
    first = int(nodes[0])
    second = int(nodes[1])
    edge[first].add(second)
    edge[second].add(first)
A = int(input())
if A in range(n):
    result = ""
    for i in edge[A]:
        result += str(i) + ','

    print(result[ :-1])    
else :
    print("ERROR: Invalid Node.")