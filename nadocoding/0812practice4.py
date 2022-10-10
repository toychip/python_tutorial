# 튜플
# 변경 x 추가 x 

# (name, age, hobby) = ("임준형" , 23 , "코딩")
# menu = ("돈가스", "치즈가스")
# print(name, age, hobby)
# print (menu)

# 세트
# 중복 x 순서 x 

# my_set = {1,2,3,3,3}
# print(my_set)

java = {"유재석", "조세호", "정형돈"}
python = set(["유재석", "박명수"])

#교집합,    java와 python을 모두 할수 있는 사람

print(java & python)
print(java.intersection(python))

#합집합     java를 할 수 있거나 python을 할 수 있는 사람

print(java|python)
print(java.union(python))

#차집합     java는 할 수 있지만 python은 할 수 없는 사람

print(java - python)
print(java.difference(python))

#python 할 수 있는 사람 새로 추가
python.add("김태호")
print(python)

#java를 까먹음

java.remove("조세호")
print(java)

















