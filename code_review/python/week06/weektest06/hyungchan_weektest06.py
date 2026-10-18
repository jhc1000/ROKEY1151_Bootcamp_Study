# hyungchan_weektest06.py

print('-----------')
#17-1

graph = {
    '두':['산','로','키'],
    '산':['두','부'],
    '로':['두'],
    '키':['두','트'],
    '부':['산'],
    '트':['키','캠','프'],
    '캠':['트'],
    '프':['트']
}

# def dfs(graph, start_node):
#     # 방문할 노드 저장 스택
#     stack = list()
#     # 방문한 노드 저장 리스트
#     visited = list()
#     # 시작노드 스택에 저장
#     stack.append(start_node)
#     # stack 빌때까지 반복
#     while stack:
#         # 스택에서 노드 pop 
#         node = stack.pop()
#         # 만약 방문 안했던곳이면
#         if node not in visited:
#             # 인접 노트 스택에 저장
#             stack.extend(reversed(graph[node]))
#             # 방문한 노드 리스트에 저장
#             visited.append(node)
#     return visited

# start_node = "두"
# print(dfs(graph, start_node))

print('-----------')
#17-2 

# def bfs(graph, start_node):
#     # 방문할 노드 저장 큐 
#     queue = list()
#     # 방문한 노드 저장 리스트
#     visited = list()
#     # 시작노드 큐에 저장
#     queue.append(start_node)
#     # queue 빌때까지 반복
#     while queue:
#         # 큐에서 노드 dequeue 
#         node = queue.pop(0)
#         # 만약 방문 안했던곳이면
#         if node not in visited:
#             # 인접 노트 큐에 저장
#             queue.extend(graph[node])
#             # 방문한 노드 리스트에 저장
#             visited.append(node)
#     return visited

# print(bfs(graph, start_node))

print('-----------')
#18-1
# import pandas as pd 

# path = r"ch21\weektest06\대구광역시 동구_연도별 체납차량 번호판 영치실적_20251031.csv"
# df = pd.read_csv(path, encoding='cp949')
# print(type(df)) # <class 'pandas.DataFrame'>
# print(df.head())
# #      년도  영치대수  체납건수  체납금액(백만원)
# # 0  2025  1307  4342        650
# # 1  2024  1143  3790        560
# # 2  2023  1196  3944        605
# # 3  2022  1058  3253        582
# # 4  2021   879  2845        484

print('-----------')
#18-2
# import matplotlib.pyplot as plt 

# # 한글 폰트 설정
# plt.rcParams["font.family"] = "Malgun Gothic"

# mask = df['년도'] != 2025
# filtered = df.loc[mask, ['년도','영치대수']]
# print(filtered)

# x = filtered['년도']
# y = filtered['영치대수']

# plt.plot(x, y, "r-")
# plt.xlabel('년도')
# plt.ylabel('영치대수')
# plt.title('대구광역시 동구_연도별 체납차량 번호판 영치실적')
# plt.show()

print('-----------')
#19-1

# import statsmodels.api as sm 
# import numpy as np 
# # 데이터 로드
# X = np.array([1,2,3,4,5])
# y = np.array([2,4,5,4,5])
# # 상수항 추가
# X = sm.add_constant(X)
# # 모델 생성 및 학습
# model = sm.OLS(y,X).fit()

# # 모델 요약
# print(model.summary())

# # W,B 출력 
# W = model.params[1]
# B = model.params[0]

# print(f"기울기 (coef): {W}")

print('-----------')
#19-2
# from scipy.optimize import root
# def equation(x):
#     return x**2 + 6*x + 9

# sol = root(equation, x0=0)
# print(sol.x)

print('-----------')
#20-1
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# iris = sns.load_dataset("iris")
# sns.boxplot(data=iris,
#             x="species",
#             y="sepal_length")
# plt.title("Box Plot Example")
# plt.show()

print('-----------')
#20-2
import cv2

# 이미지 로드
image = cv2.imread(r".\ch20\opencv\sample.jpg")

# 그레이스케일 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 출력
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('-----------')
#21-1

import os 

folder_path = os.getcwd()

file_path = os.path.join(folder_path, r"ch21\weektest06\os_ex1.ini")

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
        

print('-----------')
#21-4

import requests 

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("상태 코드:", response.status_code)

data = response.json()

print("게시글 ID:", data["id"])
print("제목 :", data["title"])
print("내용 :", data["body"])