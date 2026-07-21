#1 create class- storing info of few programmers
class programmer:
    company="microsoft"
    def info(self):
        print(f"name:{self.name}")
        print(f"salary:{self.salary}")
        print(f"company:{self.company}")
tom=programmer()
sneha=programmer()
tom.name="tom"
sneha.name="sneha"
tom.salary="50k"
sneha.salary="100k"
tom.info()
sneha.info()
 
#or using init:
class programmer:
    company="microsoft"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def info(self):
        print(f"name:{self.name},\ncompany:{self.company},\nand salary:{self.salary}")
tom=programmer("tom","50k")
sneha=programmer("sneha","100k")
tom.info()
sneha.info()


#2 create a calculator to find- square, sq.root, cube and cube root
class calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        print(f"square of {self.number} is {self.number**2}")
    def squareroot(self):
        print(f"square root of {self.number} is {self.number**0.5}")
    def cuberoot(self):
        print(f"cube root of {self.number} is {self.number**0.333}")
    def cube(self):
        print(f"cube of {self.number} is {self.number**3}")
x=calculator(2)
x.square()
x.squareroot()
x.cuberoot()
x.cube()


#3 create a class attribute and change its value using object
class xyz:
    a="25"
object=xyz()
object.a="30"
print(object.a) #value changes 
print(xyz.a)    #value remains constant


#4 greet user 
@staticmethod
def greet():
    print("hello there!")
greet()


#5 create a class which has methods to book a train, including availability of seats and fare info
class train:
    fare="800 rupees"
    seats="200"
    def __init__(self,name,number):
        self.name=name
        self.number=number
        print(f"Hello {self.name},\nfollowing are the details.")
        print("Train name:Intercity Express")
    def availability(self):
        print(f"no. of seats available are {self.seats}")
        print(f"no. of seats to book:{self.number}")
    def cost(self):
        print(f"fare per seat:{self.fare},\nThus,\nTotal fare:{self.number*800}")
    def concl(self):
            print(f"{self.number} seats have been booked.")
            
tom=train("tom",20)
tom.availability()
tom.cost()
tom.concl()
      
 
        

        
    


