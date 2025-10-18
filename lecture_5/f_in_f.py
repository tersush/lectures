def inc(value: int) -> int:
    value+=10
    return value
print('hello from function')
if __name__=='__main__':



def print_to_console(init_value: int): #что в скобках про тип данных - хинтинг, он не обязателен
    print(init_value)
    print('hello')
def no_return(value: int) -> int:
    if value%5==0:
        value*10
    if value==20:
        return
    else: return value
#print(no_return(100))
#print_to_console(2)

def rec(x:int) -> int:
    print('rec_x=',x)
    x+=1
    if x<100:
        rec(x)
    return x
rec(0)
x=1
x=inc(x)
'''ф-и по дефолту если не написано ретурн возвращают None'''