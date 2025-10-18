from abc import abstractmethod
from typing import override

class MixinAnimated:
    def animated(self):
        return True
        
class MixinFunny:
    def make_laugh(self):
        print("is laughing")
        
class MixinSpeakable:
    def speak(self):
        print("have said something")
        
class MixinActionable:
    def perform_action(self):
        print("smiles playfully")
        
class MixinCollectible:
    def able_to_collect(self):
        return True

class MixinPoseable:
    def pose(self):
        print("makes cool pose")
        
class MixinCostumeWearable:
    def costume(self):
        print(f"This cosplayer wears {self.name} costume")
        
class MixinBulliable():
    def get_bullied(self):
        print(f"This stupid {self.age} y.o. {self.gender} cosplays {self.character}.. Cringe..")
        
class BaseHuman:
    def __init__(self, gender, age):
        self.gender = gender 
        self.age = age
    def is_human(self):
        return True

class BaseCharacter(MixinActionable, MixinAnimated, MixinFunny):
    name: str = "Bob"
    
class BaseInActionCharacter(BaseCharacter):
    def performs_action(self):
        print("acts on the screen")
            
class Shrek(BaseCharacter):
    name = "Shrek"
    skin_color = "green"
    
class Donkey(BaseCharacter):
    name = "Donkey"
    fur_color = "Grey"
    
class PussInBoots(BaseCharacter):
    name = "Puss in Boots"
    fur_color = "Red"
    
class JackHorner(BaseCharacter):
    name = "Jack Horner"
    hair_color = "Durty pink"
    
class ShrekInAction(Shrek, BaseInActionCharacter):
    def performs_action(self):
        print(f"{self. name} screamed: - DONKEEEEY!")
        
class DonkeyInAction(Donkey, BaseInActionCharacter):
    def performs_action(self):
        print(f"{self. name} smiles with all teeth")
        
class PussInBootsInAction(PussInBoots, BaseInActionCharacter):
    def performs_action(self):
        print(f"{self.name} looks with cute cat eyes")
         
class JackHornerInAction(JackHorner, BaseInActionCharacter):
    def performs_action(self):
        print(f"{self. name} steals a flying carpet")
    
class BaseFunkoPop(MixinCollectible, BaseCharacter):
    def display(self):
        print("stands quietly")
        
class ShrekFunkoPop(BaseFunkoPop,Shrek):
    def display(self):
        print(f"{self.name} figure makes me calm")
        
class PussInBootsFunkoPop(BaseFunkoPop,PussInBoots):
    def display(self):
        print(f"{self.name} is the rariest figure in my collection")
        
class DonkeyFunkoPop(BaseFunkoPop,Donkey):
    def display(self):
        print(f"{self.name} figure looks very uncanny..")
        
class JackHornerFunkoPop(BaseFunkoPop,JackHorner):
    def display(self):
        print(f"{self.name} figure costs 52$")
        
class BaseCosplayer(MixinPoseable, MixinCostumeWearable, MixinBulliable, BaseCharacter, BaseHuman):
    def __init__(
        self,
        gender: str,
        age: int, 
                 ):
        self.character = self.name
        super().__init__(gender=gender, age=age)
    def pose(self):
        print("makes cool pose")
        
class ShrekCosplayer(BaseCosplayer,Shrek):
    def pose(self):
        print("makes 'roar' pose")
    
class PussInBootsCosplayer(BaseCosplayer,PussInBoots):
    def pose(self):
        print("mimics licking its paw")
        
class DonkeyCosplayer(BaseCosplayer,Donkey):
    def pose(self):
        print("stands on all fours")
        
class JachHornerCosplayer(BaseCosplayer,JackHorner):
    def pose(self):
        print("stands haughtily")
        
if __name__ == "__main__":

    puss1 = PussInBootsCosplayer(gender = "male", age=15)
    shrek1= ShrekCosplayer(gender = "female", age = 30)
    don1 = DonkeyCosplayer (gender= "male", age = 12)
    jh1= JachHornerCosplayer(gender = "male", age = 21)
    puss1.get_bullied()
    shrek1.get_bullied()
    don1.get_bullied()
    jh1.get_bullied()
    
    puss2 = PussInBootsFunkoPop()
    shrek2 = ShrekFunkoPop()
    don2 = DonkeyFunkoPop()
    jh2 = JackHornerFunkoPop()
    
    puss2.display()
    don2.display()
    shrek2.display()
    jh2.display()
    
    puss3 = PussInBootsInAction()
    shrek3 = ShrekInAction()
    don3 = DonkeyInAction()
    jh3 = JackHornerInAction()
    
    puss3.performs_action()
    shrek3.performs_action()
    don3.performs_action()
    jh3.performs_action()
        
