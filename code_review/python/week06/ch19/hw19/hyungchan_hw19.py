# hyungchan_hw19.py

print('-----------')
#6
import statsmodels.api as sm
import pandas as pd

data = {
    'x':[1, 2, 3, 4, 5],
    'y':[2, 4, 6, 8, 10]
}

df = pd.DataFrame(data)

X = df['x']
y = df['y']

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.summary())

W = model.params['x']
B = model.params['const']
print(f"기울기: {W}")
print(f"절편: {B}")

print('-----------')

#7

# import matplotlib.pyplot as plt

# x = df['x']
# y = df['y']

# H = lambda x: W * x + B

# plt.scatter(x, y, color="blue")
# plt.plot([min(x), max(x)], [H(min(x)), H(max(x))], c='r')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("Linear Regression")
# plt.show()

print('-----------')

#8

from sklearn import svm
from sklearn import metrics

# 데이터 / 레이블 
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# 알고리즘 선택
clf = svm.SVC()
# 학습
clf.fit(X, y)

# 예측
pre = clf.predict([[4.5], [6.5]])
print(pre)

print('-----------')

#9 

from scipy.optimize import root 

# 함수 선언
def equation(x):
    return (x-3)**2 

sol = root(equation, x0=1)
print(f"Root: {sol.x}")

print('-----------')

# 10
from scipy.stats import describe

A =  [80, 85, 90, 75, 95]
stats = describe(A)
print(stats)

print('-----------')