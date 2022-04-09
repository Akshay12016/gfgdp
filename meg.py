class Solution:
 def countSubstrings(self, s: str) -> int:
    n = len(s)
    c=0
    for i in range(0,n-1): #i=0
        for j in range(i+1,n+1): #j=1
            temp = s[i:j]
            if len(temp) == 1:
                c+=1
            # if the len of substring is even,
            # check if the reverse of the string is same as the string
            elif(len(temp)%2 == 0):
                if (temp == temp[::-1]):
                    c+=1
            else:
                # create a dict to check how many times
                # each value has occurred
                d = {}
                for l in range(len(temp)):
                    if temp[l] in d:
                        d[temp[l]] = d[temp[l]]+1
                    else:
                        d[temp[l]] = 1

    return c


op = Solution()
print(op.countSubstrings('abaca'))