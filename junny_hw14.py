import re
# pattern = r'\w+'
# text = "Hello, World!"
# print(re.findall(pattern, text))

# pattern =r'(ab)+'
# text = "ababab"
# match = re.match(pattern, text)
# print(match.group())

# patter=r"\w+@\w+\.\w+"
# text = "이메일 목룍: text@example.com, hello@world.net, user123@domain.org"
# email = re.findall(patter, text)
# print(email)

# text = "연락처 : 010-1234-5678, 02-987-6543, 031-456-7890"
# pattern = r"\d{3}-\d{4}-\d{4}|\d{2}-\d{3}-\d{4}|\d{3}-\d{3}-\d{4}$"
# number = re.findall(pattern, text)
# print(number)

# text = "I love Python. Java is also popular. Python is great for AI."
# patter = r"[^.]*Python[^.]*\.?"
# result = re.findall(patter, text)
# resultall = [s.strip() for s in result]
# print(resultall)


# text = "상품 코드 : A123, B456, C789, 가격: 12000원"
# patter= r"\d+"
# result = re.findall(patter, text)
# print(result)

text = "NASA is working on AI projects with IBM and Google."
pattern = r"\b[A-Z]{4}\b|\b[A-Z]{2}\b"
list = re.findall(pattern, text)
print(list)