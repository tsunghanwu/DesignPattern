from abc import ABCMeta, abstractmethod
from p2_2 import Context, State

class Water(Context):
    def __init__(self):
        super().__init__()
        self.add_state(SolidState('Solid'))
        self.add_state(LiquidState('Fluid'))
        self.add_state(GaseousState('Gas'))
        self.temperature = 25

    @property
    def temperature(self):
        return self.stateInfo

    @temperature.setter
    def temperature(self, temperature):
        self.stateInfo = temperature

    def rise_temperature(self, step):
        self.temperature = self.temperature + step

    def reduce_temperature(self, step):
        self.temperatrue = self.temperature - step

    def behavior(self):
        state = self.state
        if isinstance(state, State):
            state.behavior(self)

## A Singleton decorator
def singleton(cls, *args, **kwargs):
    instance = {}
    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton

@singleton
class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        print('I am cold and hard. Temperature is {}.'.format(context.stateInfo))

@singleton
class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return (stateInfo >= 0) and (stateInfo < 100) 

    def behavior(self, context):
        print('I am warm and fluid. Temperature is {}.'.format(context.stateInfo))

@singleton
class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print('I am hot and light. Temperature is {}.'.format(context.stateInfo))


def main():
    water = Water()
    print(water._states)
    water.behavior()
    water.temperature = -4
    water.behavior()
    water.rise_temperature(18)
    water.behavior()
    water.rise_temperature(110)
    water.behavior()

if __name__ == '__main__':
    main()

