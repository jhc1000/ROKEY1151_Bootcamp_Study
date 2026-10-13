
# import re
# data = """python one
# life is too short
# python two
# you need python
# python there"""
# p=re.compile("python")
# result = p.findall(data)
# print(result)

# import re

# text=input("이메일을 입력하세요: ")
# pattern = r"[\w.-]+@[\w.-]+\.\w+"
# if re.fullmatch(pattern, text):
#     print("올바른 이메일 형식입니다.")
# else:
#     print("올바르지 않은 이메일 형식입니다.")
# emails = re.findall(pattern, text)
# print(emails)


# def mygen():
#     for i in range(1,10):
#         result = i * i
#         yield result
# gen = mygen()
# print(next(gen))
# for item in gen:
#     print(item)
# print(next(gen, "끝"))

class Stack:
    def __init__(self):
        self.stack = ['두산','로키','부트']
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return
    def is_empty(self):
        return len(self.stack) == 0
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return
    def status_stack(self):
        return self.stack

s = Stack()
s.push('캠프')
print(s.pop())
print(s.status_stack())