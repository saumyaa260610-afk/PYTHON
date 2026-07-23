#1 dictionary- words with translation- allow person to ask meanings of the entered word
dict={'Aam':'Mango', 'Sev':'Apple', 'Admi':'Man'}
print("options are:", dict.keys())
x=input("enter the hindi word:\n")
print("The meaning of the hindi word is:" ,dict[x])


#2 input 8 nos from user and display all numbers such tht no number repeats
n=8
a=set()
for i in range(n):
    x=int(input(f"enter number{i+1}:"))
    a.add(x)
print("All nos w/out repetition from the set is/are:" ,a)


#3 can v have a set with 18(int) and "18"(str) in it?--yes
a={18, "18"}
print(a)


#6 create empty dict- 4 users- enter a lang as value and name will be the key
dict={}
n=4
for i in range(n):
    k=input(f"{i+1})\nEnter name:")
    v=input("Enter language:")
    new={k:v}
    dict.update(new)
print("Dictionary is:", dict)
