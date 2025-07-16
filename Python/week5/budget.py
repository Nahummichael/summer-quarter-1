#convert the program into a class
# 1. define the class
# 2. create the ___init___() for your class
# 3. create your instance variable
#  4. refactor your instance variable




class BudgetManager():
    def __init__(self,amount):
        self.funds = amount

        self.budgets = {}

        self.expenses = {}


    def AddBudget(self, name, amount):
        global funds
        if name in self.budgets:
            raise ValueError("STUPID AHH u alr got this item")
        if amount > self.funds:
            raise ValueError("fella u aint got the bands for allat 😂 brokie")
        self.budgets[name] = amount
        self.funds -= amount 
        self.expenses[name] = 0 
        return self.funds

    def Spend(self, name, amount):
        if name not in self.expenses: 
            raise ValueError("dont got the money for this buckaro")
        self.expenses[name] += amount 
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def PrintBudget(self):
        print("Budget              Budgeted    Spent   Remaining")
        print("-----------------------------------------------------")
        totalBudgeted = 0
        totalSpent = 0
        totalRemaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name] 
            spent = self.expenses[name]
            remainingBudget = budgeted - spent
            print(f'{name:15s} {budgeted:10.2f} {spent:10.2f}'
            f'{remainingBudget:10.2f}')
            totalBudgeted += budgeted
            totalSpent += spent
        totalRemaining = remainingBudget
        print(f'{"total":15s}, {totalBudgeted:10.2f}, {totalSpent:10.2f}'f'{remainingBudget:10.2f}')

