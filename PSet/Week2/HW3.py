balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
highBound = round((balance * (1 + monthlyInterestRate)**12) / 12.0, 2)
lowBound = round(balance / 12, 2)
monthlypay = (highBound + lowBound) / 2.0
delta = 1
count = 0

def eachmonth(x):
    balancenew = round((x - monthlypay)*(1 + monthlyInterestRate), 2)
    return balancenew

def showBalance(y):
    for i in range(1, 13):
        temp = y
        y = eachmonth(temp)
        print('In', i,'month, should pay: ', monthlypay)
        print('In', i,'month, the balance is: ', y)
    return y


while abs(showBalance(balance) - delta) >= 0:
    if showBalance(balance) < 0:
        highBound = monthlypay
        print('this is too large: ', monthlypay)
    else:
        lowBound = monthlypay
        print('this is too small', monthlypay)
    monthlypay = round((highBound + lowBound) / 2.0, 2)
    count +=1
    if count >100:
        break

print('Lowest Payment:', monthlypay)