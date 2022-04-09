n=int(input())
l=[]
temp1=[]
for i in range(n):
    l.append(int(input()))
temp2=[]
temp3=[]
temp5=[]
temp7=[]
prime=[]
for j in l:
    if j%2==0 and (j%3!=0 and j%5!=0 and j%7!=0):
        temp2.append(j)
    elif j%3==0 and (j%5!=0 and j%7!=0):
        temp3.append(j)
    elif j%5==0 and (j%7!=0):
        temp5.append(j)
    elif j%7==0:
        temp7.append(j)
    else:
        prime.append(j)
temp1.append(temp2)
temp1.append(temp3)
temp1.append(temp5)
temp1.append(temp7)
temp1.append(prime)
c=0
for i in temp1:
    if len(i)!=0:
        c+=1
#print(temp1)
print(c+len(prime))
        
