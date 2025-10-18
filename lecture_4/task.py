""" вывести треугольник паскаля до 9. чтобы было красиво
"""
print('Введи степень, для которой тебе необходимо вывести коэффициенты:')
power_of: int = int(input())
list_1=[1]
print(" " *(int(power_of)+1) + "1")
for i in range (power_of):
    inner_act=[1]
    for g in range(len(list_1)-1):
        new_variable=list_1[g]+list_1[g+1]
        inner_act.append(new_variable)
    inner_act.append(1)
    list_1=inner_act
    print(" " *(int(power_of)-i) + " ".join(map(str, inner_act)))
    

'''
    tuple_2[0]==1
    tuple_2[power_of]==1
    tuple_2[-power_of]
    [number_of_members-i]=[tuple_1[0]+tuple_1[1]] #по цифре 3 степени пишу
    i=i+1
    [number_of_members-i]=[tuple_1[1]+tuple_1[2]] #по цифре 3 степени пишу 
        []
        print()
        i=i+1
        [0]==1
    [power_of]==1
'''