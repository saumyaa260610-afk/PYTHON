#1
name=input("enter name:")
print(name, "Good Afternoon")

#2
name=input("enter name\n")
date=input("enter date\n")
letter= "dear xyz\nyou are selected!\nabc"
letter= letter.replace("xyz",name) 
letter= letter.replace("abc",date)
print(letter)


#3
string= input("enter a string:\n")
a=string.find("  ")
if a==-1:
    print("there is no double space in the given string")
else:
    print("there is double space in the given string")


#4 replace double space with single space in a string
string= input("enter a string:\n")  
if a==-1:
    print("there is no double space in the given string")
else:
    string= string.replace("  "," ")
    print (string)


#5
letter= "Dear Harry,\n This Python course is nice.\n\t Thanks!"
print(letter)
