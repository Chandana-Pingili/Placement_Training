from abc import ABC,abstractmethod

class AbstractVehicle(ABC):
    def __init__(self,colour,n_tyres,gears) -> None:
        self.colour=colour
        self.num_tyres=n_tyres
        self.gears=gears
        