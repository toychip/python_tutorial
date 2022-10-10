#def main():


def calculateGrade():


    import random
    answer = [[0 for col in range(10)]for row in range(8)]
    perfect = [0 for perx in range(10)]

    for j in range(8):                              # 학생 답 랜덤 생성
        for i in range(10):
            choice = chr(random.randint(65, 69))
            answer[j][i] = choice

    print(answer)

    for k in range(10):                              # 정답 생성
        perfect_choice = chr(random.randint(65, 69))
        perfect[k] = perfect_choice
    print("-----정답-----")
    print(perfect)

    index = [0 for students in range(8)] 
    for q in range(8):                              # 2중 반복으로 비교
        for w in range(10):
            if answer[q][w] == perfect[w]:
                index[q] = index[q] + 1
        print("{}번 학생의 맞춘 개수:{}개".format(q, index[q]))


calculateGrade()
