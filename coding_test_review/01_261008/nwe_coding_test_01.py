x = input(int("가격을 입력하시면 할인 금액이 출렵됩니다 :", x))


def shop(x):
    
            if x >= 100000:
                price = x * 0.95
                return price
            elif x >= 300000:
                price = x * 0.9
                return price
            elif x >= 500000:
                price = x * 0.8
                return price
            else:
                print("할인 적용 안됨.")

result = shop(x)    
print("할인된 금액은", x)