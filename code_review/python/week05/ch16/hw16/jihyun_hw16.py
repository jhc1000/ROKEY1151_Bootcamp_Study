# stack = []
# def push(x):
#     stack.append(x)

# def pop():
#     if len(stack)==0:
#         return -1
#     return stack.pop()

# def top():
#     if len(stack) == 0:
#         return -1
#     return stack[-1]

# def is_empty():
#     return len(stack) == 0
# push(3)
# push(5)
# print(top())
# print(pop())
# print(pop())
# print(is_empty())
# print(pop())
# print(top())

# def calcul(expression):
#     stack = []
#     for bucket in expression.split():
#         if bucket in ["+","-","*","/"]:
#             b = stack.pop()
#             a = stack.pop()

#             if bucket == "+":
#                 stack.append(a + b)
#             elif bucket == "-":
#                 stack.append(a - b)
#             elif bucket == "*":
#                 stack.append(a * b)
#             else:
#                 stack.append(a / b)
#         else:
#             stack.append(int(bucket))
#     return stack.pop()
# print(calcul("3 4 + 2 *"))

# queue = []
# def enqueue(x):
#     queue.append(x)
# def dequeue():
#     if len(queue) == 0:
#         return -1
#     return queue.pop(0)
# def front():
#     if len(queue)== 0:
#         return -1
#     return queue[0]
# def is_empty():
#     return len(queue)==0

# enqueue(3)
# enqueue(5)
# print(front())
# print(dequeue())
# print(dequeue())
# print(is_empty())
# print(dequeue())
# print(front())

# from queue_class import Queue
# bank = Queue()
# bank.enqueue("김철수")
# bank.enqueue("이영희")
# bank.enqueue("박민수")
# print("현재 대기열:",bank.status_queue())

# print("업무 처리 중인 고객 :",bank.dequeue())
# print("남은 대기 고객:",bank.status_queue())

deque = []
def push_front(x):
    deque.insert(0,x)
def push_back(x):
    deque.append(x)
def pop_front():
    if len(deque) == 0:
        return -1
    return deque.pop(0)
def pop_back():
    if len(deque) == 0:
        return -1
    return deque.pop()

push_back(1)
push_back(2)
push_front(7)
print(deque)
print(pop_front())
print(pop_back())
print(pop_back())
print(pop_front())
