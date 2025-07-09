#1. Create a list of items in your room you can potentially pack.
#2. Create an empty list to represent your travel bag 
#3. Repeatedly prompt the user for the index of an item to put in their travel bag by removing it from the the list of items in your room to your travel bag list.
#4. Once the list is complete, finalize it by creating a tuple representing your luggage. It should have every item in your travel bag. Empty the travel bag list as you do this.
#5. Print the contents of your luggage for the trip, as well as the number of items you decided to bring
roomitems = ["T-shirts", "hoodies", "underwears", 
             "toothbrushes", "toothpaste", "phone", "Ipad", "chargers", 
             "travel adapter", "games", "sunscreen", "shoes"]

travelbag = []

print("Pack them bags boy")
print("enter the index of an item you'd like to move from your room to your bag")
print("Type 'done' when your done putting the things your packing")

for item in roomitems:
    print(item)


item = int(input("item index: "))



while item != 100:
    travelbag.append(roomitems[item])
    roomitems.remove(roomitems[item])
    print("\nYour roomitems")
    print(roomitems)
    print("\nyour Travel Bag:")
    print(travelbag)
    item = int(input("item index: "))


for item in travelbag:
    print(item)