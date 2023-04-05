'''
2023-04-05
김희수
월급 수령액을 구하는 프로그램 작성
'''

sal = int(input("본봉 입력: "))
bonus = int(input("수당 입력: "))
tax = (sal+bonus) * 0.2

total = (sal+bonus-tax)

print("홍길동의 월급 실 수령액은{}이고,세금은{}이다. ".format(total,tax))

