# O(n) : Linear

import time

def test1(end_num):
    odd_num = 0
    even_num = 0

    for num in range(1 , end_num + 1):

        if num % 2 == 0:
            even_num += num
        else:
            odd_num += num
    return(odd_num,even_num)

start = time.time()
print(test1(500000))
print('Time of Funtion 1:' , (time.time()-start)*1000)
