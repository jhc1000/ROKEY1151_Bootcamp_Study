# hyungchan_ch17.py

print('-------------')
#1
"""다음 그래프를 만들고 깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS)을
위한 프로그램을 각각 작성하시오."""

# graph1 = {
#     1: [2, 3, 4],
#     2: [1, 5],
#     3: [1, 6],
#     4: [1, 6],
#     5: [2, 6],
#     6: [5, 3, 4],
# }
from graph1 import graph1

def dfs1(graph, start_node):
    stack = list()
    visited = list()
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            stack.extend(reversed(graph[node]))
            visited.append(node)
    return visited

def bfs1(graph, start_node):
    queue = list()
    visited = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)
    return visited

print(f"dfs - {dfs1(graph1, 3)}")
print(f"bfs - {bfs1(graph1, 3)}")

print('-----------')

#2

map = [
    [0,0,1,0,1],
    [1,0,1,0,0],
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,0,0,1,1]
]

print(map[0][2])
print(map[1][2])
print(map[2][2])
print(map[3][2])
print(map[4][2])
print(len(map))
print(len(map[0]))

print('-----------')

#3

# 끝까지 가본다 = dfs
# 갈 예정인 위치 스택 초기화
# 가본 위치 리스트 초기화
# (0,0) 에서 시작 -> 시작위치 스택에 저장
# 다음 위치를 스택에서 pop
# 로봇의 4 방향의 값을 확인
# 만약, 가본적이 없는 곳이면
# 만약, 0 이면 진행가능 -> 스택에 저장
# 만약, 1 이면 진행불가능
# 진행한 곳 리스트에 저장
# stack 이 없을때까지 반복
# 맵 경계를 고려

from map1 import map1, map2

# 맵 경계를 고려
def boundary(map, point):
    if 0 <= point[0] < len(map) and 0 <= point[1] < len(map[0]):
        return True
    return False

def robot_find_exit(map, start_point):
    # 갈 예정인 위치 스택 초기화
    stack = list()
    # 가본 위치 리스트 초기화
    visited = list()
    # (0,0) 에서 시작 -> 시작위치 스택에 저장
    stack.append(start_point)
    # stack 이 없을때까지 반복
    while stack:
        # print(f"stack - {stack}")
        # print(f"visited - {visited}")
        # 다음 위치를 스택에서 pop
        point = stack.pop()
        # 로봇의 4 방향의 값을 확인
        moving_direction = [[1,0],[-1,0],[0,1],[0,-1]]
        next_points = [[point[0]+x,point[1]+y] for [x,y] in moving_direction if boundary(map, [point[0]+x,point[1]+y])]
        for next_point in next_points:
            # 만약, 가본적이 없는 곳이면
            # 만약, 0 이면 진행가능 -> 스택에 저장
            if (next_point not in visited) and (map[next_point[0]][next_point[1]] == 0):
                stack.append(next_point)
        # 진행한 곳 리스트에 저장
        visited.append(point)
    return visited

start_point = [0,0]
print(f"visited point - {robot_find_exit(map1, start_point)}")
print(f"last point - {robot_find_exit(map1, start_point)[-1]}")

# print(f"visited point - {robot_find_exit(map, start_point)}")

# print(f"last point - {robot_find_exit(map, start_point)[-1]}")

print(f"visited point - {robot_find_exit(map2, start_point)}")

print(f"last point - {robot_find_exit(map2, start_point)[-1]}")

# moving_direction = [[1,0],[-1,0],[0,1],[0,-1]]
# next_points = [[start_point[0]+x,start_point[1]+y] for [x,y] in moving_direction]
# print(next_points)

print('-----------')

#3 솔루션
# 탐색 방법: DFS
# 활용 자료구조: 스택

# 미로 데이터(2차원 리스트)

def solve_maze(maze, start):
    # 1. 탐색할 노드를 담을 스택
    stack = list()
    # 2. 방문 여부 확인 리스트
    visited = list()
    # 3. 탐색 시작 노드
    stack.append(start)
    # 6. 4-5번 과정 반복
    while stack:
        # 4. 방문할 노드를 스택에서 제거
        r, c = stack.pop()

        # 5. 방문 리스트에 스택에서 꺼낸 노드가 없으면,
        if (r,c) not in visited:
            #   - 방문처리
            visited.append((r,c))
            # maze[r][c] == 2 # 좌표에 대한 방문 처리
            
            #   - 인접노드를 스택에 추가
            # 이동: 상 하 좌 우 (미로 범위 내, 길(0)인 경우만)
            # [상, 하, 좌, 우] == [(-1,0), (1,0), (0, -1), (0,1)]
            for dr,dc in [(-1,0), (1,0), (0, -1), (0,1)]:
                # nr = r+dr   # 행 변화
                # nc = c+dc   # 열 변화
                nr, nc = r+dr, c+dc
                # if 0<= nr <len(maze) and 0<= nc <len(maze[0]) and maze[nr][nc] == 0: 
                if 0<= nr <6 and 0<= nc <6 and maze[nr][nc] == 0: 
                    stack.append((nr,nc))
    return visited

print(solve_maze(map1, (0,0)))

## 좌표 이동 방법 : (행,열)
# 위 이동: (0,0) -> (-1,0)
# 아래 이동: (0,0) -> (1,0)
# 왼쪽 이동: (0,0) -> (0, -1)
# 오른쪽 이동: (0,0) -> (0,1)

## 노드-엣지 표현 형태
# 길-벽, 길-길 이 상하좌우 로 있다

## 이동 가능 범위 지정
# 범위: 0 <= 열 < 6, 0 <= 행 < 6

# 패딩처리 : 8x8 로 해서 1로 다 채우고 (1,1)
print('-----------')