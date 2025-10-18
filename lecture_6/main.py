import time
from functools import lru_cache
@lru_cache() 

def calculate_surname(age: int,name:str = 'Ksuysha')-> str:
    wait_time: int=5
    time.sleep(2)
    print(f'Waiting {wait_time} seconds...')
    time.sleep(2)
    print (f'Hello,{name} ({age} y.o.)')
    
MY_CACHE: dict[str,str]={}

def calculate_greetings(name: str = "Vova"):
    if name in MY_CACHE:
        return MY_CACHE[name]
    time.sleep(2)
    surname= name +"4kin"
    MY_CACHE[name]= surname
    return surname

print(f'MY_CACHE')
_=calculate_greetings("Vova")
_=calculate_greetings("Vov")    
_=calculate_greetings("Vo")        
    
if __name__=='__main__':
    print(f"{MY_CACHE}")
    print('Warmup cache')
    _=calculate_greetings('Ksyusha')
    _=calculate_greetings()
    _=calculate_greetings('Bread')
    print(calculate_greetings('Bread'))
    print(calculate_greetings('Ksysha'))
    print(calculate_greetings())
    print(f'{MY_CACHE}')
    
#print('Hello')
#time.sleep(3)
#print('World')


