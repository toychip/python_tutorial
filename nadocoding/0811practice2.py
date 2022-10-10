# 슬라이싱

# jumin = "940427-1246820"
# print(jumin)
# print('성별 :' + jumin[7])
# print('태어난 년도: ' + jumin[0:2]) # 0 부터 2 직전까지 0,1
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])         # 4부터 6 직전까지 4, 5
# print("생년월일 : " + jumin[:6])    # 처음부터 6 직전까지 
# print("뒤 7자리 : " + jumin[7:])    # 7부터 끝까지
# print("뒤 7자리 : " + jumin[-7:])   # 끝을 -1로 지정, -7부터 끝까지


# 문자열 처리 함수

name = "My name is Lim Jun Hyoung"
print(name.upper())     # 전체 대문자
print(name.lower())     # 전체 소문자

print(name[1].isupper())       
print(name[1].islower())
print(len(name))        # 문자열 길이 반환
print(name.replace("Jun Hyoung", "Ju Hee"))     
'''
replace, upper, lower 
문자를 찾아서 바꿈 그러나 변수가 바꿔지진 않음
'''


 # n이 몇번째 자리에 있는지

index = name.index("n")
print(index)

# 방금 index보다 한자리 뒤부터 n이 몇번째 자리에 있는지
index = name.index("n", index + 1) 
print(index)


print(name.find("Hee"))        #찾는게 없으면 -1 반환
# print(name.index("Hee"))     #찾는게 없으면 오류
print(name.count("n"))         #찾는게 몇번 나오는지

