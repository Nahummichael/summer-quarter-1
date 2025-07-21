class studentProfile:
    def __init__(self, name, age, grade, hobbies):
        self.student = {}
        self.student["Name"] = name
        self.student["Age"] = age
        self.student["Grade"] = grade
        self.student["Hobbies"] = hobbies

        
    def SetName(self):

        studentName = input("Enter the student's name: ")
        self.student["Name"] = studentName

    def SetAge(self):
        studentAge = input("Enter the student's age: ")
        self.student["Age"] = studentAge

    def SetGrade(self):
        studentGrade = input("Enter the student's grade: ")
        self.student["Grade"] = studentGrade

    def SetHobbies(self):
        hobbies = []
        hobby = input("enter student hobby (btw type: done when your finished): ").lower()
        
        
        while hobby != "done":
            hobby = input("enter student hobby (btw type: done when your finished): ").lower()
            hobbies.append(hobby)
        self.student["Hobbies"] = hobbies

      