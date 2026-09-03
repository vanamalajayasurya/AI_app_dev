
#list

from os import name


list_of_data_types = [1, 2, 3, "a", 5]
print(type(list_of_data_types))
print(list_of_data_types[3])
print(list_of_data_types)

# change a value in list

list_of_data_types[3] = "monu"
print(list_of_data_types)

#tuple

Name = ("Jay", "surya", "sai", "teja")
print(type(Name))
print(Name[2])
print(Name)

# change a value in tuple
Name = list(Name)  
Name[2] = "Monu"  
print(Name)


# dictionary
student = {
    "name" : "Jay",
    "age" : 22,
    "weight" : 70.5,
    "height" : 5.9,
    "is_student" : True
}

print(student)
print(type(student))

# acess value

print(student["name"])
print(student["age"])


# athermatic operations
a = 30
b = 50
print(a + b)
print(a - b)
print(a*b)
print(a/b)
print(a%b)

#dictionary operations

distanory = {
    "jayasurya" : "HE PLAYS CRICKET"
    ,
    "surya" : "HE PLAYS FOOTBALL"
}

print(distanory["jayasurya"]) 
