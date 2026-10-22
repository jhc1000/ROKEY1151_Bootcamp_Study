#코딩 테스트 정보 Lv2 정답률 50%, 2025 프로그래머스 코드챌린지 2차 예선
# 
# 
# #https://school.programmers.co.kr/learn/courses/30/lessons/389479




#개선된 버전의 풀이

from collections import deque



def solution(players, m, k):
    queue=deque()
    running  = 0
    answer = 0
    
    for hour,p in enumerate(players):
        while queue and queue[0][0] <= hour:
            running -= queue.popleft()[1]
        add = p // m - running
        if add>0:
            queue.append((hour +k, add))
            running += add
            answer += add
    return answer



"""
처음 생각한 시간마다 계산해서 하는 형식

def add_servers(servers, count, end_time):  # 서버를 count대 증설하는 함수
    for _ in range(count):  # 증설해야 하는 대수만큼 반복
        servers.append(end_time)  # 각 서버의 반납 시각을 리스트에 기록
    return count  # 이번에 증설한 횟수를 돌려줌
 
 
def solution1(players, m, k):  
    servers = []  # 운영 중인 서버들의 반납 시각 목록
    answer = 0  # 총 증설 횟수
    for hour in range(24):  # 0시부터 23시까지 한 시간씩 확인
        servers = [t for t in servers if t > hour]  # 반납 시각이 지난 서버는 제거
        need = players[hour] // m  # 이 시간대에 필요한 최소 서버 수
        if len(servers) < need:  # 운영 중인 서버가 부족하다면
            answer += add_servers(servers, need - len(servers), hour + k)  # 부족한 만큼 함수로 증설하고 횟수 누적
    return answer  # 총 증설 횟수 반환




"""



"""" 
개선된 버전의 풀이에 대한 주석및 설명
def solution(players, m, k):  # 방식 4의 메인 함수
    queue = deque()  # (반납 시각, 서버 대수)를 증설 순서대로 저장하는 큐
    running = 0  # 현재 운영 중인 서버 수
    answer = 0  # 총 증설 횟수
    for hour, p in enumerate(players):  # 시간과 이용자 수를 함께 꺼냄
        while queue and queue[0][0] <= hour:  # 맨 앞 서버 묶음의 반납 시각이 됐다면
            running -= queue.popleft()[1]  # 큐에서 꺼내고 그만큼 운영 수 감소
        add = p // m - running  # 필요한 서버 수와 현재 서버 수의 차이
        if add > 0:  # 부족할 때만
            queue.append((hour + k, add))  # 반납 시각과 대수를 큐 뒤에 추가
            running += add  # 운영 중인 서버 수 증가
            answer += add  # 총 증설 횟수 누적
    return answer  # 결과 반환
"""