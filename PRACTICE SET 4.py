#1 storing 7 fruits in a list entered by the user
n=7
a=[]
for i in range(n):
    x=input("ENTER A FRUIT:")
    a.append(x)
print(a)


#2 marks of 6 students and display in sorted manner
n=6
x=[]
for i in range(n):
    m=int(input(f"ENTER MARKS OF STUDENT {i+1}:"))
    x.append(m)
x.sort()
print(x)


#4 sum a list with 4 numbers
L1=[1,2,3,4]
x=sum(L1)
print(x)


#5 count the number of zeroes in the given tuple
a=(7,0,8,0,0,9)
print(a.count(0))


