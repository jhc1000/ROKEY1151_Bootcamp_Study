# hyungchan_hw20.py

print('-----------')
#6
# import seaborn as sns 
# import matplotlib.pyplot as plt 
# import numpy as np 

# # 데이터셋 로트
# data = np.random.normal(50, 10, 1000)

# # 기본 스타일 설정
# sns.set_theme(style="whitegrid")

# # 그래프 표시
# sns.histplot(data, kde=True)
# plt.title("Normal Distributed Data")
# plt.show()

print('-----------')
#7

# import seaborn as sns 
# import matplotlib.pyplot as plt  
# import pandas as pd 

# tips = sns.load_dataset("tips")
# print(tips.head())
# #    total_bill   tip     sex smoker  day    time  size
# # 0       16.99  1.01  Female     No  Sun  Dinner     2
# # 1       10.34  1.66    Male     No  Sun  Dinner     3
# # 2       21.01  3.50    Male     No  Sun  Dinner     3
# # 3       23.68  3.31    Male     No  Sun  Dinner     2
# # 4       24.59  3.61  Female     No  Sun  Dinner     4

# sns.boxplot(data=tips, 
#             x="day", 
#             y="total_bill")
# plt.show()

print('-----------')
#8
# import cv2 

# # 이미지 로드
# image = cv2.imread(r".\ch20\opencv\sample.jpg")

# # 이미지 출력
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print('-----------')
#9
# import cv2 

# # 이미지 로드
# image = cv2.imread(r".\ch20\opencv\sample.jpg")

# # 그레이스케일로 변경
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # 이미지 출력
# cv2.imshow("Gray Image", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print('-----------')
#10

import cv2

# 이미지 로드
image = cv2.imread(r".\ch20\opencv\sample.jpg")

# 엣지 검출
edges = cv2.Canny(image, 100, 200)

# 이미지 출력
cv2.imshow("Edge Image",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('-----------')