var1 = "Hello Python"
print(var1)  #문자열 객체 출력
print(id(var1))  #주소 출력

var1 = 100
print(var1)
print(id(var1))

var2 = 150.25
print(var2)
print(id(var2))


a = int(10.5)
b = int(1.5)
add = a+b
print(add)

print(int(True))
print(int(False))

st = '10'
print(int(st)**2)

name = 'hj'
age = 28
address = '''우편번호 12345 서울시 서울빌딩'''
friend = None
height = 165.4

print("주소:",address)
print("친구:",friend)
print("키:",height)
print("키:",int(height))
print(int(height))