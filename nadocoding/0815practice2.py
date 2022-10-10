# for

# for waiting_no in [1, 2, 3, 4, 5]:
#     print("대기번호: {0}".format(waiting_no))

# for waiting_no in range(1, 101):
#     print("대기번호: {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}님, 커피 주문되었습니다. ".format(customer))

# while

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피가 폐기처리 되었습니다. ")


# customer = "아이언맨"
# index = 1
# while 1:
#     print("{0}님, 커피가 준비되었습니다. {1}번 불렀습니다. ".format(customer, index))
#     index += 1
#     if index == 100:
#         print("100번이나 지나서 폐기합니다. ")
#         break

customer = "토르"
person = "unknown"

while person != customer:
    print("{0}님 커피가 준비되었습니다. ".format(customer))
    person = input("이름이 어떻게 되세요? ")
    































    
