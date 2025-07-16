# avaible money to spend
funds = 2500

# a dictionary of the items we are spending our budget on
# the key is the name of the item; and the value is the budget amount for said item
budgets = {}

# another dictionary of the expense of each budgeted item
# the key is the name of the item; and the value is the budget amount for said item
expenses = {}

# Adds an item to the budgets dictionary
def AddBudget(name, amount):
    global funds
    if name in budgets: # if the key is alr in our budgets dicitonary
        raise ValueError("STUPID AHH u alr got this item")
    if amount > funds:
        raise ValueError("fella u aint got the bands for allat 😂 brokie")
    budgets[name] = amount
    funds -= amount # the -= subtracts the current value funds is at and then amounts is subtracted by it
    expenses[name] = 0 # adds the budgeted item to the expenses dictionary
    return funds

def Spend(name, amount):
    if name not in expenses: #if the item isn't in the budget
        raise ValueError("dont got the money for this buckaro")
    expenses[name] += amount # add the expense to the budgeted item
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
    print("Budget              Budgeted    Spent   Remaining")
    print("-----------------------------------------------------")
    totalBudgeted = 0
    totalSpent = 0
    totalRemaining = 0
    for name in budgets:
        budgeted = budgets[name] # store the amount associated with that key
        spent = expenses[name] # store the amount spent on that given item
        remainingBudget = budgeted - spent # calculate the remaining
        print(f'{name:15s} {budgeted:10.2f} {spent:10.2f}'
              f'{remainingBudget:10.2f}')
        totalBudgeted += budgeted
        totalSpent += spent
        totalRemaining = remainingBudget
    print(f'{"total":15s}, {totalBudgeted:10.2f}, {totalSpent:10.2f}'
          f'{remainingBudget:10}')


print("Total funds:", funds)
# Add some items to the budget
AddBudget("Books:", 100)
AddBudget("Rent:", 800)
AddBudget("Car Note", 200)

# Spend some money on item in our budget
Spend("Books:", 50)
Spend("Rent:", 300)
Spend("Car Note", 200)

# display the enitre budget
PrintBudget()