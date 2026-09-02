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
