balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total = 0
monthlyInterestRate = annualInterestRate/12

for r in range(1, 13):
    minpay = monthlyPaymentRate*balance
    interest = (balance - minpay)*monthlyInterestRate
    balance = balance - minpay + interest
    total = total + minpay
    print ("Month: " + str(r))
    print ("Minimum monthly payment: " + str(round(minpay, 2)))
    print ("Remaining balance: " + str(round(balance, 2)))
print ("Total paid: " +str(round(total, 2)))
print ("Remaining balance: " + str(round(balance, 2)))