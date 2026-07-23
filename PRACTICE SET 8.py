#1 greatest of 2 numbers using functions
def greatest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if c>b:
            return c
        else:
            return b
a=int(input("enter a no."))
b=int(input("enter another no."))
c=int(input("enter a 3rd no."))
print(greatest(a,b,c))



#2 celsius to fahrenheit using functions
c=int(input("enter temp in celsius:"))
def fahrenheit(c):
    f = ((9*c)/5) + 32
    print(f)
print("temp in fahr is:",end="")
fahrenheit(c)


#4 calc sum of first n natural nos using recursion
def add(n):
    if n>0:
        return n+add(n-1)
    elif n==0:                     
        return 0
    else:
        return "invalid"
n=int(input("enter n:"))
print(add(n))


#5  make the pattern
def pattern(n):
   for i in range (n,0,-1):
       print("*"*i)
n=int(input("enter n:"))
pattern(n)


#6 create a function tht converts inches to cms
def conversion(inch):
    return inch*2.54
inch=int(input("enter inches measurement:"))
print("measurement in cms is:",conversion(inch))


#7 remove a word from list and strip it simultaneously using functions
def func(element):
    l1.remove(element)
    print(l1)
    print(element.strip())
l1=["    apple   ","    banana"," straw "]
element=input("enter word from list to remove and strip:").lower()
func(element)

#8 multiplication table using functions
n=int(input("enter no.:"))
def multi(n):
    for i in range(11):
        print(n,"X",i,"=",n*i)
multi(n)
