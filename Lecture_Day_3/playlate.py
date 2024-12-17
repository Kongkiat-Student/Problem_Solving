pay_rate = int(input("Enter pay rate: "))
hours = int(input("Enter hours of time: "))

if hours < 160:
    saraly = hours * pay_rate
    print(f"{saraly:.2f}")
else:
    saraly = (pay_rate * 160) + ((hours - 160) * (1.5 * pay_rate))
    print(f"{saraly:.2f}")