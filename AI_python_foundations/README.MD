![1](image.png)
![2](image-1.png)
![3](image-2.png)
![4](image-3.png)
![5](image-4.png)git pull origin main

# Day 1 - Python Fundamentals

This project contains my Day 1 Python practice as part of my AI & Python learning journey.

## Topics Covered

- Printing text using `print()`
- Multiple values in `print()`
- Variables in Python
- Dynamic typing
- Python data types:
  - String
  - Integer
  - Float
  - Boolean

## File

- `AI_python_foundations/hello.py`

## Python Code Example

```python
print("Hello, World!")
print("Hello", "hi", "greetings")
print("HELLO MY NAME IS JAYASURYA")

# Variable declaration
# Dynamic typing
name = "Jayasurya"
print(type(name))

# Integer
age = 22
print(type(age))

# Float
weight = 70.5
print(type(weight))

# Boolean
is_student = True
print(type(is_student))

grade = "A"
print(type(grade))
```

## Expected Output

```
Hello, World!
Hello hi greetings
HELLO MY NAME IS JAYASURYA
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
```

## Author

**Vanamala Jayasurya**

## Day

**Day 1 Completed**

# Day 2 - Python Basics (README.md)

## 📚 Topics Covered

Today I learned the following Python basics:

### 1. List (`[]`)

* A list stores multiple values.
* Lists are **mutable** (values can be changed).

```python
list_of_data_types = [1, 2, 3, "a", 5]

print(type(list_of_data_types))
print(list_of_data_types[3])

list_of_data_types[3] = "monu"
print(list_of_data_types)
```

**Output:**

```
<class 'list'>
a
[1, 2, 3, 'monu', 5]
```

---

### 2. Tuple (`()`)

* A tuple stores multiple values.
* Tuples are **immutable** (values cannot be changed directly).
* To change a value, convert the tuple to a list.

```python
Name = ("Jay", "Surya", "Sai", "Teja")

Name = list(Name)
Name[2] = "Monu"

print(Name)
```

**Output:**

```
['Jay', 'Surya', 'Monu', 'Teja']
```

---

### 3. Dictionary (`{}`)

* A dictionary stores data in **key : value** pairs.
* Dictionaries are mutable.

```python
student = {
    "name": "Jay",
    "age": 22,
    "weight": 70.5,
    "height": 5.9,
    "is_student": True
}

print(student)
print(student["name"])
print(student["age"])
```

**Output:**

```
{'name': 'Jay', 'age': 22, 'weight': 70.5, 'height': 5.9, 'is_student': True}
Jay
22
```

---

### 4. Arithmetic Operations

Python supports basic mathematical operations.

```python
a = 30
b = 50

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
```

**Output:**

```
80
-20
1500
0.6
30
```

---

## ✅ Day 2 Summary

* Learned **List** and how to update values.
* Learned **Tuple** and the concept of **immutable**.
* Learned **Dictionary** and how to access values using keys.
* Practiced **basic arithmetic operators**: `+`, `-`, `*`, `/`, `%`.

**Day 2 completed. 🚀**

# Day 3 - Python Practice (README.md)

## 📚 Topics Covered

Today I practiced **Lists, Tuples, Dictionaries, Arithmetic Operators, Tax Calculator, and Restaurant Bill Calculator** in Python.

---

# 1. List Practice (`practice.py`)

## Code

```python
fruits = ["apple", "banana", "orange", "grape", "kiwi"]

print(fruits)
print(type(fruits))
print(fruits[0])
print(fruits[4])

fruits[2] = "mango"

print(fruits)
```

## Output

```text
['apple', 'banana', 'orange', 'grape', 'kiwi']
<class 'list'>
apple
kiwi
['apple', 'banana', 'mango', 'grape', 'kiwi']
```

## What I Learned

* Lists use `[]`.
* Lists are mutable (values can be changed).
* Index starts from `0`.

---

# 2. Tuple Practice (`practice.py`)

## Code

```python
Names = ("jayasurya", "nikhil", "charan", "teja", "manoj")

print(Names[1])
print(type(Names))

Names = list(Names)
Names[1] = "monu"

print(Names)
print(type(Names))
```

## Output

```text
nikhil
<class 'tuple'>
['jayasurya', 'monu', 'charan', 'teja', 'manoj']
<class 'list'>
```

## What I Learned

* Tuples use `()`.
* Tuples are immutable.
* Convert a tuple to a list using `list()` to modify values.

---

# 3. Dictionary Practice (`practice.py`)

## Code

```python
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
```

## Output

```text
Jayasurya
Hyderabad
{'name': 'Jayasurya', 'age': 22, 'city': 'Hyderabad', 'is_student': True, 'weight': 70.5}
```

## What I Learned

* Dictionaries use `{}`.
* Data is stored as `key : value`.
* New values can be added using a new key.

---

# 4. Arithmetic Operators (`practice.py`)

## Code

```python
a = 20
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
```

## Output

```text
26
14
120
3.3333333333333335
2
64000000
3
```

## What I Learned

| Operator | Meaning        |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `%`      | Remainder      |
| `//`     | Floor Division |
| `**`     | Power          |

---

# 5. Tax Calculator (`calculator.py`)

## Code

```python
print("======= calculator.py =======")

itemprice = float(input("Enter the item price: $"))
quantity = int(input("Enter the quantity: "))
tax = float(input("Enter the tax percentage: "))

totalprice = itemprice * quantity
print("Total price before tax:", totalprice)

taxamount = totalprice * (tax / 100)
print("Tax amount:", taxamount)

print("Total price after tax:", totalprice + taxamount)

print("======= calculator.py =======")
```

## Example Output

```text
======= calculator.py =======
Enter the item price: $100
Enter the quantity: 2
Enter the tax percentage: 5

Total price before tax: 200.0
Tax amount: 10.0
Total price after tax: 210.0
======= calculator.py =======
```

## What I Learned

* Used `input()` to get user input.
* Used `float()` and `int()` for type conversion.
* Calculated tax and final amount.

---

# 6. Restaurant Bill Calculator (`Restaurant Bill Calculator.py`)

## Code

```python
print("======= Restaurant Bill Calculator =======")

print("Enter the food price: ₹")
food_price = float(input())

print("Enter the number of items:")
number_of_items = int(input())

print("Enter the GST percentage:")
gst_percentage = float(input())

total_price = food_price * number_of_items

gst_amount = total_price * (gst_percentage / 100)

print("GST Amount: ₹", gst_amount)

print("Total Price: ₹", total_price + gst_amount)
```

## Example Output

```text
======= Restaurant Bill Calculator =======
Enter the food price: ₹250
Enter the number of items: 3
Enter the GST percentage: 5

GST Amount: ₹37.5
Total Price: ₹787.5
```

## What I Learned

* Calculated restaurant bill using GST.
* Used user input and arithmetic operations.
* Printed the final bill amount.

---

# ✅ Day 3 Summary

Today I practiced:

* Lists and updating values.
* Tuples and converting them to lists.
* Dictionaries and adding new key-value pairs.
* Arithmetic operators (`+`, `-`, `*`, `/`, `%`, `//`, `**`).
* Built a Tax Calculator project.
* Built a Restaurant Bill Calculator project.

## 📂 Files Used

* `AI_python_foundations/practice.py`
* `AI_python_foundations/calculator.py`
* `AI_python_foundations/Restaurant Bill Calculator.py`

## 👨‍💻 Author

**Vanamala Jayasurya**

## 🚀 Day 3 Completed


# 🚀 Day 4 – Python Data Structures & Debugging Challenge

## 📚 Topics Covered

* Lists
* Tuples
* Sets
* Dictionaries
* `for` loop
* `if-else`
* `break` statement
* Debugging Python code

---

## 💻 Program 1 – First Non-Repeating Character (Using Dictionary)

### Code

```python
def non_repeating_character(S):
    count = {}

    for ch in S:
        if ch != " ":
            count[ch] = count.get(ch, 0) + 1

    for ch in S:
        if ch != " " and count[ch] == 1:
            return ch

    return "No non-repeating character found"

print("Enter a string:")
S = input()

print("The first non-repeating character is:", non_repeating_character(S))
```

### Output

```text
Enter a string:
programming
The first non-repeating character is: p

Enter a string:
aabbcdd
The first non-repeating character is: c

Enter a string:
aabbcc
The first non-repeating character is: No non-repeating character found
```

---

## 💻 Program 2 – Student Search (Using `range(len(students))`)

### Code

```python
students = ["Ravi", "Anil", "Kiran", "Suresh"]

print("List of students:", students)

for i in range(len(students)):
    if students[i] == "Kiran":
        print("Student found:", students[i])
        break
else:
    print("Student not found")
```

### Output

```text
List of students: ['Ravi', 'Anil', 'Kiran', 'Suresh']
Student found: Kiran
```

---

## 💻 Program 3 – Student Search (Without `range(len(students))`)

### Code

```python
students = ["Ravi", "Anil", "Kiran", "Suresh"]

for student in students:
    if student == "Kiran":
        print("Student found:", student)
        break
else:
    print("Student not found")
```

### Output

```text
Student found: Kiran
```

---

## 🐞 Debugging Challenge

### Original Problem Output

```text
Student not found
Student not found
Student found: Kiran
Student not found
```

### Fixed Output

```text
List of students: ['Ravi', 'Anil', 'Kiran', 'Suresh']
Student found: Kiran
```

---

## 🎯 What I Learned Today

* Difference between List, Tuple, Set, and Dictionary.
* Searching an element in a list.
* Using `break` to stop a loop.
* Importance of indentation in Python.
* Using dictionaries to solve problems efficiently.

---

## 💡 What I Found Difficult

* Understanding the correct placement of `else`.
* Using `break` in loops.
* Solving the bonus challenge without `range(len(students))`.

---

## 📌 Day 4 Summary

* Practiced Python Data Structures.
* Solved the First Non-Repeating Character problem using a dictionary.
* Learned debugging with `for`, `if-else`, and `break`.
* Solved the Student Search problem with and without `range(len(students))`.

**#100DaysOfCode #Python #Day4 #LearningPython #VSCode**

