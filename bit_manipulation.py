#Bit Manipulation
#n = number on which operations are performed
#i = position
#k = changing value number

def getbit(n, i):
    return 1 if ((1 << i) & n) != 0 else 0
def setbit(n, i):
    return (n | (1 << i))
def clearbit(n, i):
    return (n & ~(1 << i))
def togglebit(n, i):
    return (n ^ (1 << i))
def updatebit(n, i, k):
    mask = ~(1 << i)
    n = n & mask
    return (n | (k << i))


print(getbit(5,1))
print(setbit(5,1))
print(clearbit(5,1))
print(togglebit(5,1))
print(updatebit(5,1,1))