MY_COUNTER=0 #капсом пишутся константы, глобальные переменные
x=0
def print_to_console(): #все названия переменных принято не начинать с цифр  и подчеркивания
    global x
    global MY_COUNTER
    MY_COUNTER +=1
    x=0
    x+=1
    print('hello',x)
    x+=1
    print('hello',x)
print_to_console()
print_to_console()
print_to_console()