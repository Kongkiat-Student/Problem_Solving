end_num = int(input("Enter: "))


for num in range(1 , end_num + 1):

    odd_num = 0
    even_num = 0

    if num % 2 == 0:
        even_num += num
    elif num % 2 != 0:
        odd_num += num

print(odd_num)
print(even_num)