# a = "megastudy".upper() #대문자화
# print(a)
# b = "megastudy".replace("study", "coffee") #바꿔줘
# print(b)
# c = "megacoffee".count("f") #알파벳 개수를 세줘
# print(c)
# 입력한 소문자를 대문자로 변환해주는 프로그램
# a = (input("소문자 입력: ")).upper()
# print(a)
# left right 노래에서 left right 몇개씩 있는지 찾는 프로그램
# song = """left right left right..."""
# left = song.count("left")
# right = song.count("right")
# print(f"가사에서 right:{right}개, left{left}개 있음")
'''# 영어 기사 하나 가져오고 유저가 입력한 단어의 갯수를 나타내는 프로그램
art = """Despite being among the top-ranked teams in the FIFA,
ranking at No. 23, South Korea has never won the Asian Cup since hosting the 1960
event in Seoul. The closest it had come in recent years was the final of the 2015
tournament in Australia, where it fell 2-1 to the home team.
The team conceded a goal in all of its six matches in Qatar,
despite facing much lower-ranked teams, with the exception of No. 25 Australia.
Bahrain ranks No. 86, Malaysia No. 130, Saudi Arabia No. 56, and the Koreans'
 latest tormentor Jordan is ranked at No. 87."""
word = input('찾고 싶은 단어:')
result = art.count(word)
print(f"찾고 싶은 단어 {word}는 {result}개 있음")
'''
# 뉴스 기사 단어 대체 프로그램(the를 ❤로 변경)
art = """Despite being among the top-ranked teams in the FIFA,
ranking at No. 23, South Korea has never won the Asian Cup since hosting the 1960
event in Seoul. The closest it had come in recent years was the final of the 2015
tournament in Australia, where it fell 2-1 to the home team.
The team conceded a goal in all of its six matches in Qatar,
despite facing much lower-ranked teams, with the exception of No. 25 Australia.
Bahrain ranks No. 86, Malaysia No. 130, Saudi Arabia No. 56, and the Koreans'
 latest tormentor Jordan is ranked at No. 87."""
result = art.replace("the", "❤")
print(result)

