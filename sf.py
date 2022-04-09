k=int(input())
for i in range(k):
    m,n=map(int,input().split())
    temp=[]
    for i in range(m):
        temp1=[]
        temp1=list(map(int,input().split()))
        temp.append(temp1)
    final = []
    for i in range(m):
        temp2=[]
        peru = []
        for j in range(n):
            sum = 0
            
            if i==0:
                if j==0:
                    x,y=0,0
                    try:
                        x= temp[i+1][j]
                    except:
                        pass
                    try:
                        y = temp[i][j+1]
                    except:
                        pass
                    sum = x+y
                    
                    # sum = temp[i+1][j] + temp[i][j+1]
                elif j==n-1:
                    x,y=0,0
                    try:
                        x= temp[i][j-1]
                    except:
                        pass
                    try:
                        y = temp[i+1][j]
                    except:
                        pass
                    sum = x+y
                    # sum= temp[i][j-1] +temp[i+1][j]
                else:
                    sum=temp[i][j-1]+temp[i][j+1]+temp[i+1][j]
            elif i==m-1:
                if j==0:
                    x,y=0,0
                    try:
                        x= temp[i-1][j]
                    except:
                        pass
                    try:
                        y = temp[i][j+1]
                    except:
                        pass
                    sum = x+y
                    #sum = temp[i-1][j] + temp[i][j+1]
                elif j==n-1:
                    sum= temp[i][j-1] +temp[i-1][j]
                else:
                    sum=temp[i][j-1]+temp[i][j+1]+temp[i-1][j]
            else:
                print(i)
                if j==0:
                    x,y=0,0
                    try:
                        x= temp[i][j+1]
                    except:
                        pass
                    sum=x+temp[i+1][j]+temp[i-1][j]
                elif j==n-1:
                    sum=temp[i][j-1]+temp[i+1][j]+temp[i-1][j]
                else:
                    sum = temp[i+1][j] + temp[i][j+1] + temp[i-1][j] +temp[i][j-1]
            peru.append(sum)
        final.append(peru)
    for i in range(m):
        for j in range(n):
            print(final[i][j],end=' ')
        print()
