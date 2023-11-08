p = float(input("Enter initial principal: "))

r = float(input("Enter interest rate: "))

t = float(input("Enter time: "))

n = float(input("Enter number of times: "))

SIMPLE_INTEREST = str(p * (1 + r * t))
COMPOUND_INTEREST = str(p * (1 + r/n) ** n * t)

print("YUSUF AND SONS")
print("SIMPLE INTEREST = " + SIMPLE_INTEREST)
print("COMPOUND INTEREST = " + COMPOUND_INTEREST)
