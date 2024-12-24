target_money = float(input("Please enter your target money: "))
num_year = int(input("Please enter number of year: "))

key_choise = str(input("D ar M: "))


if key_choise == "D":
    num_month  = num_year * 12
    num_day = num_month * 30
    saving_money = target_money / num_day
    print("Per Day: " , saving_money)
elif key_choise == "M":
    num_month  = num_year * 12
    saving_money = target_money / num_month
    print("Per Month: " , saving_money)