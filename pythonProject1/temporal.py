'''
num1 = 100
num2 = 40
a = num1 + num2
b = num1 / num2
c = num1 - num2
d = num1 % num2
e = num1 // num2
f = num1 * num2
g = num1 ** 2
print(a, b, c, d, e, f, g)
print(num1 == num2)

tree = '#'
blank = ' '
print(blank*4, tree*1)
print(blank*3, tree*3)
print(blank*2, tree*5)
print(blank*1, tree*7)

a = input('두 자리 정수 : ')
b = int(a) // 10
c = int(a) % 10
print('십의 자리는, ', b)
print('일의 자리는, ', c)


a = 12
a -= 1
print(a)

'''
print('원주율=', format(3.14159, '8.3f'))
print('금액=', format(125000, '3,d'))
print('%o' %100)

name = '홍길동'
age = 35
price = 124.566
print('이름 : %s, 나이 : %d, 가격 : %.2f' %(name, age, price))

print('name : {}, age : {}, data : {}'. format(name, age, price))
print('이름: {1}, 나이:{0}, price:{2}'. format(age, name, price))

who = 'you'
how = 'happy'
result = f'{who} make me {how}'
print(result)

uid = input('id input : ')
query = f"select * from member where uid={uid}"
print(query)
