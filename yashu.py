def getflip(st):
    count=0
    for i in range(len(st)):
        if st[i]=='0':
            count+=1
            for j in range(i,len(st)):
                if st[j] == '0': 
                    st = st[:j] + '1' + st[j+1:]
                else: 
                    st = st[:j] + '0' + st[j+1:]
    return count
st=input()
print(getflip(st))