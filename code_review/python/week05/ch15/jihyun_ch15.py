food = ["김밥","만두","양념치킨","족발","피자","쫄면","라면"]

iterator = iter(food)
print("__iter__" in dir(food))

###이터레이터 생성방법
# 1. iter() 함수 활용
# 2. 클래스 작성
# 3. 제너레이터 생성

#확인 방법
for food in iterator:
    print(food)
print(next(iterator, "주문완료"))

# 제너레이터 생성 방법
# 1.yield
# 2.제너레이터 컴프리핸션

file_path = "./ch15/file.txt"
data ="""파이썬은 1991년 네덜란드란계 소프트웨어 엔지니어인 
1994년에 정식 출시한 인터프리터형 프로그래밍 언어
프로그래밍 교육, 인공지능, 데이터 분석 및 빅데이터
프로그래밍 입문용으로 많이 추천된다."""

def write_file(file_path):
    with open(file_path, 'w', encoding = "utf-8") as file:
        file.write(data)

# # 파일에서 한줄씩 읽기
def read_file(file_path):
    with open(file_path, 'r') as f:
        for line in f.readline():   
            yield line.strip()

write_file(file_path)
lines = read_file(file_path)
print(type(lines))          #generator
print(type(lines))
for line in lines:
    print(line)
