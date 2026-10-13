

# maplist = [
#     [0,1,1,1,1,1],
#     [0,1,0,0,0,1],
#     [0,1,0,1,0,1],
#     [0,1,0,1,0,0],
#     [0,0,0,1,1,0],
#     [1,1,1,1,1,0]
# ]

# for row in maplist:
#     print(row)

# lines = data.split("\n")

#dfs
# rows, cols = map(int, input().split())

# maplist = []

# for i in range(rows):
#     line = list(map(int, input()))
#     maplist.append(line)


# def mygraph(graph, start_row, start_col):

#     stack = [(start_row, start_col)]

#     visited = []

#     moves = [(-1,0),(1,0),(0,-1),(0,1)]

#     while stack:
#         r, c = stack.pop()

#         if (r,c) not in visited:
#             visited.append((r,c))

#             for dr, dc in moves:
#                 nr = r + dr
#                 nc = c + dc
#                 if 0 <= nr <rows and 0 <= nc <cols and graph[nr][nc] == 1:
#                     stack.append((nr,nc))
#     return visited

# print(mygraph(maplist,0,0))



#bfs
rows, cols = map(int, input().split())

maplist = []

for i in range(rows):
    line = list(map(int, input()))
    maplist.append(line)


def mygraph(graph, start_row, start_col):

    queue = [(start_row, start_col)]

    visited = []

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        r, c = queue.pop(0)

        if (r,c) not in visited:
            visited.append((r,c))

            for dr, dc in moves:
                nr = r + dr
                nc = c + dc
                if 0 <= nr <rows and 0 <= nc <cols and graph[nr][nc] == 1:
                    queue.append((nr,nc))
    return visited

print(mygraph(maplist,0,0))