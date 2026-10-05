# weektest04.py

#9-2
print("hello")
class Student:
    school = "High School"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
s1 = Student("Alice", 1)

print(Student.school)
print(s1.school)
print(s1.name)

print('----------')

#10-1

from math import factorial

print(factorial(5))

print('----------')


#10-2

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog1 = Dog()
print(dog1.speak())

print('----------')

# #11-1
# import tkinter as tk

# root = tk.Tk()
# selected_value = tk.IntVar()

# # Radiobutton 위젯 예시
# rb1 = tk.Radiobutton(root, text="옵션 1", variable=selected_value, value=1)
# rb2 = tk.Radiobutton(root, text="옵션 2", variable=selected_value, value=2)

# rb1.pack()
# rb2.pack()

# print('----------')

# import tkinter as tk
# from tkinter import messagebox

# def on_buton_click():
#     messagebox.showinfo("알림", "버튼이 클릭되었습니다!")

# root = tk.Tk()
# root.title("간단한 Tkinter 앱")
# root.geometry("300x200")

# btn = tk.Button(root, text="클릭하세요", command=on_buton_click)
# btn.pack(pady=20)

# root.mainloop()

print('----------')
# #12-1

# with open("data.txt", 'w', encoding='utf-8') as file:
#     for i in range(1,11):
#         file.write(f"{i}번째 줄입니다.\n")

# print("파일이 성공적으로 작성되었습니다.")

# with open("data.txt", "r", encoding='utf-8') as file:
#     contents = file.read()

# print("파일내용:")
# print(contents)

# print('---------')

# #12-2
# with open("data.txt", 'a', encoding='utf-8') as file:
#     data = "11번째 줄입니다.\n"
#     file.write(data)
    
# print(data)
# print("파일이 성공적으로 추가되었습니다.")

# with open("data.txt", "r", encoding='utf-8') as file:
#     contents = file.read()

# print("파일내용:")
# print(contents)

print('---------')
#13-1

# while True:
#     try:
#         num = int(input("숫자를 입력하세요:"))
#         print((lambda x:x**2)(num))
#         break
#     except ValueError:
#         print("올바른 숫자를 입력하세요!")

print('---------')
#13-2

num_list = [10,20,30,40,50]
result = map(lambda x:x**2, num_list)
result_list = list(result)
print(result_list)

print('---------')