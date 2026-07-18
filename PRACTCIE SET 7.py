#1 multiplication table of given number using for loop
x=int(input("ENTER A NUMBER:\n"))
for i in range(11):
    print(i*x)


#2
print("names: Soham, Harry, Sachin, Rahul")
L1=["harry" , "soham" , "sachin" , "rahul"]
name=input("PICK A NAME:\n").lower()
if name=="soham" or name=="sachin":
    print("GOOD MORNING!")
else:
    pass


#3 do #1 with while loop
x=int(input("ENTER A NUMBER:\n"))
i=0
while i<11:
    print(i*x)
    i+=1


#4 given number-prime or not
x=int(input("ENTER A NUMBER:\n"))
if x<2:
    print("number is not prime") 
for i in range (2,x):
    if x%i==0:
        print("number is not prime")
        break
else:
    print("number is prime")

#or
while True:
    x = int(input("ENTER A NUMBER:\n"))
    is_prime =True
    if x < 2:
        print(x, "is not a prime number")
    for i in range(2, x):
        if x % i==0:
            is_prime = False 
            break 
    if is_prime: #or u can say if is_prime==True 
        print(x, "is a prime number")
    else:
        print(x, "is not a prime number")


#5 sum of first n natural numbers using while loop
n=int(input("ENTER THE NUMBER TILL WHICH SUM OF NUMBERS HAS TO BE FOUND:\n"))
i=0
c=0
while c<=n:
    i+=c
    c+=1
print(i)


#6 factorial of a number using for loop
n=int(input("ENTER THE NUMBER WHOSE FACTORIAL IS TO BE FOUND:\n"))
c=1
a=1
for i in range(1,n+1):
      a*=c
      c+=1
print(a)


#7 print the star pattern
n=3
c=-1
a=3
for i in range(n):
    c+=2
    a-=1
    print(" "*a , end="") 
    print("*"*c , end="")
    print(" "*a)


#8 print star pattern
n=3
c=1
for i in range(n):
    print("*"*c)
    c+=1
    

#9 star pattern
n=3
for i in range(n):
   if i==0 or i==n-1:
       print("*"*n)
   else:
        print("*" + " "*(n-2) + "*")

    
#10 print multiplication table IN REVERSE ORDER using for loop 
x=int(input("Enter a number:"))
a=10
for i in range(11):
      print(x,"X",a, "=" ,x*a)
      a-=1
