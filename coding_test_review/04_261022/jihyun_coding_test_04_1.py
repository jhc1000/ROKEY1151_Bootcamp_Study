#Lv.0 평행
# https://school.programmers.co.kr/learn/courses/30/lessons/120875

#  문제 설명
# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.




def solution(dots):
    (x1,y1),(x2,y2),(x3,y3),(x4,y4) = dots

    if (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1):
        return 1
    if (y3-y1)*(x4-x2) == (y4-y2)*(x3-x1):
        return 1
    if (y4-y1)*(x3-x2) == (y3-y2)*(x4-x1):
        return 1
    answer = 0
    return answer


# 예시 1번 데이터 (평행한 경우 -> 결과: 1)
test_dots_1 = [[1, 4], [9, 2], [3, 8], [11, 6]]
result_1 = solution(test_dots_1)
print(f"테스트 1 결과: {result_1}")  # 출력: 테스트 1 결과: 1

# 예시 2번 데이터 (평행하지 않은 경우 -> 결과: 0)
test_dots_2 = [[3, 5], [4, 1], [2, 4], [5, 10]]
result_2 = solution(test_dots_2)
print(f"테스트 2 결과: {result_2}")  # 출력: 테스트 2 결과: 0



# ***두 선이 평행할 조건(기울기 일치) -> (y2-y1)(x4-x3) = (y4-y3)(x2-x1)