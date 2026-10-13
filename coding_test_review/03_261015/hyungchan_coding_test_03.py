# hyungchan_coding_test_03.py

def solution(num_list):
    answer = list(reversed(num_list))
    return answer

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [1, 1, 1, 1, 1, 2]
num_list3 = [1, 0, 1, 1, 1, 3, 5]	

print(solution(num_list1))

print(solution(num_list2))

print(solution(num_list3))