## A heater example with observer design pattern

from abc import ABCMeta, abstractmethod

class WaterHeater:
    def __init__(self):
        self._observers = []
        self._temperature = 25 ## Default temperature sets to 25
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature
        print('Set the temperature to {} degree C'.format(temperature))
        self.notifies() ## Notify the observers

    def add_observer(self, observer):
        self._observers.append(observer)

    def notifies(self):
        for observer in self._observers:
            observer.update(self)

## Parent class for the observer
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, waterheater):
        pass

## Washing mode child class of observer
class WashingMode(Observer):
    def update(self, waterheater):
        if waterheater.temperature >= 50 and waterheater.temperature < 70:
            print('The water temperature is good for showering')

## Drinking mode child class of observer
class DrinkingMode(Observer):
    def update(self, waterheater):
        if waterheater.temperature >= 100:
            print('The water temperature is good for drinking')

## Main function for execution
def main():
    heater = WaterHeater()
    washing_observer = WashingMode()
    drinking_observer = DrinkingMode()
    heater.add_observer(washing_observer)
    heater.add_observer(drinking_observer)
    heater.temperature = 40
    heater.temperature = 60
    heater.temperature = 100

if __name__ == '__main__':
    main()
