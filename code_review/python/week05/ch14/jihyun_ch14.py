text = "My phone number is 123-456-7890"
import re
numbers = re.findall(r"\d+",text)
print(numbers)

text = "Contact us at support@example.com or salese@example.org."
import re
pattern = r"[\w.-]+@[\w.-]+\.\w+"
emails = re.findall(pattern, text)
print(emails)

phone = '123-456-7890'
import re
phon_pattern = r"^\d{3}-\d{3}-\d{4}$"
if re.match(phon_pattern, phone):
    print("Vaild phone number")
else:
    print("Invalid phone number")