n=int(input())
t=int(input())
d=[]
for i in range(n):
    d.append(int(input()))
v=[]
for i in range(n):
    d.append(int(input()))
for i in range(t):
    for j in range(n):
        d[j]=d[j]+v[j]
print(d)