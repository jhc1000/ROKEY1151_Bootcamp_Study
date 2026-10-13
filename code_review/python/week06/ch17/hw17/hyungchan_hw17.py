# hyungchan_ch17.py

#2

from dfs import my_dfs

map = {
    'A': ['C','B'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['C', 'B']
}

print(my_dfs(map, 'A'))
# ['A', 'C', 'D', 'B']
print('----------')

#6

maze = [[0,1,1,1,1,1],
        [0,1,0,0,0,1],
        [0,1,0,1,0,1],
        [0,1,0,1,0,0],
        [0,0,0,1,1,0],
        [1,1,1,1,1,0]]

print('----------')

#7

for m in maze:
    print(m)
    
print('----------')

#8

# row, col, data

# def make_maze(row, col):
#     maze = list()
#     for r in range(row):
#         m = list()
#         for c in range(col):
#             n = int(input(f"({r},{c}) 데이터 입력:"))
#             m.append(n)
#         maze.append(m)
#     return maze

# row = int(input("세로(행) 개수 입력:"))
# col = int(input("가로(열) 개수 입력:"))

# maze = make_maze(row, col)

# for m in maze:
#     print(m)


print('----------')

#8 솔루션
# r = int(input("세로(행): "))
# c = int(input("가로(열): "))

# my_map = []
# for _ in range(r):
#     row = list(map(int, input().split()))
#     my_map.append(row)

# for row in my_map:
#     print(row)

print('----------')

#9 

def boundary(maze, point):
    if (0<= point[0] < len(maze)) and (0<= point[1] < len(maze[0])):
        return True
    return False

def maze_dfs(maze, start):
    stack = list()
    visited = list()
    stack.append(start)
    while stack:
        r,c = stack.pop()
        if (r,c) not in visited:
            next_step = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr, dc in next_step:
                nr, nc = r+dr, c+dc
                if boundary(maze, (nr,nc)) and maze[nr][nc] == 0:
                    stack.append((nr,nc))
            visited.append((r,c))
    return visited

start_point = (0,0)
print(maze_dfs(maze, start_point))

print('----------')

#10

def boundary(maze, point):
    if (0<= point[0] < len(maze)) and (0<= point[1] < len(maze[0])):
        return True
    return False

def maze_bfs(maze, start):
    queue = list()
    visited = list()
    queue.append(start)
    while queue:
        r,c = queue.pop(0)
        if (r,c) not in visited:
            next_step = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr, dc in next_step:
                nr, nc = r+dr, c+dc
                if boundary(maze, (nr,nc)) and maze[nr][nc] == 0:
                    queue.append((nr,nc))
            visited.append((r,c))
    return visited

start_point = (0,0)
print(maze_bfs(maze, start_point))

print('----------')