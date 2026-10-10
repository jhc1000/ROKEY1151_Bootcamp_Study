# hyungchan_hw16.py

"""
6. 리스트를 이용하여 기본적인 스택(stack)을 구현하세요. (다음 내용을 고려할 것.)
push(x): 정수 x를 스택에 삽입
pop(): 스택에서 가장 위의 값을 제거하고 반환. 만약 스택이 비어 있다면 -1을 반환
top(): 스택의 가장 위에 있는 값을 반환. 만약 스택이 비어 있다면 -1을 반환
is_empty(): 스택이 비어 있으면 True, 아니면 False를 반환
"""

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        return self.stack.append(data)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return -1
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return -1
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.pop())
print(s1.top())
print(s1.is_empty())
print(s1.pop())
print(s1.pop())
print(s1.top())
print(s1.is_empty())

print('---------')
"""
7. 후위 표기법(Postfix Notation, Reverse Polish Notation)으로 주어진 수식을 계산하는 프로그램을 작성하세요.
후위 표기법에서는 연산자가 피연산자 뒤에 위치합니다. 예를 들어, 3 4 +는 3 + 4를 의미하며, 결과는 7입니다.
연산자는 +, -, *, /만 고려합니다. (복수 연산자도 처리 가능해야 함.)
"""
# 1. 문자열에서 공백을 기준으로 쪼개서 각각의 토큰을 리스트로 만듭니다.
# 2. 스택 준비해서 리스트를 왼쪽에서 하나씩 확인합니다.
# 3. 만약, 숫자면 int 로 전환해서 스택에 push [3, 4]
# 4. 연산자면 스택에서 2개 pop -> 1번pop: 4, 2번pop: 3
# 5. 연산 후 다시 스택에 넣기
import re
def calculate_postfix(string: str)->float:
    stack = []
    # 1. 문자열에서 공백을 기준으로 쪼개서 각각의 토큰을 리스트로 만듭니다.
    string_list = string.split()
    # print(f"string_list: {string_list}")
    # 2. 스택 준비해서 리스트를 왼쪽에서 하나씩 확인합니다.
    for char in string_list:
        # 3. 만약, 숫자면 int 로 전환해서 스택에 push [3, 4]
        number = re.match(r"\d+", char)
        if number is not None: 
            # print(f"number: {number}")
            stack.append(float(number.group()))
        # 4. 연산자일때
        else: 
            # print(char)
            # 4. 연산자면 스택에서 2개 pop -> 1번pop: 4, 2번pop: 3
            b = stack.pop()
            a = stack.pop()
            if char == "+":
                stack.append(a + b)
            elif char == "-":
                stack.append(a - b)
            elif char == "*":
                stack.append(a * b)
            elif char == "/":
                try: 
                    stack.append(a / b)
                except ZeroDivisionError:
                    print("0으로 나눌수 없습니다.")
                    return None                    
            # 5. 연산 후 다시 스택에 넣기
    return stack[0]

str1 = "3 4 +"                  # 3 + 4
str2 = "5 1 2 + 4 * + 3 -"      # (1 + 2) * 4 + 5 - 3  
str3 = "5 1 1 - /"
print(calculate_postfix(str1))  # 7.0
print(calculate_postfix(str2))  # 14.0
print(calculate_postfix(str3))  # None

print('---------')
#8 
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        return self.queue.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return -1
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return -1
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

q1 = Queue()
print(q1.front())
print(q1.dequeue())
print(q1.enqueue(1))
print(q1.enqueue(2))
print(q1.enqueue(3))
print(q1.dequeue())
print(q1.front())

print('---------')

#9
"""
조건: (FIFO)
1. 고객이 도착하면 이름을 큐에 추가합니다 (Enqueue). 
2. 업무 처리가 시작되면 가장 먼저 온 고객부터 이름을 출력하고 큐에서 제거합니다 (Dequeue). 
3. 현재 대기 중인 고객 명단을 확인하는 기능을 포함하세요.
"""
# 1. 큐 초기화
# 2. Enqueue
# 3. Dequeue
# 4. is_empty
# 5. status 
class Bank(Queue):
    def staus(self):
        return self.queue
    
bank_waiting = Bank()
bank_waiting.enqueue('김철수')
bank_waiting.enqueue('이영희')
bank_waiting.enqueue('박민수')
print(bank_waiting.staus())
bank_waiting.dequeue()
print(bank_waiting.staus())

print('---------')

#10

class Deque:
    def __init__(self):
        self.deque = []
    def push_front(self, data):
        temp_list = [data]
        temp_list.extend(self.deque)
        self.deque = temp_list
    def push_back(self, data):
        self.deque.append(data)
    def pop_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        return -1
    def pop_back(self):
        if not self.is_empty():
            return self.deque.pop(-1)
        return -1
    def is_empty(self):
        if len(self.deque) == 0:
            return True
        return False
    
dq1 = Deque()
dq1.push_back(1)
dq1.push_back(2)
dq1.push_front(0)
print(dq1.deque)
dq1.pop_back()
dq1.pop_front()
print(dq1.deque)

print('---------')