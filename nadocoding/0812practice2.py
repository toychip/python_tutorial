#리스트
#suffle(lst) -> 무작위로 순서를 바꿈
#print(sample(lst, 1))  lst리스트에서 1개 만큼 랜덤으로 뽑을것이다.
subway = [10, 20, 30]

print(subway)

subway = ["유재석", "조세호", "박명수"]

print(subway)

#조세호가 몇번째 칸에 타고있는가?
print(subway.index("조세호"))

#하하를 맨 뒤에 추가
subway.append("하하")

print(subway)

#정형돈을 유재석과 조세호 사이에 태움
subway.insert(1, "정형돈")

print(subway)

# 젤 뒤에서부터 한명씩 뺌

print(subway.pop())     # 누구를 뺐는지

print(subway.count("유재석"))

#정렬

num_list = [5, 8, 3, 4, 6, 1]

num_list.sort()     #순서대로 정렬
print(num_list)

num_list.reverse()    #거꾸로 정렬
print(num_list)

# num_list.clear()
# print(num_list)

num_list.extend(subway)
print(num_list)