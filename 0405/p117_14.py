'''
2023-04-05
김희수
5과목 점수 입력 받아서 총점과 평균 구하기
'''

sub1=int(input("첫번쨰 과목 점수 입력:")) #과목1 점수 입력
sub2=int(input("두번쨰 과목 점수 입력:")) #과목2 점수 입력
sub3=int(input("세번쨰 과목 점수 입력:")) #과목3 점수 입력
sub4=int(input("네번쨰 과목 점수 입력:")) #과목4 점수 입력
sub5=int(input("다섯번쨰 과목 점수 입력:")) #과목5 점수 입력

total=sub1+sub2+sub3+sub4+sub5 #합계 구하기
avg=total/5 # 평균 구하기

print("5과목의 합계는{}이고, 평균은 {}이다.".format(total,avg))