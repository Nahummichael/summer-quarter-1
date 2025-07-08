student = {}

studentName = input("Enter the student's name: ")
student["Name"] = studentName

studentAge = input("Enter the student's age: ")
student["Age"] = studentAge


studentGrade = input("Enter the student's grade: ")
student["Grade"] = studentGrade

hobbies = []

hobby = input("enter student hobby (btw type: done when your finished): ").lower()
hobbies.append(hobby)
while hobby != "done":
    hobby = input("enter student hobby (btw type: done when your finished): ").lower()
    hobbies.append(hobby)

student["Hobbies"] = hobbies

print(student)