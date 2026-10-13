# numbers = [1,2,3,4,5]
# iterator = iter(numbers)
# for j in numbers:
#     print(j)


# fruits = ["apple", "banana", "cherry"]
# iter_f = iter(fruits)
# while True:
#     try:
#         item = next(iter_f)
#         print(fruits)
#     except StopIteration:
#         print("출력완료")
#         break

# plus = [x**2 for x in range(10)]
# print(plus)


# class Iterator:
#     def __init__(self):
#         self.data = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         while self.data <= 10:
#             current = self.data
#             self.data += 1 
#             if current % 2 ==0:
#                 return current
#         raise StopIteration

# my_iter = Iterator()
# # print(type(my_iter))
# for i in my_iter:
#     print(i)

class MyRange:
    def __init__(self, start, stop, step):
        self.current = start 
        self.stop = stop 
        self.step = step 

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration

        result = self.current
        self.current += self.step
        return result

for i in MyRange(1,10,2):
    print(i, end=" ")