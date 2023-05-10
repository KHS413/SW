'''
#문제정의
  3의 배수의 총합이 입력된 숫자를 넘었을 때의 n값과 총합계, n값이 몇 번째 인지를 
  while 반복문을 사용해 프로그램 작성하기
#문제분석
  변수 - num,sum,cnt,i
#알고리즘
  1.변수 초기화
  2.변수 삽입
'''
num=int(input("사용자 입력:"))
sum=0
cnt=0
i=0
while True:
    i=i+3
    sum=sum+i
    cnt=cnt+1
    if sum>num:
        break
    
print("{}을 넘었을 때 숫자:{}".format(num,i))
print("{}을 넘었을 때 까지의 합계:{}".format(num,sum))
print("{}을 넘었을 때 까지 몇 번째 3의 배수인가:{}".format(num,cnt))