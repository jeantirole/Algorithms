'''
(x+1) + (x+2) .. (x+i)

= i/2(x+1+x+i)
= ix + i/2(i+1)
N = ix + i/2(i+1)
1) ix = N - i/2(i+1)
2) x = (N - i/2(i+1)) / i 

'''


target_sum = 18  # 타겟 합  
min_range = 2  # 최소 범위


import sys

N, M = map(int, sys.stdin.readline().split())
for range_length in range(min_range, 101):
    remaining_sum = target_sum - (range_length * (range_length + 1) // 2)
    
    if remaining_sum % range_length == 0:
        start_number = remaining_sum // range_length 
        if start_number + 1 >= 0:
            print(*(num for num in range(start_number + 1, start_number + range_length + 1)))
            break
else:
    print(-1)
