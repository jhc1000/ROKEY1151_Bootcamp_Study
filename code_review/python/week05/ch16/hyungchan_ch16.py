# hyungchan_ch16.py

# 문제 1. 은행 번호료 시스템
# 은행에서 고색 상담을 위해 번호표 대기 시스템
# 만들려고 합니다.
# (앞서 학습한 3가지 자료구조 중 하나를 선택할 것.)
# 번호표 -> 1 : 철수, 2: 영희, 3: 민수

# 큐 사용
# 온 순서를 리스트로 생성
# 먼저 온 사람 queue 에 enqueue
# 빠질 사람 queue 에서 dequeue
from queue_class import Queue

waiting_list = Queue()
waiting_list.enqueue("철수")
waiting_list.enqueue("영희")
waiting_list.enqueue("민수")
print(waiting_list.status_queue())
waiting_dict = {i+1 : name 
                for i, name 
                in zip(range(len(waiting_list.status_queue())),
                       waiting_list.status_queue()
                       )
                }
print(waiting_dict)
# waiting_list.dequeue()
# waiting_list.dequeue()
# waiting_list.dequeue()
# print(waiting_list.status_queue())

print('-----------')

from queue_class import Queue

bank = Queue()
bank.enqueue("철수")
bank.enqueue("영희")
bank.enqueue("민수")
print(bank.status_queue())
bank.dequeue()
bank.dequeue()
bank.dequeue()
print(bank.status_queue())

# 은행의 VIP 고객 우선처리한다 => deque

print('-----------')
# 문제 2. 브라우저 뒤로가기 시스템
# 웹 브라우저 방문 기록을 관리하는 프로그램을 작성하시요.
# (앞서 학습한 3가지 자료구조 중 하나를 선택할 것.)
# 이동 웹사이트 경로: "네이버" -> "유투브" -> "구글"
# 최근 방문 기록이 먼저 보여야하니 stack
from stack_class import Stack

website = Stack()
website.push("네이버")
website.push("유투브")
website.push("구글")
print(website.status_stack())
# 뒤로가기 버튼 클릭
print(website.pop())    # 이전 사이트
print(website.peak())   # 현재 위치 사이트
print(website.status_stack())

# 브라우저: 앞/뒤 이동 -> 덱
# 문서편집기: Undo/Redo -> 덱

print('-----------')
#1
# 괄호의 짝이 올바르게 사용되었는지 확인 
# 스택 활용 (괄호 종류는 소(), 중{}, 대[])
# pop을 해서 "(" 와 ")" 의 개수를 세고 
# 일치하면 True
# 불일치하면 False

str1 = "(a+b)"
str2 = "(a+b]}"
str3 = "[{(x+y)+3}-4]"
str4 = "[{x+y)+3}-4]"    
   
def check_brackets(string: str)->bool:
    left_bracket = ["(","{","["]
    right_bracket = [")","}","]"]
    left_bracket_num = [0,0,0]
    right_bracket_num = [0,0,0]
    str_list = [i for i in string]
    while str_list != []:
        current_str = str_list.pop()
        for i in range(len(left_bracket)):
            if current_str == left_bracket[i]:
                left_bracket_num[i] += 1
        for i in range(len(right_bracket)):
            if current_str == right_bracket[i]:
                right_bracket_num[i] += 1
    if left_bracket_num == right_bracket_num:
        return True
    return False

print(check_brackets(str1)) # True
print(check_brackets(str2)) # False
print(check_brackets(str3)) # True
print(check_brackets(str4)) # False

print('----------')
# 풀이
# 스텍 활용 이유: 늦게 나온 시작 괄호를 먼저 처리함
# 1. 빈 스택 생성
# 2. 문자열 내 문자를 가져온다.
# 3. 만약, 문자에 "여는", 괄호가 있다면, 스택에 push -> "( { ["
# 4. 만약, 문자에 "닫는", 괄호가 있다면, 스택에 pop
    # 4-1 만약, 스택이 비었다면 False
    # 4-2 pop 한 괄호를 확인하여 서로 일치하지 않으면 False
# 5. 문자열을 모두 확인했을 때, 스택이 비었다면 True

def check_brackets(string: str)->bool:
    # 1. 빈 스택 생성
    stack = []
    # 2. 문자열 내 문자를 가져온다.
    for char in string:
        # 3. 만약, 문자에 "여는", 괄호가 있다면, 스택에 push -> "( { ["
        if char in "({[":
            stack.append(char)
        # 4. 만약, 문자에 "닫는", 괄호가 있다면, 스택에 pop
        elif char in ")}]":
            print(f"char: {char}")
            # 4-1 만약, 스택이 비었다면 False
            if not stack: 
                return False
            # 4-2 pop 한 괄호를 확인하여 서로 일치하지 않으면 False
            top = stack.pop()
            print(f"top: {top}")
            if (char == ")" and top != "(") or \
                (char == "}" and top != "{") or \
                (char == "]" and top != "["):
                return False    # 짝 안맞음
        
    # 5. 문자열을 모두 확인했을 때, 스택이 비었다면 True
    print(f"stack: {stack}")
    return len(stack) == 0

print(check_brackets(str1)) # True
print(check_brackets(str2)) # False
print(check_brackets(str3)) # True
print(check_brackets(str4)) # False
print(check_brackets("()}")) # False
print(check_brackets("(({})")) # False
print('----------')

def check_brackets(string: str)->bool:
    # 1. 빈 스택 생성
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    # 2. 문자열 내 문자를 가져온다.
    for char in string:
        # 3. 만약, 문자에 "여는", 괄호가 있다면, 스택에 push -> "( { ["
        if char in "({[":
            stack.append(char)
        # 4. 만약, 문자에 "닫는", 괄호가 있다면, 스택에 pop
        elif char in pairs:
            # 4-1 만약, 스택이 비었다면 False
            # 4-2 pop 한 괄호를 확인하여 서로 일치하지 않으면 False
            if not stack or stack.pop() != pairs[char]: # stack 여는 괄호  비교  pairs 닫는괄호 키
                return False
    # 5. 문자열을 모두 확인했을 때, 스택이 비었다면 True
    return not stack

print(check_brackets(str1)) # True
print(check_brackets(str2)) # False
print(check_brackets(str3)) # True
print(check_brackets(str4)) # False

print('----------')
#2
# 회전 큐 구현
# 덱 사용
# 리스트로 구현
# 1. 초기 회전 큐 생성
# 2. append
# 3. appendleft
# 4. pop
# 5. popleft
# 6. is_empty
# 7. rotate
# 8. 상태 반환
from collections import deque

class RotateQueue:
    # 1. 초기 회전 큐 생성
    def __init__(self):
        self.rotatequeue = []
    # 2. append
    def append(self, data):
        return self.rotatequeue.append(data)
    # 3. appendleft
    def appendleft(self, data):
        temp_list = [data]
        temp_list.extend(self.rotatequeue)
        self.rotatequeue = temp_list
    # 4. pop
    def pop(self):
        if not self.is_empty():
            return self.rotatequeue.pop()
        return
    # 5. popleft
    def popleft(self):
        if not self.is_empty():
            return self.rotatequeue.pop(0)
        return
    # 6. is_empty
    def is_empty(self):
        if len(self.rotatequeue) == 0:
            return True
        return False
    # 7. rotate
    def rotate(self, num):
        if not self.is_empty():
            if num >= 0:
                for i in range(0, num):
                    temp = self.rotatequeue.pop()
                    temp_list = [temp]
                    temp_list.extend(self.rotatequeue)
                    self.rotatequeue = temp_list
            else: 
                for i in range(num, 0, -1):           
                    temp = self.rotatequeue.popleft()
                    self.rotatequeue.append(temp)
        return 
    # 8. 상태 반환        
    def status(self):
        return self.rotatequeue
rot1 = RotateQueue()
rot1.append(1)
rot1.appendleft(0)
rot1.append(2)
rot1.append(3)
rot1.append(4)
rot1.pop()
rot1.popleft()
print(rot1.status())
rot1.rotate(2)
print(rot1.status())