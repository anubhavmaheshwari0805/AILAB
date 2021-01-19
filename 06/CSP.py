#!/usr/bin/env python

def backtrack(x, enemy, domain, assigned) :
    if -1 not in assigned :
        return x
    v=999
    for i in range(len(domain)) :
        if v>len(domain[i]) and assigned[i]!=1 :
            v=i
    order=[]
    for i in domain[v] :
        mini=1000
        for j in enemy[v] :
            temp=len(domain[j])
            if i in domain[j] :
                temp-=1
            if mini>temp :
                mini=temp
        order.append((i,mini))
    order=sorted(order,key=lambda x:x[1], reverse=True)
    ordered=[i[0] for i in order]
    for i in ordered :
        newdomain=[[j for j in i] for i in domain]
        x[v]=i
        assigned[v]=1
        newdomain[v]=[k for k in newdomain[v] if k==i]
        temp=[]
        for j in range(len(newdomain)) :
            if j!=v and j in enemy[v] :
                newdomain[j]=[k for k in newdomain[j] if k!=i]
        res=backtrack(x, enemy, newdomain, assigned)
        if res!=0:
            return res
    x[v]=""
    assigned[v]=-1
    return 0

n=8 #input("Enter the number of people : ")
c=3 #input("Enter the number of tables : ")
#l=[]
#line=input("Enter elements of list L(people who should not sit together) till an empty newline character :\n").split()
#while(line) :
#    l.append((int(line[0]),int(line[1])))
#    line=input().split()
l=[(0,2),(0,3),(0,4),(1,4),(1,7),(2,3),(2,6),(3,4),(3,7),(4,7),(5,6)]
enemy=[[] for i in range(n)]
for i in l :
    enemy[i[0]].append(i[1])
    enemy[i[1]].append(i[0])
x=["" for i in range(n)]
assigned=[-1 for i in range(n)]
domain=[[x for x in range(c)] for i in range(n)]
res=backtrack(x, enemy, domain, assigned)
if res==0 :
    print('False')
else:
    for i in range(len(res)) :
        print(i,' : ',res[i])
