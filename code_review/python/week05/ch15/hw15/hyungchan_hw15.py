# hyungchan_hw15.py

#2
nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))

# 1
# 2
print('--------')

#3
def my_gen():
    yield 1
    yield 2
    yield 3
gen = my_gen()
print(next(gen))
print(next(gen))
# 1
# 2
print('--------')

#4
gen_a = (x * 2 for x in range(5))
for i in gen_a:
    print(i)
    
print('--------')

#5
def countdown(n):
    while n > 0:
        yield n
        n -= 1
gen = countdown(3)
for x in gen:
    print(x, end=" ")

# 3 2 1 
print('\n--------')

#6
numbers = [1, 2, 3, 4, 5]
iter_nums = iter(numbers)
for i in iter_nums:
    print(i)

print('--------')

#7

fruits = ["apple", "banana", "cherry"]
iter_fruits = iter(fruits)
while True:
    try:
        print(next(iter_fruits))
    except StopIteration:
        break

print('--------')

#8

def generator(number):
    for i in range(0, number+1):
        yield i**2
    
gen1 = generator(9)
for i in gen1:
    print(i)
    
print('--------')

#9

gen1 = (i for i in range(11) if i % 2 == 0)
for i in gen1:
    print(i)
    
print('--------')

# 10

class MyRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.position = self.start - self.step
    def __iter__(self):
        return self
    def __next__(self):
        self.position += self.step
        if self.position > self.stop:
            raise StopIteration
        return self.position
    
myrange = MyRange(0, 20, 3)
for i in myrange:
    print(i)

print('--------')