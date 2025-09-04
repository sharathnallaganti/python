"""
we have 2 types of vriables in class  1. instance Variable  2. class varibles

=> we have different types of methods in the classes
1. instance methods   > used for instance variables
2. class method       > used for class variables
3. static method   

"""

class Student:

    School = "Hyderabad Public School" # class variable 

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2       #  m1, m2, m3 are Instance variables 
        self.m3 = m3

    def ave(self):
         return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def get_School_Name(cls):
        return cls.School
   
    @staticmethod
    def info():
        print("this is student class")

student1 = Student(89,81,72)
student2 = Student(90,53,65)
student3 = Student(38,99,74)


print(student2.ave())

print(Student.get_School_Name())

Student.info()