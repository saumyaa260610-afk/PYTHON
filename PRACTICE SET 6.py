#1 finding greatest of 4 numbers entered by the user
a=int(input(f"ENTER 1st NUMBER:\n"))
b=int(input(f"ENTER 2nd NUMBER:\n"))
c=int(input(f"ENTER 3rd NUMBER:\n"))
d=int(input(f"ENTER 4th NUMBER:\n"))
if a>b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
else:
    print(d)

#or:
a=int(input(f"ENTER 1st NUMBER:\n"))
b=int(input(f"ENTER 2nd NUMBER:\n"))
c=int(input(f"ENTER 3rd NUMBER:\n"))
d=int(input(f"ENTER 4th NUMBER:\n"))
greatest=a
if b>greatest:
    greatest=b
if c>greatest:
    greatest=c
if d>greatest:
    greatest=d
print(greatest, "is the greatest number")
# we cannot use if elif else here becuz if v do then v hv to choose only 1 option
#but here when one condition is not satisfied, the next condition depends on it
#as the value held by the variable "greatest" may change.

#or
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if (num1 > num4):
    g1 = num1
else:
    g1 = num4

if (num2 > num3):
    g2 = num2
else:
    g2 = num3

if (g1 > g2):
    print(str(g1) + " is greatest")
else:
    print(str(g2) + " is greatest")

#or
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

print(max(num1, num2, num3, num4), "is greatest")



#2 pass or fail
a=int(input("ENTER MARKS OF SUB1-out of 50:\n"))
b=int(input("ENTER MARKS OF SUB2-out of 50:\n"))
c=int(input("ENTER MARKS OF SUB3-out of 50:\n"))
totalpercent=((a+b+c)*100)/150
per1=(a*100)/50
per2=(b*100)/50
per3=(c*100)/50
if totalpercent>=40 and per1>=33 and per2>=33 and per3>=33:
    print("pass")
else:
    print("fail")



#3 spam comment
text=input("ENTER THE TEXT:\n").lower()
a="make alot of money"
b="buy now"
c="subscribe this"
d="click this"
if (a,b,c,d) in text:
    print("SPAM TEXT")
else:
    print("NO SPAM")


#4 given username has less than 10 characters or no
x=input("ENTER THE USERNAME:\n")
if len(x)<10:
    print("YES")
else:
    print("NO")



#5 name is present in list or not case 1) list is not entered by user 2)list is
#entered by user
    
#case 1)
x=input("ENTER NAME:\n").lower()
abc=["shreya" , "saumyaa" , "shivansh"]
if x in abc:
    print("YES")
else:
    print("NO")
    
#case 2)
abc=[]
n=int(input("Enter the number of names to be added in the list:\n"))
for i in range(n):
    x=input(f"{i+1})ENTER NAME:\n").lower()
    abc.append(x)
name=input("ENTER THE NAME TO BE SEARCHED:").lower()
if name in abc:
    print("YES")
else:
    print("NO")

#6 calculating grade of student from marks given by user (scheme is given)
x=int(input("ENTER MARKS:\n"))
if x>=90 and x<=100:
    print("EXCELLENT")
elif x>=80 and x<90:
    print("A")
elif x>=70 and x<80:
    print("B")
elif x>=60 and x<70:
    print("C")
elif x>=50 and x<60:
    print("D")
elif x<50 and x>=0:
    print("FAILED")
else:
    print("INVALID MARKS- TRY AGAIN!")

#7 given post-talking about saumyaa or not
post=input("ENTER THE TEXT IN THE POST:\n").lower()
if "saumyaa" in post:
    print("POST TALKS ABOUT SAUMYAA")
else:
    print("POST DOES NOT TALK ABOUT SAUMYAA")
