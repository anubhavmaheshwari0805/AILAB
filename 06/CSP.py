#!/usr/bin/env python

def backtrack(soln, assigned, domain, enemy_list) :
    if -1 not in assigned :
        return soln
    v=1000
    w=0
    for i in range(len(domain)) :
        if len(domain[i])<v and assigned[i]==-1 :
            v=len(domain[i])
            w=i
    affected=[]
    for i in domain[w] :
        soln[w]=i
        assigned[w]=1
        for e in enemy_list[w] :
            if i in domain[e] :
                domain[e].remove(i)
                affected.append(e)
        res=backtrack(soln, assigned, domain, enemy_list)
        if res!=0 :
            return res
        for a in afected :
            domain[a].append(i)
        affected=[]
    return 0

people=8#int(input("Enter no. of peoples : "))
tables=3#int(input("Enter no. of tables : "))
constraints=[]
#list=input("Enter the pair of peoples who can't sit together : ").split()
#while list :
#    constraints.append((int(list[0]),int(list[1])))
#    list=input().split()
constraints=[(0,2),(0,3),(0,4),(1,4),(1,7),(2,3),(2,6),(3,4),(3,7),(4,7),(5,6)]
assigned=[-1 for i in range(people)]
domain=[[x for x in range(tables)] for i in range(people)]
soln=["" for i in range(people)]
enemy_list=[[] for i in range(people)]
for i in constraints :
    enemy_list[i[0]].append(i[1])
    enemy_list[i[1]].append(i[0])

res=backtrack(soln,assigned,domain,enemy_list)
if res==0 :
    print("No solution")
else :
    print(res)