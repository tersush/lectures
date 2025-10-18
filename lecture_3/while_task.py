"""дан регион [-1000;1000)
пользователь загадал целое число
задача программы замучать пользователя в виде вопросов 
взять середину региона и спросить больше или меньше выбранного числа
и так в цикле делить регионы пополам сужая область поиска, пока не найдем нужное число
"""

# ввести диапазон пользователю
print(f"Давай сыграем в игру, загадай число и назови любой диапазон, в который это число входит. Если надоест, скажи: выход")
array_beggining: int = input()
array_end: int = input()
median = (int(array_beggining)+int(array_end))//2
user_input_1: str = input(f"Твое число больше или меньше {median} [если больше 1, меньше 0, равно =]?")
while user_input_1!="=":
    if user_input_1=="выход":
        break
    while user_input_1=="0":
        array_end=median
        median = (int(array_beggining)+int(array_end))//2
        user_input_1: str = input(f"Твое число больше или меньше {median}[если больше 1, меньше 0, равно =]?")
        median+=1
    while user_input_1=="1": 
        array_beggining=int(median)
        median = (int(array_beggining)+int(array_end))//2
        user_input_1: str = input(f"Твое число больше или меньше {median}[если больше 1, меньше 0, равно =]?")
        median-=1
if user_input_1 =="=":
    print(f"Твое число {(int(array_beggining)+int(array_end))//2}!")