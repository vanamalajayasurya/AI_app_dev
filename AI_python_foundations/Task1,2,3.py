students = ["Ravi", "Anil", "Kiran", "Suresh"]
print("List of students:", students)

for i in range(len(students)):
    if students[i] == "Kiran":
        print("Student found:", students[i])
        break

else:
    print("Student not found")
