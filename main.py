# Net Income Calculator
# JetBrains Academy - Hyperskill

print("Earned amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")

print()

# Calculate total income
income = 202 + 118 + 2250 + 1680 + 1075 + 80

print(f"Income: ${income}")

# Get expenses from user
print("Staff expenses:")
staff_expenses = int(input())

print("Other expenses:")
other_expenses = int(input())

# Calculate net income
net_income = income - staff_expenses - other_expenses

# Display net income
print(f"Net income: ${net_income}")
