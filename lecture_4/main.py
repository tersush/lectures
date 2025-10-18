a: int = 2
b: str = 'hello'
c: float = 2.4
d: bool = True
e: None = None #отсутствие вообще чего-либо

if b is None: #это делает ссылку на None, выходит "дешевле"
    print('b is None')
    
if e==None:
    print("e is None")
