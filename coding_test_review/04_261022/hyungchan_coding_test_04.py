# hyungchan_coding_test_04.py

"""
코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 
지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.
"""



## 푼 코드를 적어주세요
# 끝까지 가는 최솟값을 구하기 : BFS (너비우선탐색)
# queue를 이용
# visited 리스트에 방문한 위치 저장
# 시작노드 (0,0)
# queue 에 시작노드 저장
# stack 이 빌때까지 while:
# node를 queue 에서 dequeue
# 만약 node 가 visited에 없다면
# visited 에 저장
# 방향에 따른 다음 노드 계산
# 만약 1. 해당 노드 가 0이거나 2. 범위 밖이 아니면
# queue에 다음 노드 저장
# 1스탭 지날때마다 answer +1 
# (다음 노드들을 step 리스트에 저장후 step 리스트를 queue에 저장) 
# (step 이 빈 리스트면 queue에 저장 x)
# 만약 node 가 마지막 지역이면 return answer
# return -1
def boundary(maps, point):
    if (0<= point[0] <len(maps)) and (0<= point[1] <len(maps[0])):
        return True
    return False

def solution1(maps):
    answer = 0
    # 시작노드 (0,0)
    start = (0,0)
    end = (len(maps)-1, len(maps[0])-1)
    # queue를 이용
    queue = list()
    # visited 리스트에 방문한 위치 저장
    visited = list()
    # queue 에 시작노드 저장
    queue.append([start])
    # stack 이 빌때까지 while:
    while queue:
        # node를 queue 에서 dequeue
        nodes = queue.pop(0)
        # 1스탭 지날때마다 answer +1 
        # (다음 노드들을 step 리스트에 저장후 step 리스트를 queue에 저장) 
        # (step 이 빈 리스트면 queue에 저장 x)
        answer += 1
        step = list()
        for node in nodes:
            r = node[0]
            c = node[1]
            # 만약 node 가 visited에 없다면
            if node not in visited:
                # visited 에 저장
                visited.append(node)
                # 만약 node 가 마지막 지역이면 return answer
                if node == end:
                    return answer
                direction = [(1,0), (0,1), (-1,0), (0,-1)]
                for (dr,dc) in direction:
                    nr = r+dr
                    nc = c+dc
                    # 만약 1. 해당 노드 가 0이거나 2. 범위 밖이 아니면
                    if not boundary(maps, (nr,nc)) or (maps[nr][nc] == 0):
                        continue
                    else:
                        step.append((nr,nc)) 
        if step:
            queue.append(step)
    return -1



## 그밖에 해당 코드 관련 알면 좋을 내용을 적어주세요.

# 최단거리 계산 (다음 방문 노드 map값은 이전 노드 map값에서 +1)

def boundary(maps, point):
    if (0<= point[0] <len(maps)) and (0<= point[1] <len(maps[0])):
        return True
    return False

def solution2(maps):
    start = (0,0)
    end = (len(maps)-1, len(maps[0])-1)
    queue = list()
    visited = list()
    queue.append(start)
    while queue:
        node = queue.pop(0)
        r = node[0]
        c = node[1]
        if node not in visited:
            visited.append(node) 
            if node == end:
                return maps[r][c]
            direction = [(1,0), (0,1), (-1,0), (0,-1)]
            for (dr,dc) in direction:
                nr = r+dr
                nc = c+dc
                if not boundary(maps, (nr,nc)) or (maps[nr][nc] == 0):
                    continue
                else:
                    # 최단거리 계산 (다음 방문 노드 map값은 이전 노드 map값에서 +1)
                    queue.append((nr,nc)) 
                    maps[nr][nc] = maps[r][c] + 1
    return -1


# 타 솔루션
from collections import deque

def solution3(maps):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]

    x_h, y_h = (len(maps[0]), len(maps))
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]

            if nx > -1 and ny > -1 and nx < x_h and ny < y_h:
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:
                    maps[ny][nx] = d + 1
                    if nx == x_h - 1 and ny == y_h - 1:
                        return d + 1

                    queue.append((nx, ny, d + 1))

    return -1

if __name__=="__main__":
    maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    answer1 = 11
    
    maps2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    answer2 = -1
    
    # result1 = solution1(maps1)
    # result2 = solution1(maps2)
    
    # result1 = solution2(maps1)
    # result2 = solution2(maps2)
        
    result1 = solution3(maps1)
    result2 = solution3(maps2)
    print(f"테스트1: {result1==answer1}")
    print(f"테스트2: {result2==answer2}")