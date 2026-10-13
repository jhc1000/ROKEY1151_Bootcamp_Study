
#연습문제 1번

g1 = {1: [2, 3, 4], 2: [1, 5], 3: [1, 6], 4: [1, 6], 5: [2, 6], 6: [3, 4, 5]}

def dfs(graph, start_node):
    stack = list()
    visited = list()
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    print("dfs - ", visited)
    return visited

def bfs(graph, start_node):
    queue = list()
    visited = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    print("bfs - ", visited)
    return visited

dfs(g1, 1)
bfs(g1, 1)

#2번 맵 0,1로 표현

map5 = [
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
]

for row in map5:
    print(row)



#3번, 로봇 (0,0)->(5,5)
graph = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
]
n, m = len(graph), len(graph[0])

dx = [-1, 1, 0, 0]      # 상, 하, 좌, 우 ->개별로 나눠도 무관
dy = [0, 0, -1, 1]

def robot_dfs(graph, start, goal):
    stack = [start]
    visited = []
    parent = {start: None}          # 어느 칸에서 왔는지 기록 (경로 복원용)

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.append((x, y))
        if (x, y) == goal:          # 출구에 도착하면 종료
            break
        for i in reversed(range(4)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))
                parent.setdefault((nx, ny), (x, y))

    # 출구에서 입구까지 거꾸로 따라가며 경로 만들기
    path = []
    cur = goal if goal in visited else None
    while cur:
        path.append(cur)
        cur = parent[cur]
    return visited, path[::-1]

visited, path = robot_dfs(graph, (0, 0), (5, 5))
print("탐색 순서:", visited)
print("출구 도착:", (5, 5) in visited)
print("경로:", path)