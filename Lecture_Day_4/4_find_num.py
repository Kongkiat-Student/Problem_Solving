while True:
        start_num = int(input("Please enter start number: "))
        end_num = int(input("Please enter end number: "))
        division_num = int(input("Please enter division number:"))
        for count in range(start_num + 1 , end_num):
            if count % division_num == 0:
                print(count)
                count += 1
        keep_going = int(input("Exit Press 0, continue Press 1: "))
        if keep_going == 0:
             print("Bye")
             break
