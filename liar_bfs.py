#!/usr/bin/python
import Queue
import sys
f=open(sys.argv[1])
dic={}
l=f.readline()
n=int(l)
while n>0:
    n=n-1
    l=f.readline()
    name,n2=l.split()
    if name not in dic:
        dic[name]=[]
    n2=int(n2)
    while n2>0:
        n2=n2-1
        l=f.readline().rstrip()
        if l in dic.keys():
            if name in dic[l]:
                pass
            else:
                dic[l].append(name)
        else:
            dic[l]=[]
            dic[l].append(name)
        if l not in dic[name]:
            dic[name].append(l)
q=Queue.Queue()
lis,color=[],{}
for x in dic.keys():
    color[x]=0
color[name]=2
q.put((name,0))
lis.append((name,0))
while q.empty()!=True:
    temp=q.get()
    i=(temp[1] +1 )%2
    for x in dic[temp[0]]:
        if color[x]==0:
            q.put((x,i))
            lis.append((x,i))
            color[x]=1
n0,n1=0,0
for x in lis:
    if x[1]==1:
        n0+=1
    else:
        n1+=1
print max(n0,n1),min(n1,n0)

