n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
c=0
print(l)
for i in l:
    if i%2==0:
        i=i//2
        l.append(i)
        l.remove(2*i)
        print(l)
        c+=1
    else:
        pass
print(c)