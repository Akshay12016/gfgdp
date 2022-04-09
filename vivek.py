n=int(input())
l=[]
temp1=[]
for i in range(n):
    l.append(int(input()))
for i in [2,3,5,7]:
    temp=[]
    for j in l:
        if j%i==0:
            temp.append(j)
            l.remove(j)
    temp1.append(temp)
for i in temp1:
    if len(i)==0:
        temp1.remove(i)
print(temp1)
for i in temp1:
    for j in i:
        if j%6==0:
            i.remove(j)
        elif j%10==0:
            i.remove(j)
        elif j%14==0:
            i.remove(j)
        elif j%15==0:
            i.remove(j)
        elif j%35==0:
            i.remove(j)
        elif j%21==0:
            i.remove(j)
print(temp1)