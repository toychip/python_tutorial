# 사전

cabinet = {3 : "유재석", 100 : "김태호" }

print(cabinet[3])

print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5])
# 오류가 있으면 바로 프로그램 종료

print(cabinet.get(5))
# 오류가 있으면 None으로 출력하고 프로그램 계속 진행


print(cabinet.get(5, "사용가능"))
#없으면 뒷 문장을 출력

print(3 in cabinet) 
#안에 있는지 확인

cabinet[300] = "조세호"

print(cabinet)

del cabinet[3]
# 키에 해당하는 값을 지움

print(cabinet)

#키들만 출력

print(cabinet.keys())

#값들만 출력

print(cabinet.values())

#키와 값들을 쌍으로 묶어서 출력

print(cabinet.items())

#전부 지우기

cabinet.clear()
print(cabinet)

















