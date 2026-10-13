# 이름_test_prepare_code.py 로 저장

"""
문제 내용을 적거나 문제 위치(ex.파이썬 17차시 과제 9번 문제)를 적어주세요. 
"""
#### 예시 ####
"""
코딩테스트 입문 : 배열 뒤집기
https://school.programmers.co.kr/learn/courses/30/lessons/120821
정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
"""
#### 예시 ####

## 푼 코드를 적어주세요
#### 예시 ####
def solution(num_list):
    answer = list(reversed(num_list))   # 리스트 거꾸로 하는 방법1: reversed() 쓰기  
    return answer

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [1, 1, 1, 1, 1, 2]
num_list3 = [1, 0, 1, 1, 1, 3, 5]	

print(solution(num_list1))

print(solution(num_list2))

print(solution(num_list3))
#### 예시 ####


## (선택) 그밖에 해당 코드 관련 알면 좋을 내용을 적어주세요.
#### 예시 ####
def solution(num_list):
    return num_list[::-1]     # 리스트 거꾸로 하는 방법2: 리스트 슬라이싱  

num_list1 = [1, 2, 3, 4, 5]
print(solution(num_list1))


def solution(num_list):
    result =[]
    while(num_list):
        result.append(num_list.pop())   # 리스트 거꾸로 하는 방법3: 스택 사용 
    return result

num_list1 = [1, 2, 3, 4, 5]
print(solution(num_list1))
#### 예시 ####