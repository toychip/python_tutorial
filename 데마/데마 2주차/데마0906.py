# def main():
#     name = get_name()
#     print('hello', name)


# def get_name():
#     name = input('Enter your name: ')
#     return name

# main()



from random import *
Lst = [random.randint(1, 100) for i in range(20)]

Lst2_temp = range(1, 101)
Lst2_temp = list(Lst2_temp)

shuffle(Lst2_temp)

Lst2 = sample(Lst2_temp, 20)



# def findsame():    
#     for i in range(1):
#         index = Lst2.find("Lst2[i]")
#         if index == 1:
#             made_list()




# def made_list():
#     Lst = [random.randint(1, 100) for i in range(20)]

