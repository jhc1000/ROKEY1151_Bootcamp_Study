import pandas as pd

# df_csv = pd.read_csv(r"ch18/pandas/data1.csv")
# df = pd.DataFrame(df_csv)
# meanval = (df['Age'].mean())
# minnval = (df['Age'].min())
# maxval = (df['Age'].max())
# meanval1 = (df['Salary'].mean())
# minnval2 = (df['Salary'].min())
# maxval3 = (df['Salary'].max())
# print("Age 평균:",meanval,"최댓값:",maxval,"최솟값:",minnval)
# print("Salary 평균:",meanval1,"최댓값:",maxval3,"최솟값:",minnval2)

data = {
    'Name':['Yori','Bob','Alice','Dave'],
    'Age':[37,30,33,35],
    'Salary':[5800,6000,5500,7000]
}
df=pd.DataFrame(data)
filterd = df.loc[df['Salary']>=6000,['Name','Age','Salary']]
print(filterd)

# import numpy as np
# # arr = np.array([1,2,3,4,5,6,7,8,9,10])
# # multi = arr **2
# # tmean = np.mean(multi)
# # tmax = np.max(multi)
# # tmin = np.min(multi)
# # print("원본 배열:",arr)
# # print("제곱 배열:",multi)
# # print("평균:",tmean, "최댓값:",tmax,"최솟값:",tmin)

# nansu = np.random.randint(1,13,(3,4))
# row_max = np.max(nansu, axis=1)
# print(nansu)
# print("각 행의 최댓갑:",row_max)

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,3,6,8,10]
plt.plot(x,y,"-")
plt.grid(True)
plt.title("Grid Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()
