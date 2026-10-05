# hw13.py

# 프로그래머스 차시별 과제 풀이를 여기에 적으시면 됩니다.

#2
try:
    x = int("abc")
except ValueError:
    print("ValueError occurred!")
finally:
    print("Execution finished.")

# ValueError occurred!
# Execution finished.
print('-------')

#6

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

print('-------')


#7

try:
    raise KeyError("Key is missing!")
except KeyError as e:
    print(e)
    
print('-------')

#8
    
add = lambda x,y: x+y
print(add(3,5))

print('-------')

#9

per = ["10.31", "", "8.00"]
for i in per:
    try:
        print(float(i))
    except ValueError:
        print(0)

print('-------')

#10

numbers = [10, 20, 30]
try:
    index = int(input("인덱스를 입력:"))
    print(numbers[index])
except IndexError:
    print("잘못된 인덱스입니다.")
except ValueError:
    print("정수를 입력하세요")
    
print('-------')
