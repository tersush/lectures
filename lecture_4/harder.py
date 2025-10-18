a: Ellipsis = ...
b: complex = complex(real=3,imag=-2)
c: list = [a,2,b,4,a,b,7,8,10]
d: tuple = (1,2,3,4)
e: set = {'hello','like','chego','nu','hello'} #помогает искать уникальные значения, в сете нет порядка
f: dict = {1: '11',
           2: '22', 
           3: '33',
           'kak': 'dela'} #keyword:value -> call f[1], 1 - keyword,в дикшн может быть дикшн, но онли в формате велью
print(c[2])
print(c[1:3]) #слайсинг по списку, начало и конец (не включительно)
print(c[0:7:2]) #старт:стоп:шаг

print(c[::2]) #от начала до конца с шагом 2
print(c[::-2]) #переворачивает лист 

print(e)

print(list(f.keys()))
print(list(f.values()))