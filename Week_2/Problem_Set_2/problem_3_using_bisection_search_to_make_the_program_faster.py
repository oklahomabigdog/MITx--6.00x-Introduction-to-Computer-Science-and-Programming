balance = 999999
annualInterestRate = 0.18

newbalance = balance
monthlyrate = (annualInterestRate) / 12
guesses = 0
epsilon = 0.01
start = balance / 12
end = (balance * (1 + monthlyrate)**12) / 12
ans = (end + start)/2.0

while abs(0 - newbalance) >= epsilon:
    guesses += 1
    if guesses == 30:
        break
    newbalance = balance
    for i in range(0, 12):
        newbalance = round(((newbalance - ans) * (1 + monthlyrate)), 2)
    if  newbalance >= 0:
        start = ans
    else:
        end = ans
    ans = (end + start)/2.0
print("Lowest Payment: " + str(round(ans, 2)))