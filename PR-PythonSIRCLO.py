import random

while(True):
    try:
        angka = int(input("guess any number:"))
        if type(angka) != int:
            raise ValueError
        break
    except ValueError as e:
        print("input a valid number 1-20")

def guess_num(func):
    def wrapper(number):
        i = 1
        while i <= 5:
            list_numbers=func(number)
            print(list_numbers)
            for num in list_numbers:
                if num == number:
                    return f"congrats, you guessed {number} on round {i}"
            i+=1
        return f"unfortunately you have not won any guess"
    return wrapper

@guess_num
def generate_number(number):
    random_list=[random.randint(0,20) for i in range(0,6)]
    return random_list

print(generate_number(angka))


# def generate_number():
#        random_list=[random.randint(0,20) for i in range(0,5)]
#        return random_list

# def guessed_number(number,func):
#     i = 1
#     while i <= 6:
#         list_numbers = func()
#         print(list_numbers)
#         for num in list_numbers:
#             if num == number:
#                 return f"Congratulations, You Guessed {number} on round {i}"
#         i+=1
#     return f"Unfortunately you have not won any guess"

# print(guessed_number(angka,generate_number))

