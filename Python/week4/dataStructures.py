snacklist = ["plums", "fruit snacks", "BBQ lays", "M&Ms"]
snacklist.append("mangos")
for snack in snacklist:
    print(snack)

print()

myColleges = ("UC Berkeley","Howard","USC", "standford", "Contra Costa College")
for college in myColleges:
    print(college)

print()

actorsbday = {"Ana de Armas: April 30, 1988", 
              "Keanu Reeves: September 2, 1964",
              "Ryan Gosling: Ryan Gosling",
              "Debby Ryan: May 13, 1993", 
              "Chadwick Boseman: November 29, 1976"}
for bday in actorsbday:
    print(bday)

print()

carAttribute = {"Brand": "Honda",
                "Model": "Civic",
                "Year": "2026", 
                "Engine": "4-cylinder",
                "WheelSize": "18in"}
carAttribute["color"] = "blue"
for attribute in carAttribute:
    print(carAttribute.get(attribute))