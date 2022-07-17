from abc import ABCMeta, abstractmethod

class Context(metaclass=ABCMeta):
    def __init__(self):
        self._states = []
        self._curState = None
        self._stateInfo = 0
    
    @property
    def state(self):
        return self._curState
    
    def add_state(self, state):
        if state not in self._states:
            self._states.append(state)

    def change_state(self, state):
        if state is None:
            return False
        elif self._curState == None:
            print('Initialize to {} phase'.format(state.name))
        else:
            print('From {} to {}'.format(self._curState.name, state.name))

        self._curState = state
        self.add_state(state)
        
        return True
    
    @property
    def stateInfo(self):
        return self._stateInfo

    @stateInfo.setter
    def stateInfo(self, stateInfo):
        self._stateInfo = stateInfo
        ## Find the corresponding state and change the state
        for state in self._states:
            if state.isMatch(stateInfo):
                self.change_state(state)

class State(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def isMatch(self, stateInfo):
        return False

    @abstractmethod
    def behavior(self, context):
        pass

