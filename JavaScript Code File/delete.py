
# name="Rohan"
# age="89"

# str1="My name is {1} and age is {0}"
# print(str1.format(name,age))
# print(str1.format(age,name))

# print(f"my name is: {name} and age {age}")

# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a | b) # Union: {1, 2, 3, 4}
# print(a & b) # Intersection: {2, 3}
# print(a - b) # Difference: {1}
# print(a ^ b) # Symmetric Difference: {1, 4}

str1={
    "name":"Rohan",
    "age":90,
    "adhar":123456789
}

# print(str1["adhar"])

# for key in str1:
#     print(key,str1[key])

# for key in str1.keys():
#     print(key)

# for key in str1.values():
#     print(key)

# for key,value in str1.items():
#     print(key,value)

# age = -5
# if age < 0:
#     raise ValueError("Age cannot be negative")

# age = 12
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# import module1

# module1.addTwoNum(4,6)

# list1=[3,4,5,6,7]

# for index,value in enumerate(list1,start=5):
#     print(index,value)

# print(dir(module1))

# import math
# print(dir(math))
# help(math.sqrt)

# import os
# print(os.getcwd())

# os.rmdir("shiva")

# for i in range(100):
#     os.mkdir(f"MyFolder{i}")

# for i in range(100):
#     os.rmdir(f"Neeraj {i}")

# for i in range(100):
#     os.rename(f"MyFolder{i}",f"Neeraj {i}")
# for 

# f=open("data.txt","r")
# print(f.read())

# f=open("data1.txt","w")
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f.seek(6)
# print(f.readline())
# print(f.tell())
# f.write("Hello word")
# f.truncate(5)

# class Car:
#     company="Tesla"
#     def __init__(self,name ,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

#     def printDetail(self):
#         print(f"My name is: {self.name}")
#         print(f"My name is: {self.age}")
#         print(f"My name is: {self.salary}")

#     @staticmethod
#     def addTwoNum(num1,num2):
#         print(f"The sum is: {num1+num2}")

#     @classmethod
#     def takeValue(cls,str2):
#         name,age,salary=str2.split("-")
#         return cls(name,int(age),int(salary))

    
# obj1=Car("Rohan-56-67000")
# sr1="Rohan-78-4500"
# obj1=Car.takeValue(sr1)
# obj1.printDetail()

# print(dir(obj1))
# print(obj1.__dict__)

# obj1=Car("Rohan",67,78000)
# print(obj1.salary)
# obj1.printDetail()

# obj2=Car("Geeta",67,78000)
# obj2.printDetail()

# def decor(hero):
#     def wrapper_function():
#         print("Before the function runs")
#         hero()
#         print("After the function runs")
#     return wrapper_function

# @decor
# def greet():
#     print("hello Good Morning")

# @decor
# def greet1():
#     print("hello Good enving")


# greet()
# greet1()

# class Girl:
#     def walk(self):
#         print("Human can walk")

# class Lady(Girl):
#     def running(self):
#         print("Human can run")

# # g1=Girl()
# # g1.walk()
# # g1.running()

# # g1=Lady()
# # g1.walk()
# # g1.running()

# class Boy:
#     def sleep(self):
#         print("Human can sleep")

# class Man(Boy):
#     def laugh(self):
#         print("Human can laugh")

# class NewBorn(Lady,Man):
#     def weep(self):
#         print("Human can weep")

# h1=NewBorn()
# h1.weep()
# h1.running()


class Human:
    company="Tesla"
    def __init__(self,name ,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def printDetail(self):
        print(f"My name is: {self.name}")
        print(f"My name is: {self.age}")
        print(f"My name is: {self.salary}")

# obj1=Human("Shubham",78,23000)
# print(dir(obj1))

# class Human:
#     company="Tesla"
#     def __init__(self,name ,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
    
#     def __str__(self):
#         return f"My name is: {self.name} age is: {self.age} and salary {self.salary}"

#     def __len__(self):
#         return len(self.name)

# obj1=Human("Shubham",78,23000)

# print(obj1.__str__())
# print(obj1)
# print(len(obj1))

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __str__(self):
#         return f"({self.x},{self.y})"

#     def __add__(self, other):
#         self.x=self.x+other.x
#         self.y=self.y+other.y
#         return Point(self.x,self.y)

# p1=Point(5,7)
# p2=Point(3,4)

# print(p1)
# print(p2)

# p3=p1+p2

# print(p3)

import time
# Current time in seconds
# print("Epoch time:", time.time())

# Delay for 2 seconds
# print("Wait for 2 seconds...")
# time.sleep(2)
# print("Resumed!")

# local = time.localtime()
# print("Local time tuple:", local)

# print("Formatted:", time.strftime("%Y-%m-%d %H:%M:%S", local))

# time_str = "2025-07-16 11:00:00"

# parsed = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")

# print("Parsed time tuple:", parsed)

# import argparse

# # Create parser
# parser = argparse.ArgumentParser(description="Simple calculator utility")

# # Add arguments
# parser.add_argument("num1", type=float, help="First number")
# parser.add_argument("num2", type=float, help="Second number")
# parser.add_argument("--operation", "-o", choices=["add", "sub"],
# default="add", help="Operation to perform")
# # Parse arguments
# args = parser.parse_args()
# # Perform operation

# if args.operation == "add":
#     result = args.num1 + args.num2
# else:
#     result = args.num1 - args.num2
# print("Result:", result)