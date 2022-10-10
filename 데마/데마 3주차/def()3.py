# def num5():
#     print()
#     print("5번 문제")
#     print()
#     Eng_Score = Score[:, 1:2]       # 영어 점수를 모아놓은 리스트 생성
#     Eng_under90_Score = Eng_Score < 90  # 영어 점수가 90점 미만인지 아닌지 boolean값으로 삽입
#     # boolean값으로 True인 학생들의 (90점 미만인 학생들의) 점수만을 가져옴
#     print("90점 미만의 학생들의 점수: {0}".format(Eng_Score[Eng_under90_Score]))

import numpy as np
Score = np.random.randint(100, size=(10, 4))

print(Score)
first_score = Score[0:1, :]
second_score = Score[2:3, :]
third_score = Score[4:5, :]
fourth_score = Score[6:7, :]
fifth_score = Score[8:9, :]
odd_score = np.concatenate([first_score, second_score, third_score, fourth_score, fifth_score,], axis=0)
print(odd_score)
for i in range(5):
    print("{0}번째 학생의 과학 점수: {1}, 수학 점수:{2}, 국어 점수:{3}, 영어 점수:{4}"\
          .format(i+1, odd_score[i][3],odd_score[i][2], odd_score[i][0], odd_score[i][1]))






    # 0, 2, 4, 6, 8, 첫번째, 세번째, 다섯번째, 일곱번째, 아홉번째

# Odd_Score = Score[:, odd[]]
# print(Odd_Score)
#
# Score[a]

