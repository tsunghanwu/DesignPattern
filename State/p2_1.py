from abc import ABCMeta, abstractmethod

class Water:
    def __init__(self, state):
        self.__temperature = 25
        self.__state = state

    @property
    def state(self):
        return self.__state

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature
        if self.__temperature <= 0:
            self.change_state(SolidState('Solid'))
        elif self.__temperature <= 100:
            self.change_state(LiquidState('Liquid'))
        else:
            self.change_state(GaseousState('Gas'))

    def rise_temperature(self, step):
        self.temperature = self.temperature + step

    def reduce_temperature(self, step):
        self.temperature = self.temperature - step

    def change_state(self, state):
        if self.__state:
            print('State change: {} to {}'.format(self.state.name, state.name))
        else:
            print('Initialize state to {}'.format(state.name))
        
        self.__state = state

    def behavior(self):
        self.__state.behavior(self)


class State(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def behavior(self, water):
        pass

class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print('I am cold and hard. Current temperature is {}C.'.format(water.temperature))

class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print('I am warm and fluid. Current temperature is {}C'.format(water.temperature))

class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print('I am hot and light. Current temperature is {}C'.format(water.temperature))


def main():
    water = Water(LiquidState('Liquid'))
    water.behavior()
    water.temperature = -4
    water.behavior()
    water.rise_temperature(18)
    water.behavior()
    water.rise_temperature(110)
    water.behavior()

if __name__ == '__main__':
    main()
