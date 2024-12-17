loan_money = int(input("Please enter your loan: "))

if loan_money <= 1000:
    result = loan_money + (loan_money * (10 / 100))
    print(result)
elif loan_money <= 10000:
    result = loan_money + (loan_money * (5 / 100))
    print(result)
else:
    result = loan_money + (loan_money * (2 / 100))
    print(result)
