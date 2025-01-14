print('Please enter R -> Running')
print('Please enter C -> Cycling')
print('Please enter S -> Swimming')
print('Please enter N -> Next Day')
print('Pleae enter other key -> Out Program')

day = 1
sum_cal = 0

sum_time_run = 0
sum_time_cycling = 0
sum_time_swimming = 0

while True:
    print("Day is: " , day)
    while True:
        keep_key = str(input("Please select menu: "))
        if keep_key == "R":
            Running = float(input("PLease enter time for running: "))
            sum_time_run = sum_time_run + Running
            sum_cal = sum_cal + (Running * 10)
        elif keep_key == "C":
            Cycling = float(input("PLease enter time for cycling: "))
            sum_time_cycling = sum_time_cycling + Cycling
            sum_cal = sum_cal + (Cycling * 8)
        elif keep_key == "S":
            Swimming = float(input("Please enter time for swimming: "))
            sum_time_swimming = sum_time_swimming + Swimming
            sum_cal = sum_cal + (Swimming * 5)
        elif keep_key == "N":
            day = day + 1
            print("Day is: " , day)
        else:
            print("---------------------------------------------------")
            print("Sum day for exercise" , day , "day")
            print("---------------------------------------------------")
            print("Sum time Exercise by Running:" , sum_time_run , "minute")
            print("Sum time Exercise by Cycling:" , sum_time_cycling , "minute")
            print("Sum time Exercise by Swimming:" , sum_time_swimming , "minute")
            print("---------------------------------------------------")
            print("Sum kalorie Burnning:" , sum_cal , "Kalorie")
            print("---------------------------------------------------")
            break
    break
