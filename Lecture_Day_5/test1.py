input_str = str(input(""))
list_str = []
for str in input_str:
    list_str.append(str)
list_str.reverse()
full_str = sum(list_str)
print(full_str)