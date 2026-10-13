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