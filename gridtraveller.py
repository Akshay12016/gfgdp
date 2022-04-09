def gridTraveller(m,n,dict={}):
    key=str(m)+','+str(n)
    if key in dict: return dict[key]
    if m==1 and n==1: return 1
    if m==0 or n==0: return 0
    dict[key]=gridTraveller(m-1,n,dict)+gridTraveller(m,n-1,dict)
    return dict[key]

print(gridTraveller(18,18))