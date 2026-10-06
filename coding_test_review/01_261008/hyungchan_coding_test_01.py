# hyungchan_coding_test_01.py

from math import floor 

def solution(price):
    answer = 0
    discount_ratio = 0.0
    if price >= 500000:
        discount_ratio = 0.2
    elif price >= 300000:
        discount_ratio = 0.1
    elif price >= 100000:
        discount_ratio = 0.05
    answer = floor(price*(1-discount_ratio))
    return answer

print(solution(150000))
print(solution(580000))

