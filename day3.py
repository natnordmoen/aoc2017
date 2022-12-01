import math

def spiral(n):#4
    k=math.ceil((math.sqrt(n)-1)/2)#1
    t=2*k+1#3
    m=t**2#9
    t=t-1#2
    if n>=m-t:
        return k-(m-n),-k
    else:
        m=m-t

    if n>=m-t:
        return -k,-k+(m-n)
    else:
        m=m-t

    if n>=m-t:
        return -k+(m-n),k
    else:
        return k,k-(m-n-t)

koord = spiral(368078)

print((abs(0-koord[0]))+ abs((0-koord[1])))

# part 2
# https://oeis.org/A141481/b141481.txt