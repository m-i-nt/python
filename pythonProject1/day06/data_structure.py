# data_structure
# [] list, {} set, {} dict, () tuple

# # set(집합, !!!중복 허용 안됨!!!)
# a = {1,2,3,1,2,3}
# b = set([1,2,3,4,1,2,3,4]) #!!!set(1,2,3,4)는 a = 1,2,3,4를 쓴 것과 같아서 오류남!!!
# print(a) #{1, 2, 3}
# print(b) #{1, 2, 3, 4}
# a.add(10)
# print(a) #{10, 1, 2, 3}
#
# starbucks = ["아아", "라떼", "모카", "티"]
# megacoffee = ["아아", "라떼", "딸기", "아이스크림"]
# a = set(starbucks)
# b = set(megacoffee)
# #1
# a.update(b)
# print(a)
# #2
# set = set.union(a,b)
# print(set)

# #영어기사의 모든 단어를 중복 없이
# article = """ Tensions continued to build Tuesday between doctors and the government, with a group of over 10,000 junior doctors ending their first discussion about joining the nationwide strike without reaching a conclusion. Instead, they decided to forge an emergency committee in an apparent move to escalate their offensive against the government plan to increase the medical school enrollment quota.
#
# The Korea Intern Resident Association, consisting of thousands of junior doctors essential to the critical care of patients in large hospitals across the country, said it would transition into an emergency leadership committee system to make an active response against the plan which they claim will lower the nation’s health service quality.
#
# Although no further announcement was made regarding plans to engage in collective action on the group’s official website, observers suggest that the shift translates into them buying time to mull measures possibly to take collective action within legal boundaries in which they could keep their medical licenses.
#
# According to reports, some are also seeking ways to protest by refusing to renew training contracts with hospitals. Also, some interns are considering leaving the hospital after completing their training if they can’t submit resignations. If the walkouts were to occur, observers believe it would likely happen after Thursday when the specialist practical examination ends."""
# b = article.split(" ")
# c = set(b)
# d = list(c)
# d.sort()
# print(d)

# 두개의 영어기사를 스크랩해서 중복된 단어만 추출
article1 = '''The Korea Intern Resident Association, consisting of thousands of junior doctors essential to the critical care of patients in large hospitals across the country, said it would transition into an emergency leadership committee system to make an active response against the plan which they claim will lower the nation’s health service quality.'''
article2 = """Tensions continued to build Tuesday between doctors and the government, with a group of over 10,000 junior doctors ending their first discussion about joining the nationwide strike without reaching a conclusion. Instead, they decided to forge an emergency committee in an apparent move to escalate their offensive against the government plan to increase the medical school enrollment quota."""
wordList1 = article1.split(" ")
wordList2 = article2.split(" ")
wordset1 = set(wordList1)
wordset2 = set(wordList2)
#1
set = set.intersection(wordset1, wordset2)
#2
set = wordset1.intersection(wordset2)
print(set)


# 데이터가 추가/삭제되면 새로운 변수에 넣기 (예) a.sort() -> print(a)
# 데이터가 추가/삭제되지 않으면 그대로 한 줄 (예) a = set.intersection() -> print(a)