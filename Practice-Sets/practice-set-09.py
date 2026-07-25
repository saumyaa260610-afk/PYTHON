#1 reading text from a file- check if it contains "twinkle"
with open ("poems.txt","r") as f:
    text=f.read().lower()
    if "twinkle" in text:
        print("FILE CONTAINS WORD")
    else:
        print("FILE DOES NOT CONTAIN WORD")



#2 read the text from file for highscore and display, also update new highscore
with open("hiscore.txt","r")as f:
    text=f.read()
    if text=="":
        text=0
        print("no highscore set")
    else:
        print("highscore=",text)
        text=int(text)
with open("hiscore.txt","w")as f:
    score=int(input("enter new score:"))
    if score>text:
        print("Congrats, Highscore updated to: ",score)
        f.write(str(score))
    else:
        print("highscore remains same:",text)
        f.write(str(text))



#3write tables till 20 and place them in different files
for i in range(1,21):
    with open(f"tables{i}.txt","w") as f:
        for j in range(1,11):
            f.write(str(f"{i} X {j} = {i*j}\n"))

            
    
#4 replace word donkey with #######
with open("donkey.txt","r") as f:
    text=f.read()
with open("donkey.txt","w") as f:
    f.write(text.replace("donkey","######"))



#6 mine a log file and see if python is present,print line number
with open("logfile.txt","r") as f:
    text=f.read().lower()
    if "python" in text:
        print("python is present")
    else:
        print("python is not present")



#7 mine a log file and see if python is present,print line number
with open("logfile.txt","r") as f:
    i=1
    text=True
    while text:
        text=f.readline()
        if "python" in text:
            print(f"python is present on line{i}")
            i+=1
        else:
            i+=1



#8 creating a copy of a file
with open("file.txt","r")as f:
    text=f.read()
with open("filecopy.txt","w") as g:
    g.write(text)

    

#9 checking if 2 files are same
with open("tables1.txt","r")as f:
    text=f.read()
with open("tables1copy.txt","r")as g:
    text2=g.read()
if text==text2:
    print("both files are same")
else:
    print("both files are not same")



#10 wipe out contents of a file
with open("logfile.txt","w") as f:
    f.write("")


#11 rename a file
import os
os.rename("tables1copy.txt","copy of tables1.txt")
