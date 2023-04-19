'''
2023-04-19
김희수
두 개의 숫자를 입력받아서 두 번째 수가 첫 번째 수의 약수인지 구분하기
#문제분석
  변수 num1,num2
  수식 num % num2 == 0

  #알고리즘
  변수선언 
   num1,num2에 정수입력
'''




num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

if num1 % num2 == 0:
    print(num2, "는", num1, "의 약수입니다.")
else:
    print(num2, "는", num1, "의 약수가 아닙니다.")