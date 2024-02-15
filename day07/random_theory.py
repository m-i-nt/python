import random

# a = random.randint(0, 101) # 0~101까지 랜덤 숫자 뽑기
# b = random.randint(0, 11)
# c = ['아메', '라떼', '우유']
# print(f"{a} {b}") #실행할 때마다 새로운 결과값 나옴
# print(f"{random.choice(c)}") #실행할 때마다 리스트에서 랜덤하게 뽑힘

# 유저에게 번호 하나를 물어봐서 로또 번호에 있으면 번호 있음, 없으면 번호 없음
user = int(input('번호 대시오: '))
# 리스트에 6개의 랜덤 정수(1-45)를 넣고 정렬해서 보여주기 #로또
num = []
num1= random.randint(1, 45)
num2= random.randint(1, 45)
num3= random.randint(1, 45)
num4= random.randint(1, 45)
num5= random.randint(1, 45)
num6= random.randint(1, 45)
num.append(num1) #num.append(random.randint(1, 45)) 해도 됨
num.append(num2)
num.append(num3)
num.append(num4)
num.append(num5)
num.append(num6)
num.sort()
print(num)
if user in num:
    print('번호 있음')
else:
    print('번호 없음')
