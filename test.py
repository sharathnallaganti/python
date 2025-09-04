class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
        self.laptop = None  # Initialize laptop as None


    def show(self):
        return f"Student: {self.name}, Roll No: {self.roll_number}, Laptop: {self.laptop.show() if self.laptop else 'No Laptop'}"
    class Laptop:
        def __init__(self,name, ram, cpu):
            self.name = name
            self.ram  = ram
            self.cpu  = cpu
        def show(self):
            return f"{self.name},{self.ram},{self.cpu}"

    
student1 = Student("Sharath", 123121)
student2 = Student("Joshi", 877662)


laptop1= student1.Laptop("Dell","8GB","i5")
laptop2 = student2.Laptop("Apple","16GB","M4")


print(student1.show())
