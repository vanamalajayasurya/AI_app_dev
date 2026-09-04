# list

from os import name


fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(fruits)
print(type(fruits))
print(fruits[0])
print(fruits[4])
fruits[2] = "mango"
print(fruits)

# tuple 

Names = ("jayasurya", "nikhil", "charan", "teja", "manoj")
print(Names[1])
print(type(Names))

Names = list(Names)
Names[1] = "monu" 

print(Names)
print(type(Names))


# dictionary 

student = {
    "name": "Jayasurya",
    "age": 22,
    "city": "Hyderabad",
    "is_student": True
}

print(student["name"])
print(student["city"])

student["weight"] = 70.5


print(student)

a = 20
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)







