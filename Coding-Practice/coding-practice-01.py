# Leap Year
while True:
    year=int(input("enter year:"))
    if year%4==0 and year%100!=0 or year%400==0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
    choice=input("would you like to continue?(yes/no): ").lower()
    if choice==no:
        break


# Print all prime numbers within an interval
start=int(input("enter start number:"))
stop=int(input("enter stop number:"))
for i in range(start,stop+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
    else:
        pass


# Fibonacci series
n=int(input("enter number:"))
def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    elif n>1:
        return fib(n-1)+fib(n-2)
    else:
        return "invalid"
print(fib(n))


# Armstrong number
number=int(input("enter number:"))
original=number
count=0
n=len(str(number))
if number<0:
    print("Not armstrong")
else:
    while number!=0:
        last_digit=number%10
        count+=(last_digit)**n
        number=number//10

    if count==original:
        print("Armstrong number")
    else:
        print("Not armstrong")


# Print Armstrong numbers in an interval
start=int(input("enter start number:"))
stop=int(input("enter stop number:"))
for number in range(start,stop+1):
    if number<0:
        pass
    n=len(str(number))
    original=number
    count=0
    while number!=0:
        last_digit=number%10
        count+=(last_digit)**n
        number=number//10

    if count==original:
        print(original)
