from random import randrange


ok_sign = ["o", "x"]
sum = 0

for users in range(1, 51):
    so_time = randrange(5, 51)
    if so_time <= 15 and so_time >= 5:
        index = 0
        sum +=1
    elif so_time > 15:
        index = 1
    
    print("[{0}]{1}번째 손님 (소요시간: {2}분)".format(ok_sign[index], users, so_time))
print("총 탑승객 {0}명".format(sum))