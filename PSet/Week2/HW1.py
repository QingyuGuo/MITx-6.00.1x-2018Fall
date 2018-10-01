# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#
# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print
#
# Remaining balance: 813.41
# instead of
#
# Remaining balance: 813.4141998135
# So your program only prints out one thing: the remaining balance at the end of the year in the format:
#
# Remaining balance: 4784.0
# A summary of the required math is found below:
#
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = 100
annualInterestRate = 0.1
monthlyPaymentRate = 0.1
monthlyInterestRate = annualInterestRate / 12
# totalPay = 0

def eachmonth(x):
    monthlypay = round(x * monthlyPaymentRate, 2)
    balancenew = round((x - monthlypay)*(1 + monthlyInterestRate), 2)
    return monthlypay, balancenew

for i in range(1, 13):
    temp = balance
    monthlypay = eachmonth(temp)[0]
    balance = eachmonth(temp)[1]
    # totalPay += monthlypay
    # print('In', i,'month, should pay: ', monthlypay)
    # print('In', i,'month, the balance is: ', balance)

# print('Total payment is:', totalPay)
print('Remaining balance:', balance)



