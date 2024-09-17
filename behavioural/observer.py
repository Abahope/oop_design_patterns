# Core or library code


class Observer:
    """Responsible for defining how to respond to notifications"""

    def update(self, message: str): ...


class Subject:
    """Responsible for defining how take in subscribers, remove subscribers, and notify them of events"""

    def attach(self, observer: Observer): ...

    def detach(self, observer: Observer): ...

    def notify(self): ...


# Consumer or add-on code


class ConcreteSubject(Subject):
    """Responsible for taking in subscribers, removing subscribers, and notifying them of events"""

    def __init__(self):
        self.observers = []
        self.subject_state = "something"

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        idx = self.observers.index(observer)
        self.observers.pop(idx)

    def notify(self, message: str):
        for observer in self.observers:
            observer.update(message)

    def change_state(self, message: str):
        self.subject_state = message
        self.notify(message)


class ConcreteObserver(Observer):
    """Responsible for responding to notifications"""

    def __init__(self, id: int, observer_state: str):
        self.id = id
        self.observer_state = observer_state

    def update(self, message: str):
        self.observer_state += " " + message
        print(f"Observer {self.id} state updated to: {self.observer_state}")


# Any component can make code like this (client, core, non-core)


def some_function(subject: ConcreteSubject, observers: list[ConcreteObserver]):
    """Does some stuff"""
    for observer in observers:
        subject.attach(observer)
    # Change state (and notify observers)
    print("Changing subject state to A")
    subject.change_state("A")
    print("Detaching observer 1")
    subject.detach(observers[0])
    print("Changing subject state to B")
    subject.change_state("B")


if __name__ == "__main__":
    subject = ConcreteSubject()
    observer_1 = ConcreteObserver(1, "1 -")
    observer_2 = ConcreteObserver(2, "2 -")
    some_function(subject, [observer_1, observer_2])
