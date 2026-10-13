# hyungchan_hw18.py

# 5
import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

print('-------------')
#6
import pandas as pd 

path = r"C:\rokey\py_work\ch18\hc_data.csv"
df_csv = pd.read_csv(path)
print(df_csv)

age = df_csv["Age"]
salary = df_csv["Salary"]
print(f"Age 평균: {age.mean()}, 최대값: {age.max()}, 최솟값: {age.min()}")
print(f"Salary 평균: {salary.mean()}, 최대값: {salary.max()}, 최솟값: {salary.min()}")

# # 솔루션
# for column in df_csv.columns[1:]: 
#     print(f"{column} 평균: {df_csv[column].mean()}, 최댓값: {df_csv[column].max()}, 최솟값: {df_csv[column].min()}")

print('-------------')
#7

mask = (df_csv["Age"] >= 30) & (df_csv["Salary"] >= 60000)
print(df_csv[mask])

print('-------------')
#8
import numpy as np 

arr = np.array(range(1,11))
# arr = np.arange(1, 11)

print(f"원본 배열: {arr}")
arr2 = arr ** 2
print(f"제곱 배열: {arr2}")
print(f"평균: {arr2.mean():.1f}, 최댓값: {arr2.max()}, 최솟값: {arr2.min()}")

print('-------------')
#9
import numpy as np

randint = np.random.randint(1,13,(3,4))
print(f"원본 행렬:\n{randint}")
max_arr = np.array([randint[0].max(), randint[1].max(), randint[2].max()])
print(f"각 행의 최댓값: {max_arr}")

# # 솔루션
# # 3x4 크기의 1~20 사이의 난수 행렬 생성
# np.random.seed(42)
# matrix = np.random.randint(1, 21, size=(3, 4))

# print("원본 행렬:")
# print(matrix)

# # 각 행의 최댓값 찾기
# row_max_values = np.max(matrix, axis=1)     # axis=0 : 각 열의 최대값, axis=1 : 각 행의 최대값
# print("각 행의 최댓값:", row_max_values)

print('-------------')
#10
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x,y)
plt.title("Ch18 HW #10 Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()

# # 솔루션
# # 그래프 그리기
# plt.plot(x, y, marker='o', linestyle='-', color='b')

# # 제목 및 축 라벨 추가
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# # 그리드 추가
# plt.grid(True)

# # 그래프 표시
# plt.show()


print('-------------')