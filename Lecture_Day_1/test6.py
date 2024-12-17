print("***Calculate the sum between start and stop number***")

start_num = int(input("Enter the start numbers: "))
end_num = int(input("Enter the end numbers: "))

total_sum = 0

for i in range(start_num,end_num+1):
    total_sum += i

print(f"the sum from {start_num} to {end_num} is: " , total_sum)