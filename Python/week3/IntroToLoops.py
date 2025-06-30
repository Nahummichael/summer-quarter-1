geniuses = ["Nahum","Nishad", "Darron"]

for genius in geniuses:
    print(genius)

answer = input("Want the list again? Y/N: ")
while answer == "Y":
    for genius in geniuses:   
        print(genius)
    answer = input("should I keep looping Y/N: ")