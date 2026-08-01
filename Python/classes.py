# class Student:
#     name="Mukesh"
#     age="35"
#     subject="python"
# object=Student()
# print(object.name)
# object.name="ankit"
# print(object.name)
# object1=Student()
# print(object1.name)
# class H:
#  def name(self,n):
#     return n
#  def namee(self,n):
#     return n
# a=H()
# print(a.name("ankit"))
# print(a.namee("divesh"))

#calculator
# class Calculator:
#     def add(self,a,b):
#        return a+b
#     def sub(self,a,b):
#        return a-b
#     def multi(self,a,b):
#        return a*b
#     def div(self,a,b):
#        return a/b
# c=Calculator()
# num1=float(input("Enter first number::"))
# num2=float(input("Enter second number::"))
# print("1.add")
# print("2.sub")
# print("3.multi")
# print("4.div")
# choice=int(input("enter choice::"))
# if choice==1:
#    print("addition",c.add(num1,num2))
# elif choice==2:
#    print("subtraction",c.sub(num1,num2))
# elif choice==3:
#    print("multiply",c.multi(num1,num2))
# elif choice==4:
#    print("division",c.div(num1,num2))
# else:
#    print("number invalid")

#constructor
# class Person:
#     def __init__(self):
#         print("Mukesh")
# obj1=Person()
    
# class Student:
#     def __init__(self,name,age=30):
#         self.name=name
#         self.age=age
# p1=Student("mukesh")
# p2=Student("ankit",20)
# print(p1.name,p1.age)
# print(p2.name,p2.age)

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p=Student("mukesh",35)
# print(p.name,p.age)

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def bark(self):
#         print(self.name+"says  woof!!")
# object=Dog("Buddy",5)
# object.bark()
# print(object.name,object.age)
    
# Inheritance

# class Student:
#     def __init__(self,name,age,major):
#         self.n=name
#         self.a=age
#         self.m=major
#         print("Student Created")
#     def info(self):
#         return f"{self.n},{self.a},{self.m}"
# s1=Student("Mukesh",30,"Information Technology")
# s2=Student("Ankit",17,"Computer sciennce")
# print(s1.info())
# print(s2.info())
# class Student1(Student):
#     def full_info(self):
#         return "Hello we are student"
# obj=Student1("Divesh",20,"CSE")
# print(obj.info())
# print(obj.full_info())

# class person:
#     def __init__(self,firstname,lastname):
#         self.fn=firstname
#         self.ln=lastname
#     def intro(self):
#         return(f"{self.fn},{self.ln}")
# object=person("mukesh", "singh")
# print(object.intro())
# class person1(person):
#     pass
# obj=person1("Rajat", "Singh")
# print(obj.intro())  

#multiple
# class Math:
#     def add(self,a,b):
#         return a+b
# class Show:
#     def show(self,value):
#         print("Result:",value)
# class Result(Math,Show):
#     def calculate(self,a,b):
#         total=self.add(a,b)
#         self.show(total)
# r=Result()
# r.calculate(10,20)

# class ParentA:
#     def father(self,name,age):
#      self.fathername=name
#      self.fatherage=age
# class ParentB:
#     def mother(self,name,age):
#      self.mothername=name
#      self.motherage=age

# class Child(ParentA, ParentB):
#    def child(self,name):
#       self.childname=name
      
#       print(self.childname, "father & mother name is",self.fathername,"and",self.mothername)
#       print(self.childname,"father and mother age is:",self.fatherage,"and",self.motherage)
# c=Child()
# c.father("Mukesh",37)
# c.mother("Vandana",32)
# c.child("Devanshi")

# using super function




# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"Animal created: {self.name}, {self.age} years old")
# class Dog(Animal):
#     def __init__(self,name,age,breed):
#         super().__init__(name,age)
#         self.breed=breed
#         print(f"Dog created: {self.name}, {self.age} years old, Breed: {self.breed}")
# d=Dog("Buddy",5,"Labrador")

# Using abstract
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def engine(self):
#         print("This is an abstract method for engine")
#     @abstractmethod
#     def wheels(self):
#         print("This is an abstract method for wheels")
#     @abstractmethod
#     def fuel(self):
#         print("This is an abstract method for fuel")
# class Car(Vehicle):
#     def engine(self):
#         print("Car has a petrol engine")
#     def wheels(self):
#         print("Car has 4 wheels")
#     def fuel(self):
#         print("Car uses petrol")
# class Bike(Vehicle):
#     def engine(self):
#         print("Bike has a petrol engine")
#     def wheels(self):
#         print("Bike has 2 wheels")
#     def fuel(self):
#         print("Bike uses petrol")
# c=Car()
# c.engine()
# c.wheels()
# c.fuel()
# b=Bike()
# b.engine()
# b.wheels()
# b.fuel()

# Eancapulation

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def show(self):
#         print (f" Candidate Name: {self.name}, Candidate Age: {self.__age}")

# s=Student("Mukesh",35)
# s.show()

#using getter method
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def show(self):
#         print(f"My name is: {self.name}, My name is: {self.__age}")
# p=Person("mukesh",35)
# print(p.get_age())
# p.show()
#using setter method
# class Person1:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         if age>0:
#             self.__age=age
#         else:
#             print("Invalid age")
#     def show(self):
#         print(f"My name is: {self.name}, My name is: {self.__age}")

# p1=Person1("Mukesh",25)
# p1.show()
# p1.set_age(30)
# p1.show()
# p1.set_age(-5)
# p1.show()

# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.__grade=0
#     def set_grade(self,grade):
#         if 0 <= grade <=100:
#             self.__grade=grade
#         else:
#             print("Grade must be between 0 to 100")
#     def get_grade(self):
#         return self.__grade
#     def get_status(self):
#         if self.__grade >=60:
#             print ("Passed")
#         else:
#             print("Failed")
# s=Student("Mukesh")
# s.set_grade(70)
# print(s.get_grade())
# print(s.get_status())
