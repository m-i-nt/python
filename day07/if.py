# 프로그램 실행 순서(위->아래)
# 프로그램의 흐름을 제어할 필요할 때가 있다.
# 제어문(control statement) : 프로그램의 흐름을 컨트롤함
# 1) 조건문(conditional statement): if, switch[dict]
# 2) 반복문(loop statement): for, while

# 조건문 if
# a = int(input('숫자입력: '))
# if a > 0:
#     print('a는 양수입니다')
#     print('테스팅!')
# print('프로그램 끝')

#유저에게 megastudy를 입력하면 (조건)'메가스터디 유저이군요!'(무조건)'안녕하세요!
# a = input('입력: ')
# if a == "megastudy":
#     print('메가스터디 유저이군요!')
# print('안녕하세요!')
# = 한번 쓰면 문자 대입, == 두번 쓰면 비교 연산자('같다')

#유저에게 영어로 좋아하는 과일을 입력받고
#apple이면 '저두 사과 좋아해요!'
#(무조건) '~~과일은 맛있죠!'
# fruit = input('좋아하는 과일을 영어로 쓰기: ')
# if fruit == 'apple':
#     print('저두 사과 좋아해요!')
# print(f"{fruit}는 맛있죠!")

# if-else
# a = int(input('숫자입력: '))
# if a > 0:
#     print('양수')
# else:
#     print('0 또는 음수')

# 유저에게 숫자를 입력받고 홀수인지 짝수인지 판별해주는 프로그램
# a = int(input('숫자 입력: '))
# if a % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# # 유저에게 영어 단어를 입력받고, e가 있으면 e포함, 없으면 e없음
# word = input('영어 단어 입력: ')
# if 'e' in word: #if word.count('e') > 0 :
#     print('e포함')
# else:
#     print('e없음')

# 유저에게 하나의 알파벳을 입력받고 소문자면 대문자로, 대문자면 소문자로 출력
# alphabet = input('알파벳 입력: ')
# if alphabet.islower(): #.islower(): 소문자니?
#     print(alphabet.upper())
# else:
#     print(alphabet.lower())


# 두 숫자를 유저에게 입력받고 큰 숫자를 출력하는 프로그램
# num1 = int(input('숫자 입력:'))
# num2 = int(input('숫자 입력:'))
# if num1 >= num2:
#     print(num1)
# else:
#     print(num2)

