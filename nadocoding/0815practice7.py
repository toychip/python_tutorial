# 지역변수 전역변수

gun = 10

#전역변수를 지역변수로 사용 그러나 권장x return을 통해 사용하는 것을 추천
def checkpoint(soilders):   # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soilders
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
# checkpoint(2)   # 2명이 경계 근무를 나감
gun = checkpoint_ret(gun, 2)
print("전체 총: {0}".format(gun))