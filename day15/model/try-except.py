try:
    num = int(input('숫자입력:'))
    print(f"결과: {10 / num}")
except ValueError:
    print('숫자를 넣으세요 ...')
except ZeroDivisionError:
    print('0 넣지 마 ...')
