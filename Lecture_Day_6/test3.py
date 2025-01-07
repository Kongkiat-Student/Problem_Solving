import array as arr

number = arr.array('i',[50,87,65,39])

n_max = max(number)
n_min = min(number)
n_sum = sum(number) 
n_average = n_sum / len(number)
n_sorted = sorted(number)
n_sorted_2 = sorted(number , reverse=True)

print("Array: " , end= " ")
for i in range(4):
    print(number[i], end=" ")

print("\t")

print("Max =", n_max , "Min =" , n_min)
print("Sum =", n_sum , "Average =", n_average)
print(n_sorted)
print(n_sorted_2)