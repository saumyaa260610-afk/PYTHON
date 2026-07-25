#1 open 3 text files- if any one of these are not present, print a message without exiting.
try:
    def read(file):
        with open(file,"r") as f:
            print(file.read())
    read("1.txt")
    read("2.txt")
    read("3.txt")
except FileNotFoundError:
    print("file does not exist.")

#2 print third, fifth, and seventh element from a list using enumerate function.
l1=[5,8,9,0,4,3,28,5,2,3,7]
for index,item in enumerate(l1):
    if index==2 or index==4 or index==6:
        print(item)

#3 display a/b where a,b are integers; if b=0 then show error without exiting program.
try:
    a=int(input("enter integer:"))
    b=int(input("enter another integer:"))
    print(f"{a}/{b} is={a/b}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
    
