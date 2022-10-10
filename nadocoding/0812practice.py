# print("a" + "b")
# print("a", "b")

# 방법 1
# print("나는 %d살입니다." %20)
# print("나는 %s를 좋아해요." % "파이썬")
# print("apple 은 %c로 시작해요." %"a")

# 방법 2
# print("나는 %s색과 %s색을 좋아해요."%("파란","빨간"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("검정", "하얀"))
# print("나는{age}살이며, {color}색을 좋아해요. ".format(age = 20, color="파랑"))


# 방법 4
# age = 30
# color = "노랑"

# print(f"나는{age}살이며, {color}색을 좋아해요") 
# print("Red apple\rpine")

# 퀴즈
# url = "http://youtube.com"
# my_str = url.replace("http://", "")
# print(my_str)
# my_str = my_str[:my_str.index(".")]

# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

# print("{0}의 비밀번호는 {1}입니다. ".format(url, password))
