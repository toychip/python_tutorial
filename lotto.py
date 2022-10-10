import random
for j in range(20):
    lotto = []

    rnd_num = random.randint(1, 45)

    for i in range(6):
        while rnd_num in lotto:
            rnd_num = random.randint(1, 45)

        lotto.append(rnd_num)


    lotto.sort()
    print('{}번째 로또번호: {}\n'.format(j+1, lotto))
    lotto.clear()


