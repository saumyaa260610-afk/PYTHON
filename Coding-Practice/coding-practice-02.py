# Sum of all natural numbers until the given number 
number=int(input("enter the number to stop adding :"))
def Sum(n):
    if n==0:
        return 0
    else:
        return n+Sum(n-1)
if number==0 or number<0:
    print("Please enter a natural number.")
else:
    print(Sum(number))


# Find numbers divisible by a number using lambda and filter()
n=int(input("enter a number to check divisibility:"))
start=int(input("entger range start value:"))
stop=int(input("enter range stop value:"))
result=filter(lambda i: i%n==0,range(start,stop+1))
for i in result:
    print(i)


# Finding HCF of 2 numbers (without using Euclid's Algorithm)
no1=int(input("enter number:"))
no2=int(input("enter another number:"))
if no2<no1:
    smaller=no2
else:
    smaller=no1
list_divisors=[]
for i in range(1,smaller+1):
    if no1%i==0 and no2%i==0:
        hcf=i
print(f"HCF of {no1} and {no2} is {hcf}")


# Shuffle a deck of cards
shape=["clubs","spades","hearts","diamonds"]
num=["A","K","Q","J",2,3,4,5,6,7,8,9,10]
list_deck=[]
for i in shape:
    for j in num:
        card=j,i
        list_deck.append(card)
import random
random.shuffle(list_deck)
for i in range(52):
    print(f"{list_deck[i][0]} of {list_deck[i][1]}")


# Display Calendar
year=int(input("Enter year:"))
month=int(input("Enter month number:"))
import calendar
print(calendar.month(year,month))


# Conversion of decimal to binary
def convert(n):
    if n>1:
        convert(n//2)
    print(n%2,end="")
number=int(input("Enter decimal number:"))
convert(number)


# Adding two matrices 
A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
B=[[1,2,3],
   [4,5,6],
   [7,8,9]]
C=[]
for i in range(len(A)):
    C.append([A[i][j]+B[i][j] for j in range(len(A[0]))])
for i in C:
    print(i)


# Transpose of a Matrix
A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
T=[]
for i in range (len(A)):
    T.append([A[j][i] for j in range(len(A[0]))])
for i in T:
    print(i)


# To check whether a string is palindrome or not
string=input("Enter word:").lower()
if string[::-1]==string:
    print(f"{string} is a plaindrome")
else:
    print(f"{string} is not a palindrome")
