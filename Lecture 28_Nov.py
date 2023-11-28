class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def say_hi(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Age: {self.age}")
        
class Student(Person):
    def __init__(self, name):
        super().__init__(name, 15, "male")
        
    def say_hi(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Age: {self.age}")
        
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name, 33, "male")
        
    def say_hi(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Age: {self.age}")
        

obj1 =Person("Salim", 17, "male")
obj1.say_hi()

obj2 = Student("Yahya")
obj2.say_hi()

obj3 = Teacher("Saud")
obj3.say_hi()