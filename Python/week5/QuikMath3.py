class calculator:
    def Add(self, k, y):
        return k + y
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, c, d):
        return c * d
    
    def divide(self, e, f):
        if f != 0:
            return e / f
        else:
            return "dumb ahh you can't divide by zero"
    

theCalculator = calculator()
addingCalculator = theCalculator.Add(5,8)
subtractCalculator = theCalculator.subtract(10,4)
productCalculator = theCalculator.multiply(10, 9)
qoutientCalculator = theCalculator.divide(20, 5)

print("addition:", addingCalculator)
print("subtracting:", subtractCalculator)
print("product:", productCalculator)
print("qoutient:",qoutientCalculator)