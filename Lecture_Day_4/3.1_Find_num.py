start_num = int(input("Please enter start number: "))
end_num = int(input("Please enter end number: "))

for count in range(start_num + 1 , end_num):
    if count % 3 == 0:
        print(count)
        count += 1