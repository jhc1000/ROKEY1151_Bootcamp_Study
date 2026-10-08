# hyungchan_coding_test_01.py

"""
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
"""

"""
10 ≤ price ≤ 1,000,000
price는 10원 단위로(1의 자리가 0) 주어집니다.
소수점 이하를 버린 정수를 return합니다.
"""

# 만약, 500000 원 이상 : 0.8 배의 금액 지불
# 만약, 300000 원 이상 : 0.9 배의 금액 지불
# 만약, 100000 원 이상 : 0.95 배의 금액 지불
# 그외 : 1배의 금액 지불
# 지불 금액 반환시 소수점 이하를 버린 정수를 return

print('----------')
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
print('-----------')

import math
from math import floor 
# round() 반올림
# math.ceil() 올림
# math.floor() 버림

print(round(99.2))
print(math.ceil(99.1))
print(math.floor(99.6))

print('----------')
# round(수, 소수점자리)
print(round(3.14159, 2))
print(round(3.14159, 1))
print(round(314.1591, 0))
print(round(314.1591, -1))
print(round(314.1591, -2))

# ceil(), floor() 는 정수 단위로만 올림/버림
print(math.ceil(99.1))
print(math.floor(99.6))


print('----------')



# 사이트 솔루션
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
        
print(solution(150000))
print(solution(580000))
print('-----------')

# dict.items() 은 iterable
discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
print(discount_rates.items())
print("__iter__" in dir(discount_rates.items()))  # True # iterable
print("__next__" in dir(discount_rates.items()))  # False # iterable


#  for __ in ___ = iterable (range(5), "fjlsfjs", [1,2,5,7,5], discount_rates.items())
print('-----------')
# int는 소수점 버림 판정
print(int(float(123.999)))  # 123

print('-----------')
