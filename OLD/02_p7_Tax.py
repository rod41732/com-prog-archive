income = int(input().strip())
tax = 0
tax += min(income, 100000)*0.05
income -= 100000
if income > 0:
  tax += min(income, 400000)*0.10
  income -= 400000
if income > 0:
  tax += min(income, 500000)*0.20
  income -= 500000
if income > 0:
  tax += min(income, 3000000)*0.30
  income -= 3000000
if income > 0:
  tax += income*0.37
print(tax)
