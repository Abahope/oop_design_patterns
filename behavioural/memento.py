class Memento:
    """Responsible for holding information about state"""

    def __init__(self, my_state):
        self.my_state = my_state


class Originator:
    """Has some state it can afford to duplicate

    Responsible for
    - some behavior,
    - reinitalizing from memento,
    - creating a memento
    """

    def __init__(self, my_state):
        self.my_state = my_state

    def set_memento(self, memento: Memento):
        self.my_state = memento.my_state

    def create_memento(self):
        return Memento(my_state=self.my_state)

    def do_something(self):
        print("Some originator unique behavior")
        self.my_state += 1


class Caretaker:
    """Responsible for taking care of the state and using it to restore the originator

    - This may warrant becoming a core class if you have multiple originators
    """

    def __init__(self):
        self.mementos = []

    def restore_to_memento(self, originator: Originator, index: int):
        memento = self.mementos[index]
        originator.set_memento(memento)

    def save_memento(self, originator: Originator) -> Memento:
        memento = originator.create_memento()
        self.mementos.append(memento)
        return memento


def some_function(caretaker: Caretaker):
    originator = Originator(my_state=0)
    originator.do_something()
    caretaker.save_memento(originator)
    print("state after first and only save:", originator.my_state)
    # some time passes
    originator.do_something()
    originator.do_something()
    originator.do_something()
    originator.do_something()
    print("state before restore:", originator.my_state)
    # restore it to last saved state (state 1)
    caretaker.restore_to_memento(originator, -1)
    print("state after restore:", originator.my_state)


if __name__ == "__main__":
    caretaker = Caretaker()
    some_function(caretaker)
