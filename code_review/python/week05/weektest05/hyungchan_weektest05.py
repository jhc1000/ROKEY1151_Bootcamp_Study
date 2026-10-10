# hyungchan_weektest05.py

print('----------')
#14-1

import re

data = """python one
life is too short
python two
you need python
python three"""

def find_python_sentence(data):
    pattern = r"^python.*"
    sentence_list = re.findall(pattern, data, re.M)
    return sentence_list
print(find_python_sentence(data))

print('----------')
#14-2
# 이메일 형식: user@example.com

import re

data = "user@example.com"

def evaluate_email_form(email):
    pattern = r"[\w]+@[\w]+\.[\w]+"
    m1 = re.match(pattern, email)
    return m1 is not None
print(evaluate_email_form(data))

print('----------')
#15-1

class ListIterator:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("리스트를 입력해야 합니다.") 
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

my_list = [1,2,3,4,5]
iterator = ListIterator(my_list)

for item in iterator:
    print(item)
    
print('----------')
#15-2

def generator(n):
    for i in range(1,n+1):
        yield (lambda x: x**2)(i)

gen1 = generator(5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

print('----------')
#16-1
class Stack:
    def __init__(self):
        self.stack=['두산', '로키', '부트']
        
    def push(self, data):
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

stack1 = Stack()
stack1.push('캠프')
print(stack1.status_stack())

print('----------')
#16-1

stack1.pop()
print(stack1.status_stack())

print('----------')