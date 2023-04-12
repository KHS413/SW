'''
2023-04-12
김희수
입력받은 두 수의 크기 비교
#문제분석
    변수-숫자1(num1),숫자2(num2)
#알고리즘
  1.변수 선언
    num1,num2에 정수 입력
  2.논리(선택 if~else)
    if num1 > num2:
      (참)큰 수는 num1, 작은 수는 num2
    else:
      (거짓) 큰수는 num2, 작은 수는 num1
'''

num1=int(input("숫자를 입력하세요: "))
num2=int(input("숫자를 입력하세요: "))

if num1 > num2:
    print("두 수 중에 큰 수는 num1이고 작은 수는 num2입니다")
else:
    print("두 수 중에 큰 수는 num2이고 작은 수는 num1입니다")
