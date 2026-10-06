# hyungchan_ch14.py

import re

#1 
text = "My phone number is 123-456-7890"

numbers = re.findall(r"\d+", text)
print(numbers)

print('-----------')

#2 
text = "Contact us at support@example.com or sales@example.org."
pattern = r"[\w.-]+@[\w.-]+\.\w+"
emails = re.findall(pattern, text)
print(emails)

print('-----------')
#3 

phone = "123-456-7890"
phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
if re.match(phone_pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

print('-----------')