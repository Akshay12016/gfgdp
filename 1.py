import math
m = int(input())

typelst = []
for i in range(m): typelst.append(int(input()))
timelst = []
for i in range(m): timelst.append(int(input()))

lst1 = []
lst2 = []
lst3 = []

for i in range(m):
        if typelst[i] == 1:
            lst1.append(timelst[i])
        elif typelst[i] == 2:
            lst2.append(timelst[i])
        elif typelst[i] == 3:
            lst3.append(timelst[i])

lst1.sort()
lst2.sort()
lst3.sort()
    
for i in range(1,len(lst1)):
        lst1[i] += lst1[i-1]
    
for i in range(1,len(lst2)):
        lst2[i] += lst2[i-1]

for i in range(1,len(lst3)):
        lst3[i] += lst3[i-1]

ans = math.inf
    
try:
        ans = lst1[m-1] + lst2[m-1]
except:
        pass

   

for i in range(m):

        if i < len(lst3):
            if i==m-1:
                try:
                    val = lst3[i]
                    if val < ans: ans = val
                except: 
                    pass
            try:
                indx = m-i-2
                val = lst3[i] + lst2[indx] + lst1[indx]
                if val < ans: ans = val  
            except:
                pass
    
if ans==math.inf:
        print(-1)
else:
        print(ans)