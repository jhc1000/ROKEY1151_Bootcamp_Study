# hyungchan_ch15.py

#1 
food = ["김밥", "만두", "양념치킨", "족발", "피자", "쫄면", "라면"]

# 이터레이터 생성 방법
# 1. iter() 함수 활용
# 2. class 작성
# 3. 제너레이터 생성

iter_food = iter(food)
print(type(iter_food))
for i in iter_food:
    print(i)
    
    
print('---------')

#2
file_path = "./ch15/ch15_2.txt"
# data = [f"i 번째 줄\n" for i in range(1,10)]
data = """1번째 줄
2번째 줄
3번째 줄
4번째 줄
5번째 줄
6번째 줄
7번째 줄
8번째 줄
"""

def write_file(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data) 
        
        
# def read_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#         for line in lines:
#             yield line.strip()
            
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()
        

write_file(file_path)
gen_read = read_file(file_path)
print(type(gen_read))
print(next(gen_read))
print(next(gen_read))
print(next(gen_read))

