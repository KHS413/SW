'''
김희수
2023-05-3
1~10합계 구하기
'''
#while 반복
i=1 #반복 횟수 초기화
sum=0
while i<=10: #반복 조건
    sum=sum+i #합계
    i=i+1
print('1~10까지의 합계:',sum)

print()
#for 반복
sum=0
for i in range(1,11): #반복 조건
    sum = sum + i    
print('1~10까지의 합계:',sum) #i출력