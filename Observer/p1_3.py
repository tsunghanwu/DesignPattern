## A heater example with observer design pattern

from abc import ABCMeta, abstractmethod
from p1_2 import Observer, Observable

class WaterHeater(Observable):
    def __init__(self):
        super().__init__() ## Init with the observable parent class setting
        self._temperature = 25 ## Default temperature sets to 25
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature
        print('Set the temperature to {} degree C'.format(temperature))
        self.notify_observers() ## Notify the observers

## Washing mode child class of observer
class WashingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and observable.temperature >= 50 and observable.temperature < 70:
            print('The water temperature is good for showering')

## Drinking mode child class of observer
class DrinkingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and observable.temperature >= 100:
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
