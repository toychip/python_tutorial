# # 자료구조의 변경
# # 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


# 퀴즈#4

from random import *

users = range(1, 21)   # 1부터 21 직전까지 

users = list(users)

shuffle(users)

winners = sample(users, 4)      # 4명 중에서 1명은 치킨 3명은 커피
print("---당첨자발표---")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("---축하합니다---")
