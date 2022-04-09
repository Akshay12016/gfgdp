n = int(input("Enter n: "))

holder1 = n
holder2 = n

prime = True

holder3 = 0
holder4 = 0

for i in range(2,n):
    if (n % i) == 0:
        prime = False


if(prime == True):
    print("The prime closest to " + str(n) + " is " + str(n))
else:
    while (prime == False):
        holder1 -= 1
        holder2 += 1

        for i in range(2,holder1):
            if (n % i) == 0:
                prime = False
            else:
                prime = True
                holder3 = holder1

        for i in range(2,holder2):
            if (n % i) == 0:
                prime = False
            else:
                prime = True
                holder4 = holder2


    if(abs(n - holder3) <= abs(n-holder4)):
        print("The prime closest to " + str(n) + " is " + str(holder3))
    elif (abs(n - holder3) > abs(n-holder4)):
        print("The prime closest to " + str(n) + " is " + str(holder4))