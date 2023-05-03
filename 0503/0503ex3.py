'''
김희수
2023-05-03
#문제정의
  1~입력받은 숫자까지의 합계 구하기
#문제분석
  변수 i,n,sum
  
#알고리즘
  1. 변수 선언
  2. 문장 출력
'''

#for반복
n=int(input("정수입력:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    i=i+n
print("1~{}숫자까지의 합:".format(n),sum)