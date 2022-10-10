# 표준 입출력

# print("python", "java", sep = ",", end ="?") # end 끝부분을 end로 바꿔서 줄바꿈 x
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# scores = {"수학":0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
#     # ljust 왼쪽 정렬, rjust 오른쪽 정렬

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기 번호:" + str(num).zfill(3))


# zfill() 안 숫자는 몇칸을 말하는지 의미, 빈 공간을 0으로 채우는 함수


answer = input("아무 값이나 입력하세요 : ")

print("입력하신 값은 {0}입니다. ".format(answer))



