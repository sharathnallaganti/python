"""
class ---  is blueprrint to create an object
object --- is an instance of class

Inside the class variables are called as "attributes" and functions called as "Methods"
  

=> id() function is used to print the object memory address()

=> every time when we create an object it will take the space and that space size is depends no of variables in object


Decorator in class like Constructor



Rule	Example
Use class keyword	class 
Use PascalCase for naming	class StudentRecord:
Indent everything inside class	4 spaces
Methods must include self	def speak(self):
Constructor must be __init__	def __init__(self):
Use self.variable for object attributes	self.age = 21
Use parentheses to create objects	p = Person()


"""

# Empty class

class Myclass:
  pass

# Class With Only Variables

class Person:
  name ="Sharath"
  age= 25

print(Person.name)
print(Person.age)



# Simple class

class computer:
     
     def config(self):
        print("i7, 16gb, 215gb")
comp1=computer()
comp1.config()





# another class with objects

class Cars:
    
     def __init__(self,Brand,Model,Year):
                
               self.Brand =  Brand
               self.Model =  Model
               self.Year =   Year
                
car1= Cars("TATA", "Nexon" , 2019)
car2= Cars("Mahindra", "Scarpio" , 2012)

 
print(car1.Brand ,car1.Model, car1.Year) # simple way to print the objects Attributes 

print(Cars)    # used the get the memory address of the class 

print(car1)   # used to print the Memory Address of the object




# 

class Student:
      
      def __init__(self,name ,roll_no):
            self.name = name
            self.roll_no = roll_no
      
      def __str__(self):
            return f"the name of the student is ,{self.name},and Roll number,{self.roll_no}"
        

student1 = Student("Sharath", 11231)
student2 = Student("Joshi", 98522)

print(student1)



# another way to print the objects
class Student:
      
      def __init__(self,name ,roll_no):
            self.name = name
            self.roll_no = roll_no
           
      
      def  show(self):
            print(" the name of the student is ",self.name , "and Roll number", self.roll_no)
      
   
        
student1 = Student("Sharath", 11231)
student2 = Student("Joshi", 98522)


student2.show()



# int method

class car:
    def __init__(self, brnad, model, year):

        self.brand = brnad
        self.model = model 
        self.year  = year

    def __str__(self):
       
        return f"{self.brand},{self.model},{self.brand}"

car1 = car("Tayota","Corolla",2016)

car2 = car("Tesla","medel S", 2019)

print(car1)
print(car2)


# there is another way to print the objects

class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", self.cpu , self.ram)

comp1 = Computer("i5","8GB")
comp2 = Computer("i7","16GB")


comp1.config()
comp2.config()



# Another Example

class Rectangle:
    
    def __init__(self,width,height):
        self.width =  width
        self.height = height
    
    def perimeter(self):
        print("The perimeter of the rectangle is", 2 * (self.height + self.width))
    
    def area(self):
        print("area of the rectangle is", (self.width * self.height) )

rec1 = Rectangle(2,4)
rec2 = Rectangle(10,11)


rec1.perimeter()

rec2.perimeter()

rec2.area()
