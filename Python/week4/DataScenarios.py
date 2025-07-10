#1. A restaurant menu with prices for each item
#2. High scores to an arcade game
#3. All of the months of the year
#4. All the items in your backpack
#5. Look up Student emails by their names
#6. A shopping cart of groceries 
#7. [Add a scenario of your own]

#data structures: tuples, lissts, Dictionaries, sets

print("Scenario 1: A restaurant menu with prices for each item")
print("best structure: Dictionary; best for pairing foods, with prices in key/value")
menu = {
    "French Toast": 12,
    "Grand Slam": 12,
    "T-Bone Steak": 18,
    "Avacado Toast": 15
}
for key, item in menu.items():
    print(key, ":", item)

print("\nScenario 2: High scores to an arcade game")
print("best structure: List; Need a mutable structure to be able to change in real time")
highScores = [
    100,
    105,
    110,
    99,
    40
]
for score in highScores:
    print(score)

print("\nScenario 3: All of the months of the year")
print("best structure: tuple; the years of the month arent going to change")

year = (
    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)
for month in year:
    print(month)

print("\nScenario 4: All the items in your backpack")
print("best structure: list; because the things in my backpack can change depending on the day ahead")
Backpack = [
    "chrombook",
    "notebooks",
    "pens",
    "pencils",
    "textbooks"
]
for item in Backpack:
    print(item)

print("\nScenario 5: Look up Student emails by their names")
print("best structure: tuple; because the students' emails aren't going to change")
studentEmails = (
    "student email1",
    "student email2",
    "student email3",
    "student email4",
)

for email in studentEmails:
    print(email)
