# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
#
# In this problem, we will not be dealing with a minimum monthly payment rate.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
#
# Lowest Payment: 180

balance = 1000
annualInterestRate = 0.1
monthlyInterestRate = annualInterestRate / 12
monthlypay = 10

def eachmonth(x):
    balancenew = round((x - monthlypay)*(1 + monthlyInterestRate), 2)
    return balancenew

def showBalance(y):
    for i in range(1, 13):
        temp = y
        y = eachmonth(temp)
        # print('In', i,'month, should pay: ', monthlypay)
        # print('In', i,'month, the balance is: ', y)
    return y


while showBalance(balance) > 0:
    monthlypay +=10


print('Lowest Payment:', monthlypay)