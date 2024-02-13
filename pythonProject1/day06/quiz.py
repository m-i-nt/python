# 영화 예매 프로그램[dict 등 자료 구조 적절히 사용]
# 사용자로부터 영화 종류, 팝콘 종류 입력받고 구매한 영화 내용, 팝콘 이름, 총 금액을 출력하는 프로그램

# a = input('영화 종류 : ')
# movie = {'액션': '10000', '로코': '8000', '공포': '9000'}
# b = input('팝콘 종류 : ')
# popcorn = {'치즈': '6000', '카라멜': '5000', '일반': '5000'}
# c = int(movie[a]) + int(popcorn[b])
# print(f"선택하신 영화는 '{a}', 팝콘은 '{b}'이므로 총 '{c}원' 입니다.")

theater = {
    'movie': {
        'movieList': ['액션', '로코', '공포'],
        'price': [10000, 8000, 9000]
    },
    'popcorn':{
        'popcornList': ['치즈', '카라멜', '일반'],
        'price':[6000,5000,5000]
    }
}
movie = int(input(f"{theater['movie']['movieList']}중 선택하세요(0~2번):"))
popcorn = int(input(f"{theater['popcorn']['popcornList']}중 선택하세요(0~2번):"))
print(f"영화:{theater['movie']['movieList'][movie]}, 팝콘:{theater['popcorn']['popcornList'][popcorn]}")
print(f"총 가격:{theater['movie']['price'][movie]+theater['popcorn']['price'][popcorn]}")