print('재미있는', '파이썬')
print('python', 'java', 'c', sep = ',')
print()
print('영화 타이타닉')
print('평점 ', end = ':')
print(' 5점')

fos = open('sample.py',  mode='wt')
print('print("hello world")', file = fos)
fos.close()

format(value, 'format')
%d %o %x %f %s

