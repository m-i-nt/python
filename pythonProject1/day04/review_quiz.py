'''
# 1
age = int(input("나이가 어떻게 되십니까?"))
print(f"나이가 {age}살이라면, 출생년도는 {2025-age}년입니다.")

# 2
side = input('한 변의 길이:')
print(f"한 변의 길이가 {side}cm이면, 넓이는 {side**2}cm^2")

# 밑변과 높이를 받아서 정삼각형 너비 구하기
base = int(input('밑변의 길이 :'))
height = int(input('높이:'))
print(f"밑변이 {base}cm, 높이가 {height}cm라면 너비는 {0.5*base*height}cm^2입니다.")
'''
# 정수 분리기
num = int(input('10000~99999 정수 입력:'))
print(f"{num//10000}만 {(num//1000)%10}천 {(num//100)%10}백 {(num//10)%10}십 {(num%10)}")

'''
num = input('10000~99999 정수 입력:')
num[0], num[1], num[2], ...
'''

# 시간 변환(초 단위를 시:분:초 로 쪼개기)
time = int(input('시간 입력:'))
hour = time // 3600
min = (time % 3600) // 60
sec = time % 60
print(f"{hour}시:{min}분{sec}초")

# 다섯 자리 수 중에서 백의 자리 숫자 추출
num1 = input('10000~99999 정수 입력:')
print(f"{(num1 // 100) % 10}")