#с этим я все поняла спасибо, теперь давай так же только с другим кодом с занятия, там посложнее:

from abc import abstractmethod
from typing import override

class BaseDuck:
    wings: int = 2
    beak: bool = True

class BaseToy:
    material: str = 'plastic'
    
class MixinWalkable:
    legs: int = 2
    def walk(self):
        print(f"Walked away on {self.legs} feets")

class MixinNoisable:
    @abstractmethod
    @override
    def make_noise(self, volume_db: int) -> None:
        raise NotImplementedError

class MixinDustable:
    def get_dusty(self) -> None:
        print('gets dusty')

class Duckess(BaseDuck, MixinNoisable, MixinWalkable, MixinDustable):
    def make_noise(self, volume_db: int) -> None:
        print(f'quackie ({volume_db} dB)')

class Duck(BaseDuck, MixinNoisable, MixinWalkable, MixinDustable):
    def make_noise(self, volume_db: int) -> None:
        print(f'quack ({volume_db} dB)')
        
class ToyDuck(BaseDuck, BaseToy, MixinDustable):
    pass

if __name__ == "__main__":

    d1 = Duck()

    d1.make_noise(12)

    d1.walk()

    ds1 = Duckess()

    ds1.make_noise(12)

    td1 = ToyDuck()

    td1.get_dusty()
    
# from abc import abstractmethod
# from typing import override

# class BaseDuck:
#     wings: int = 2
#     beak: bool = True
   
    
# class BaseToy():
#     def get_dusty
#     def make_noise(self, volume_db: int)-> None:
#         raise NotImplementedError
    
# class MixinWalkable:
     
#     @abstractmethod
#     @override
#     def get_dusty(self)->None:
#         print(""gets dusty)
        
# class MixinNoisible:
#     @abstractmethod
#     @override
#     legs: int = 2
#     def walk(self):
#         print(f"Walked away")
        
    
     
#     @abstractmethod
#     @override
# class Mixin
    
# class Duckess(BaseDuck):
#     def make_noise(self, volume_db: int)-> None:
#         print(f"quake {volume_db} db")
#     d1 = Duck()
#     d1.make_noise(12)
    
#     ds1 = Duck()
    
    
# class Duck(BaseDuck, MixinNoisible, MixinWalkable):
#     d = Duck
#     d.make_noise()
    
# class ToyDuck(BaseDuck, BaseToy):
#     td = ToyDuck()

# if __name__=="__main__":
#     d1 = Duck()
#     d1.make_noise(12)
#     d1.walk()
    
#     ds
        
    