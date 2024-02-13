# a = "hello,world".split(',')
# b = 'hello world happy'.split(' ')
# print(b)
#
# #영문 기사를 오름차순으로 단어 정렬
# article = """The top YouTubers in Korea earned an average annual income of nearly million won."""
# words = article.split(" ")
# words.sort()
# print(words)
# a = ",".join("megastudy")
# print(a)
# b = ",".join(['happy','sad','good'])
# print(b)
'''
# 영어 기사에서 유저에게 입력받은 이모지로 각각 단어 사이에 이모지를 넣어 새로운 기사로 출력하는 프로그램
emoji = input('이모지 입력:')
article = """a b c """
words = article.split(" ")
result = emoji.join(words)
print(result)

emoji = input('이모지 입력:')
article = """a b c """
result = article.replace(' ', 'emoji')
print(result)
'''
#유저에게 이메일 주소를 입력받고 유저의 도메인을 제외한 앞의 이메일을 첫글자만 대문자로 된 이메일 출력
#예: megastudy@naver.com -> Megastudy

# @로 split
# 리스트에서 첫번째 가져오기
# 가져온 첫번째를 대문자화
# 출력

# email = input('이메일 주소 입력: ')
# id = email.split('@')
# result = id[0].capitalize()
# print(result)

#단어를 입력하면 알파벳 순으로 정렬해서 보여주는 프로그램
#예: mega -> aegm

# mega -> ['m','e','g','a']
# 정렬화
# 문자화

# word = input('단어 입력: ')
# result = list(word)
# result.sort()
# new = ''.join(result)
# print(new)

# # 1. 유저에게 설날에 먹은 음식 3개를 묻고,
# # 설날에 먹은 음식 리스트 나타내기
# food = []
# a = input('설날에 먹은 음식 : ')
# b = input('설날에 먹은 음식 : ')
# c = input('설날에 먹은 음식 : ')
# food.append(a)
# food.append(b)
# food.append(c)
# print(food)
#
# # 2. 유저에게 좋아하는 커피 프랜차이즈 영어로 입력받고
# # 대문자화하기
# cafe = input('좋아하는 커피 프랜차이즈: ')
# result = cafe.upper()
# print(result)
#
# # 3. 유저에게 이메일 주소를 입력받고 도메인만 출력하기
# # ex) megastudy@naver.com -> naver
# a = input('이메일 주소 입력: ')
# b = a.split('@')
# c = b[1].split('.')
# print(c[0])

# # 4. 영어 기사를 스크랩해서 단어별로 리스트화해서 오름차순으로 출력
# article = """ Tensions continued to build Tuesday between doctors and the government, with a group of over 10,000 junior doctors ending their first discussion about joining the nationwide strike without reaching a conclusion. Instead, they decided to forge an emergency committee in an apparent move to escalate their offensive against the government plan to increase the medical school enrollment quota.
#
# The Korea Intern Resident Association, consisting of thousands of junior doctors essential to the critical care of patients in large hospitals across the country, said it would transition into an emergency leadership committee system to make an active response against the plan which they claim will lower the nation’s health service quality.
#
# Although no further announcement was made regarding plans to engage in collective action on the group’s official website, observers suggest that the shift translates into them buying time to mull measures possibly to take collective action within legal boundaries in which they could keep their medical licenses.
#
# According to reports, some are also seeking ways to protest by refusing to renew training contracts with hospitals. Also, some interns are considering leaving the hospital after completing their training if they can’t submit resignations. If the walkouts were to occur, observers believe it would likely happen after Thursday when the specialist practical examination ends."""
#
# word = article.split(" ")
# word.sort()
# print(word)

# 영어 기사에서 유저에게 입력받은 이모지로 각각 단어 사이에 이모지를 넣어 새로운 기사로 출력하는 프로그램
article = """ Tensions continued to build Tuesday between doctors and the government, with a group of over 10,000 junior doctors ending their first discussion about joining the nationwide strike without reaching a conclusion. Instead, they decided to forge an emergency committee in an apparent move to escalate their offensive against the government plan to increase the medical school enrollment quota.

The Korea Intern Resident Association, consisting of thousands of junior doctors essential to the critical care of patients in large hospitals across the country, said it would transition into an emergency leadership committee system to make an active response against the plan which they claim will lower the nation’s health service quality.

Although no further announcement was made regarding plans to engage in collective action on the group’s official website, observers suggest that the shift translates into them buying time to mull measures possibly to take collective action within legal boundaries in which they could keep their medical licenses.

According to reports, some are also seeking ways to protest by refusing to renew training contracts with hospitals. Also, some interns are considering leaving the hospital after completing their training if they can’t submit resignations. If the walkouts were to occur, observers believe it would likely happen after Thursday when the specialist practical examination ends."""

emoji = input('이모지 입력 : ')
