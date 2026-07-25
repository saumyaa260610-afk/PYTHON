#1 create class ,representing 2d vector, use it to create class representing 3d vector
class C1:
    def __init__(self,icap,jcap):
        self.icap=icap
        self.jcap=jcap
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"
class C2(C1):
    def __init__(self,icap,jcap,kcap):
        super().__init__(icap,jcap)
        self.kcap=kcap
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
xyz=C1("30","20")
abc=C2("30","20","10")
xyz.__str__()
abc.__str__()


#2create class pets from class animal and class dog from class pets. add a method to dog.
class animal:
    def __init__(self,name):
        self.name=name
class pets(animal):
    def __init__(self,name):
        super().__init__(name)
        print(f"name of animal:{self.name}")
class dog(pets):
    def __init__(self,name):
        super().__init__(name)

owl=dog("owl")


#3 create class bank account- storing account holder's name and balance; allow user to deposit and withdraw money; finally show account details.
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,dep):
        print(f"{dep} rupees deposited.")
        self.balance=self.balance+dep
    def withdraw(self,draw):
        if self.balance>=draw:
                   print(f"{draw} rupees withdrawn.")
                   self.balance=self.balance-draw
        else:
            print(f"current balance:{self.balance} rupees \nAmount to be withdrawn should be less than current balance.")
    def details(self):
        print(f"Name:{self.name}\nCurrent balance:{self.balance} rupeess")
tom=BankAccount("tom",25000)
tom.deposit(0)
tom.withdraw(5000)
tom.details()


#4 create class student- storing student's name and marks of 3 subs; calculate avg marks and highest mark ; finally display all details.
class Student:
    def __init__(self,name,eng,math,sci):
        self.name=name
        self.eng=eng
        self.math=math
        self.sci=sci
    def avg(self):
        self.avg=(self.eng+self.math+self.sci)/3
    def highest(self):
        if self.eng>self.math:
            if self.eng>self.sci:
                self.highest="English"
            else:
                self.highest="Science"
        else:
            if self.math>self.sci:
                self.highest="Maths"
            else:
                self.highest="Science"
    def details(self):
        print(f"Name:{self.name} \nEnglish marks:{self.eng} \nMath marks:{self.math} \nScience marks:{self.sci} \nAverage of all marks:{self.avg} \nHighest mark:{self.highest}")
tom=Student("tom",95,91,96)
tom.avg()
tom.highest()
tom.details()


#5 create class movie- store movie name, genre, rating (/10);  change ratings, display movie details, and show if movie is recommended or not.
class Movie:
    def __init__(self,name,genre,rating):
        self.name=name
        self.genre=genre
        self.rating=rating
    def change_rating(self,newrating):
        self.rating=newrating
    def details(self):
        print(f"Name of movie:{self.name} \nGenre:{self.genre} \nRating:{self.rating}")
    def recommend(self):
        if self.rating>=8:
            print(f"Movie is recommended.")
        else:
            print("Worth watching.")

Avengers=Movie("Avengers","Action",9)
Avengers.change_ratings(10)
Avengers.details()
Avengers.recommend()

        
        
        
        
        
        
        
        
        
    


    
    
