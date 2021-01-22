num=int(input())
r=[]
s=[]
m=[]
report=[]

for i in range(1,num+1):
    temp=0
    z=str(input())
    k=z.replace(' ','',)
    d=k.split(',',)
    if d[0]+' # '+d[1] in s:
        q=s.index(d[0]+' # '+d[1])
        temp=int(m[q])+int(d[2])
        m[q]=temp
    else:
         s.append(d[0]+' # '+d[1])
         m.append(d[2])
x=0
while x<len(s):
    f=s[x]+' # '+str(m[x])
    report.append(f)
    report.sort()
    x=x+1
h=0    
while h<len(report):
    print(report[h])
    h=h+1