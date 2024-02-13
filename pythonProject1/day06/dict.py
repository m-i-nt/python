# dict: key(중복안됨, int, str) - value(중복가능, 모든 타입)
coffee = {
    1 : "아아",
    2 : "아라",
    3 : "바닐라"
}
print(coffee[3])

#유저에게 mbti를 입력받고 유저의 mbti 성향을 알려주는 프로그램 만들기
#entj -> 외향적 직관적 공감 못하는 계획적 이시군요
mbti ={
    'e': '외향적',
    'i': '내향적',
    's': '현실적',
    'n': '직관적',
    't': '공감 못하는',
    'f': '감성적',
    'p': '즉흥적',
    'j': '계획적'
}
user = input('mbti 입력: ')
print(f"{mbti[user[0]]} {mbti[user[1]]} {mbti[user[2]]} {mbti[user[3]]} 이시군요")
