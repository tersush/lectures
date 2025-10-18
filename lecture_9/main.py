from enum import StrEnum
from typing import Self
import Prendon

class Names(StrEnum):

    MER: str = "Mercury"
    MAR: str = "Mars"
    ER: str = "Earth"
    UR: str = "Uranus"
    

    

class Planets:
    health_points: int = 100
    name = Names.MER
        
    def __eq__(self, other: Self):
        return self.health_points==other.health_points
    
    def __lt__(self, other:Self):
        return self.health_points
    
    def __str__(self):
        return f"Planet({self.name!r}, hp={self.health_points!}"
    
    def styling(self):
        if self.name == Names.MER:
            return "name is Mercury"
        elif self.name is Names.MAR: #лучше использовать это
            return "in Mars style"
        return "without style"
    
    def attack(
        self, 
        other: Self,
    ):
        print(f"{self.name} is attacking {other.name}{self.styling}")
        other.health_points -=10
        
class PlanetArmy:
    planets_list: list[Planets]
    planets_name: Names
    planets_max_health_points: int = 100
    
    def __init__(
        self,
        for 
    
    for _ in range(20):          #если нам не нужна буква i можно просто _
        planets: Planets = Planets(
            health_points = random.randint(
                a=1,
                b=self.palnets_max_health_points
            )
        )
        
if __name__=="__main__":
        # m1: Planets = Planets(health_points=100, name=Names.MAR)
        # m2:Planets = Planets(health_points=90, name=Names.ER)
        # print("==",m1==m2)
        # print("!=",m1!=m2)
        # print(f"{m2.health_points}")
        # m1.attack(m2)
        # print(f"{m2.health_points}")
        