'''
2023-04-11
김희수
  정수 2개와 연산자 1개 (+,-,*,/)를 입력 받아서 사칙연산을 수행하는 프로그램 작성
'''

num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))
op = input("연산자를 입력하세요(+,-,*,/): ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("잘못된 연산자입니다.")

print("결과는 {}입니다.".format(result))
