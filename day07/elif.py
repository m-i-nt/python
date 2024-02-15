#elif
# a = 1
# if a>0:
#     print('양수')
# elif a == 0:
#     print('0')
# else: #else는 모든 여집합이라 가정 불가
#     print('음수')

#유저에게 영어점수를 입력받고 90점대(A), 80점대(B), 70점대(C), 70미만(과락)
# score = int(input('영어점수 입력: '))
# if score >= 90:
#     if score == 100:
#         print('100점 축하합니다!') #if 안에 if 또 넣기 가능
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# else:
#     print('과락')

# 정수입력받고 양의홀수, 양의짝수, 0, 음의홀수, 음의짝수를 출력
# a = int(input('정수 입력: '))
# if a > 0:
#     if a % 2 == 0:
#         print('양의 짝수')
#     else:
#         print('양의 홀수')
# elif a == 0:
#     print('0')
# else:
#     if a % 2 == 0:
#         print('음의 짝수')
#     else:
#         print('음의 홀수')

# 비밀번호 설정 프로그램
# 유저에게 비밀번호 설정을 입력받고, 아래 조건이 성립되도록 프로그램 만들기
# 1. 최소 10글자 이상 -> 틀리면 '10글자가 아닙니다'
# 2. !,@,#이 하나 이상 -> 틀리면 '!,@,# 중 꼭 포함'
# 3. 첫 글자가 무조건 대문자 -> 틀리면 '첫번째 문자가 꼭 대문자여야 함'
# 1~3 모두 통과 시 '비밀번호 설정완료!' 나타내기

# pw = input('비밀번호 입력: ')
# if len(pw) < 10:
#     print('10글자가 아닙니다.')
# elif not ('!' in pw or '@' in pw or '#' in pw):
#     print('!,@,# 중 꼭 포함')
# elif pw[0].islower():
#     print('첫번째 문자가 꼭 대문자여야 함')
# else:
#     print("비밀번호 완료!")

# 사용자에게 버스 노선 종류를 나타내는 정수와 승객의 나이를 입력받고 나이와 노선에 따라 요금 계산해 출력
bus = int(input('버스 노선 종류 선택(1~3): '))
price = {
    1: 1200,
    2: 2000,
    3: 1000
}
age = int(input('나이 입력: '))
if 8 <= age <= 19:
    result = int(price[bus]) * 0.7
elif age < 8 or age >= 65:
    result = 0
else:
    result = price[bus]
print(f"버스 요금은 {result}원입니다")

# bus = {
#     'type': ['시내버스', '광역버스', '마을버스']
#     'price': [1200, 2000, 1000]
# }