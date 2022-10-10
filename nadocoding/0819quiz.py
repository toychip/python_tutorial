# def std_weight(height, gender):
#     if gender == "male":
#         trans_height = height / 100
#         avg_kg = trans_height * trans_height * 22
#         print("키 {0}cm 남자의 표준 체중은 {1}kg입니다. ".format(height, round(avg_kg, 2)))
#     elif gender == "female":
#         avg_kg = trans_height * trans_height * 21
#         print("키 {0}cm 여자의 표준 체중은 {1}kg입니다. ".format(height, round(avg_kg, 2)))


# std_weight(185, "male")



def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    elif gender == "여자":
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다. ". format(height, gender, weight))
