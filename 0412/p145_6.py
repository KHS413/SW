'''
2023-04-12
김희수
두 숫자를 입력받아 두 숫자가 모두 짝수이면 두 수를 더한 결과를 출력하고
그렇지 않으면 둘 중 하나가 홀수이면 몇 번째 입력한 수를 짝수로 입력해야 하는지 출력

#문제분석
  변수 첫번쨰 정수(num1),두번째 정수(num2)

  수식 num1 % 2== 0 (num1은 짝수) / num1%2 ! =0

  #알고리즘
1. 변수 선언
  -num1,num2에 정수 입력
2.논리 (선택 if~elif~else)
  if num1%2 ==0 and num2%2==0:
    (조건 참) num1+num2
  elif num1%2==0 and num2%2==1:
    (조건 참) 두 번째 정수를 짝수로 입력하세요.
  elif num1%2==1 and num2%2==0:
    (조건 참) 첫 번째 정수를 짝수로 입력하세요.      
  else:
      "두 숫자 모두를 짝수로 입력하세요"

'''

num1=int(input("숫자를 입력하세요: "))
num2=int(input("숫자를 입력하세요: "))

if num1%2 ==0 and num2%2==0:
    print("{}+{}={}".format(num1,num2,num1+num2))
elif num1%2==0 and num2%2==1:
    print("두 번째 정수를 짝수로 입력하세요.")
elif num1%2==1 and num2%2==0:
    print("첫 번째 정수를 짝수로 입력하세요.")     
else:
      print("두 숫자 모두를 짝수로 입력하세요")