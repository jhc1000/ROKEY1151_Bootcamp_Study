# hyungchan_hw14.py

#3
import re
pattern = r'\w+'
text = "Hello, World!"
print(re.findall(pattern, text))
# ["Hello", "World"]

print('-----------')
#5
import re
pattern = r'(ab)+'
text = "ababab"
match = re.match(pattern, text)
print(match.group())

print('-----------')
#6
import re

text = "이메일 목록: test@example.com, hello@world.net, user123@domain.org"
pattern = r"\w+@\w+.\w+"
result = re.findall(pattern, text)
print(result)

print('-----------')
#7
import re

text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"
pattern = r'\d{3}-\d{4}-\d{4}'
result = re.findall(pattern, text)
print(result)

print('-----------')
#8
import re

text = "I love Python. Java is also popular. Python is great for AI."
pattern = r"\b[\w ]*Python[\w ]*\."     
result = re.findall(pattern, text)
print(result)
# \b는 단어의 경계(word boundary)를 뜻합니다. 
# 알파벳/숫자/밑줄(`\w`)과 그 외의 문자(공백, 구두점 등)가 만나는 지점부터 매치하게 해줌.

print('-----------')
#9
import re

text = "상품 코드: A123, B456, C789, 가격: 12000원"
pattern = r"\d+"
result = re.findall(pattern, text)
print(result)

print('-----------')
#10
import re

text = "NASA is working on AI projects with IBM and Google."
pattern = "[A-Z]{2,}"
result = re.findall(pattern, text)
print(result)

print('-----------')