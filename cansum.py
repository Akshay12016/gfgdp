def cansum(target,numbers,dict={}):
    if target in dict: return dict[target]
    if target==0: return True
    if target<0: return False

    for i in numbers:
        remainder=target-i
        if cansum(remainder,numbers,dict) ==True:
            dict[target]=True
            return True

    dict[target]=False
    return False

print(cansum(300,[7,14]))