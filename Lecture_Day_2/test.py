print("***calculate sum of odd and even number (Exit press 0)***")

sum_even_num = 0
sum_odd_num = 0

while True:

    num = int(input("Enter number: "))
    if num == 0:
        print(f"sum of even number = {sum_even_num}")
        print(f"sum of odd numbers = {sum_odd_num}")
        break
    elif num % 2 == 0:
        sum_even_num = sum_even_num + num
    elif num % 2 != 0:
        sum_odd_num = sum_odd_num + num 
