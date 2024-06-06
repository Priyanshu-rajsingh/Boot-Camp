# Q1: finding weather a number is odd or even without using mod operator
'''n = int(input("Enter N value: "))
if (n & 1) == 0:
    print("Even")
else:
    print("Odd")'''

'''#Q2 : check weather two numbers of the same sign or not

def checksign(x, y):
    return "Opposite" if (x^y)<0 else "Same"
print(checksign(-12,-13))'''

#Q3 : Find the missing number

'''def findmissingnumber(arr, n):
    x1 = arr[0]
    x2 = 1
    for i in range(1,n):
        x1 = x1 ^ arr[i]
    for j in range(2, n+2):
        j = x2 ^ j
    return x1 ^ x2

print(findmissingnumber([1,2,3,5],4))'''

'''    
# Q4 : Odd occuring number

def oddoccuringelement(arr, n):
    a = arr[0]
    for i in range(1, n):
        a = a ^ arr[i]
    return a

print(oddoccuringelement([2,4,3,2,4],5))'''

'''
# Q5 : Alternate bit check if same return true else false
def checksetbits(n):
    if(n & (n + 1)) == 0:
        return True
    return False
def alternatebits(n):
    res = n ^ (n >> 1)
    return checksetbits(res)
print(alternatebits(7))
'''
'''
# Q6 : count the number of set bits ( = 1) in a binary number
def countones(n):
    count = 0
    while n != 0:
        n = n & n-1
        count += 1
    return count
print(countones(9))
'''
'''
# Q7 : Program to add two numbers without any arithematic operators
def addbitwisly(x, y):
    while y!=0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x
print(addbitwisly(5,5))
'''    

def subset(arr, n):
    for i in range(1 << n):
        for j in range (n):
            if(i & 1 << j):
                print(arr[j],end =" ")
        print()
subset(['a','b','c'],3)



'''
def decimaltobinary(n):
    if n >= 1:
        decimaltobinary(n // 2)
        print(n % 2)

if n!=0 and (n & (n -1) == 0)
n is power of 2

a = a ^ b
b = a ^ b
a = a ^ b 
'''