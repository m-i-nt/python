#1
arr = []
delete_list = []

if [i for i in arr] == [x for x in delete_list]:
    res = arr.remove(i)

input('arr 입력:')
print(res)

#filter
def solution(arr, delete_list):
    return list(filter(lambda x: x not in delete_list, arr))

#2
def solution1(n):
    listNumber = list(str(n)) #['1',...'5']
    listNumber.reverse()
    return list(map(lambda x: int(x), listNumber))

def solution1(n):
    return list(map(lambda x: int(x), reversed(str(n))))

12345 n
'12345' str(n)
'54321' reversed(str(n))
5,4,3,2,1 map(lambda x: int(x), reversed(str(n)))
[5,4,3,2,1] list(map(lambda x: int(x), reversed(str(n))))

list(str(n)).reverse() == reversed(str(n))
#reverse는 list만 가능/ reversed는 문자도 되고 리스트도 되고 튜플도 됨


#3
def solution2(num):
    num.sort()
    return max(num[0]*num[1], num[-1]*num[-2])

