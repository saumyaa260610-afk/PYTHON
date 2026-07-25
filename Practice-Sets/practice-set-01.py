#factorial without functions or recursions
while True:
    n=int(input("enter number:"))
    if n<0:
        print("invalid.we cannot find factorial of negative numbers.")
        
    elif n==0 or n==1:
            print("1 is the factorial of 0")
    else:
        a=2
        fact=n*(n-1)
        for i in range(n):
          if i>=1 and a<n:
             fact=fact*(n-a)
             a+=1
          else:
             continue
        print(fact,"is the factorial of",n)

    
#factorial using functions
while True:
    def fact(n):
        if n<0:
            print("invalid.we cannot find factorial of negative numbers.")
        elif n==0 or n==1:
                print("1 is the factorial of",n)
        else:
            a=2
            fact=n*(n-1)
            for i in range(n):
              if i>=1 and a<n:
                 fact=fact*(n-a)
                 a+=1
              else:
                 continue
            print(fact,"is the factorial of",n)
    n=int(input("enter number:"))
    fact(n)

#factorial using recursions
while True:
    def fact(n):
        if n<0:
           return "invalid"
        elif n==0 or n==1:
            return 1
        else:
            return n*fact(n-1)
    n=int(input("enter no:"))
    print(fact(n))














