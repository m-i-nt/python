# 1. 유저에게 설날에 먹은 음식 3개를 묻고,
# 설날에 먹은 음식 리스트 나타내기
food = []
a = input('설날에 먹은 음식 : ')
b = input('설날에 먹은 음식 : ')
c = input('설날에 먹은 음식 : ')
food.append(a)
food.append(b)
food.append(c)
print(food)

# 2. 유저에게 좋아하는 커피 프랜차이즈 영어로 입력받고
# 대문자화하기
cafe = input('좋아하는 커피 프랜차이즈: ')
result = cafe.upper()
print(result)

# 3. 유저에게 이메일 주소를 입력받고 도메인만 출력하기
# ex) megastudy@naver.com -> naver
a = input('이메일 주소 입력: ')
b = a.split('@')
c = b[1].split('.')
print(c[0])
