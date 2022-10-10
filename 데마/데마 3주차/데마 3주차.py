import numpy as np
Score = np.random.randint(100, size=(10, 4))

def num1():
    print()
    print("1번 문제")
    print()                     # 행은 0~9까지 모두 출력해야하므로 행은 0:1 에 수학 점수는
    for i in range(10):         # 인덱스에서 2열에 있기에 2:3을 사용한다, 반복문을 이용하여 수학 점수만 출력
        print("{0}번째 학생의 수학 점수: {1}점".format(i+1, int(Score[i:i+1, 2:3])))

def num2():
    print()
    print("2번 문제")
    print()
    sum_Score = np.sum(Score, axis=1)          # 넘파이 sum함수를 이용하여 각 학생의 점수를 합해야하므로
    for k in range(10):               # 행들의 값을 더하는 axis를 이용한다.
        print("{0}번째 학생의 점수 합계: {1}점".format(k+1, sum_Score[k]))
                            # 반복문을 이용하여 번째는 반복 i+1, 합한 리스트를 새로 만들어서 출력한다.

def num3():
    print()
    print("3번 문제")
    print()
    first_score = Score[0:1, :]
    second_score = Score[2:3, :]            # 인덱스에 주어진 값으로 불린 인덱스를 구하는 5번같은 문제는 풀 수 있는데..
    third_score = Score[4:5, :]             # 2차원 배열에서 불린 인덱스만을 이용하여 홀수행만 갖고 오는 방법을 몰라서 이렇게 풀었습니다..
    fourth_score = Score[6:7, :]            # 최선을 다해서 계속 생각해봤지만 이 방법 말곤 도저히 모르겠어서 이렇게 제출합니다 ㅠㅠ
    fifth_score = Score[8:9, :]
    # concatenate 함수를 이용하여 합친다. axis=0 이므로 한 행 후 바로 다음 행이 이어지게 하는 구조다.
    odd_score = np.concatenate([first_score, second_score, third_score, fourth_score, fifth_score, ], axis=0)
    for i in range(5):
        print("{0}번째 학생의 과학 점수: {1}, 수학 점수:{2}, 국어 점수:{3}, 영어 점수:{4}" \
              .format(i + 1, odd_score[i][3], odd_score[i][2], odd_score[i][0], odd_score[i][1]))

def num4():
    print()
    print("4번 문제")
    print()                                     # 과목을 출력할 subject리스트를 만든다.
    subject = ["국어", "영어", "수학", "과학"]
    # 최대값을 구하는 max함수를 사용하고, 과목 중에 최대값을 구해야하므로 axis=0으로 열의 최대값을 구한다.
    max_Score = np.max(Score, axis=0)           # 최대값을 저장할 max_Score리스트를 만든다.
    for j in range(4):                          # 과목 이름과 점수를 함께 출력한다.
        print("{0}의 최대 점수: {1}".format(subject[j], max_Score[j]))

def num5():
    print()
    print("5번 문제")
    print()
    Eng_Score = Score[:, 1:2]       # 영어 점수를 모아놓은 리스트 생성
    Eng_under90_Score = Eng_Score < 90  # 영어 점수가 90점 미만인지 아닌지 boolean값으로 삽입
    # boolean값으로 True인 학생들의 (90점 미만인 학생들의) 점수만을 가져옴
    print("90점 미만의 학생들의 점수: {0}".format(Eng_Score[Eng_under90_Score]))

def main():
    print("60191957 임준형 데이터 마이닝 3주차 과제")
    print()
    print("학생들의 전체 점수표")
    print(Score)
    num1()
    num2()
    num3() 
    num4()
    num5()

main()