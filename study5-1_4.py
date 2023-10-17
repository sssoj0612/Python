#adder3.py
# 계산기가 3,5,10개 필요할 때 그때마다 전역 변수와 함수를 추가할 것인가?
# 클래스를 이용하면 해결 가능

class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

# Calculator 클래스로 만들어진 별개의 계산기(인스턴스) 생성
cal1 = Calculator()
cal2 = Calculator()

# 결과값 역시 다른 계산기 결과값과 상관 없이 독립적인 결과값 유지
print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
