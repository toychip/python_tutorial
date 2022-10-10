from typing_extensions import Self


class isReact:
    def __init__(self):
        self.__answer == 1
    def regular_cube(avenue):
        volumee = avenue * avenue * avenue
        return volumee                          #정육면체의 경우

    def hexahedron(avenue, height, high):
        volumee = avenue * height * high
        return volumee                          #직육면체의 경우

    
answer = input("정육면체 입니까? Y or N: ");

if answer == 'Y':
    avenue = int(input("변의 길이를 입력하시오:"))
    fin = isReact.regular_cube(avenue)
    
        

elif answer == 'N':
    avenue = int(input("가로의 길이를 입력하시오:"))
    height = int(input("세로의 길이를 입력하시오:"))
    high = int(input("높이의 길이를 입력하시오:"))
    fin = isReact.hexahedron(avenue, height, high)
else:
    print("잘못 입력하셨습니다. ")
        
print("총 부피는 {}입니다.".format(fin))




#def anony_func():



