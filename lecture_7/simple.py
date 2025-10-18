class Human:

    name: str

    legs: int

    eyes: int

    hands: int

    hair_color: str

    

    def __init__(

        self, 

        name: str = "Vova",

        eyes: int = 2,

        hands: int = 2,

        legs: int = 2,

        hair_color: str = "brown",

    ):

        self.name = name

        self.legs = legs

        self.eyes = eyes

        self.hands = hands

        self.hair_color = hair_color

        

    def __repr__(self):  # необязательный пируэт

        vars_to_print = [

            f"{name}={value!r}" for name, value in vars(self).items()

        ]

        return (

            f"{self.__class__.__name__}({', '.join(vars_to_print)})"

        )

    

    def blink(self):

        print(f"{self.name} blinked with {self.eyes} eyes")

        

    def walk(self):

        print(f"{self.name} walked away on {self.legs} feet(s)")

    

    def break_plank(self, plank_material: str = "wooden", quantity: int = 2):

        print(

            f"{self.name} breaks {quantity} {plank_material} planks"

        )


class SmartHuman(Human):

    glasses: bool

    iq: int

    

    def __init__(self, glasses: bool = True, iq: int = 130):

        super().__init__()  # вызов инита родителя

        self.glasses = glasses

        self.iq = iq

    

    def blink(self):

        print(

            f"Smart {self.name} blinked with {self.eyes} eyes "

            f"and with glasses {'on' if self.glasses is True else 'off'}"

        )

    

if __name__ == '__main__':

    human1 = Human()

    

    human1.blink()

    human1.break_plank()

    human1.break_plank('plastic', 3)

    

    human2 = Human(name="Andrey", legs=2)

    human2.blink()

    

    smart_human1 = SmartHuman()

    smart_human1.blink()

    

    print(smart_human1)
# class Human:
#     name: str = "Vova"
#     eye: int
#     hands: int
#     legs: int
#     hair_color: str = "brown"
    
#     def __init__(self, name: str = "Vova", legs: int = 2, hair_color: str = "brown", eye: int = 2):
#         self.name = name
#         self.legs = legs
#         self.hair_color = hair_color
#         self.eye = eye
#         self.blink(self.name)
        
# class SmartHuman(Human):
#     glasses: bool = True
#     iq: int = 130
        
#     def __init__(self, glasses: bool = True, iq: int = 130):
#         super().__init__() # вызов ф-и того, от чего наследуем
#         self.glasses = glasses
#         self.iq = iq
    
#     def blink(self,name): #имя которое будет относится к классу - через self
#         self.name = "Andrey"
#         print(f"{self.name} blinked with {self.eye} and with glasses {"on" if self.eye is True else "off"}") #тернарные функции
        
#     def break_plank(self, planck_material: str = "wooden", quantity: int = 2):
#         print (f"Breaks {quantity} {planck_material}")
    
        
#     def walked(self,name):
#         print(f"{name} walked away")
        
#     if __name__=="__main__":
#         human1 = Human(name="Kate", legs =2)
#         smart_human1 = SmartHuman()
#         smart_human1.blink()
        
        