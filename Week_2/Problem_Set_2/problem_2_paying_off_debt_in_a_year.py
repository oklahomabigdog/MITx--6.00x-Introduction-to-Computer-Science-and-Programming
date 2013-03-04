balance = 3926
annualInterestRate = 0.2

payment = 0
updated = balance
monthly = annualInterestRate/12

while (updated >= 0):
  updated = balance
  payment += 10
  for r in range(0, 12):
      updated = round(((updated - payment) * (1 + monthly)), 2)
print("Lowest Payment: " + str(payment))