import random
def ex(w,b):
    #make a list with 10 "w"'s and 10 "b"'s
    balls = ['w']*w + ['b']*b
    #pop three random elements from the list
    a = balls.pop(random.randint(0, len(balls)-1))
    b = balls.pop(random.randint(0, len(balls)-1))
    c = balls.pop(random.randint(0, len(balls)-1))
    if a == b == 'w':
        return c == 'w'
    return 0
w=int(input())
b=int(input())
exps = int(input())
sucs = 0
for i in range(exps):
    sucs += ex(w,b)
print(sucs / exps) 
