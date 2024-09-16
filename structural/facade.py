# Core or library code


class ComponentA:
    """Responsible for behavior A"""

    def something_unique(self):
        print("ComponentA did something unique")


class ComponentB:
    """Responsible for behavior B"""

    def something_interesting(self):
        print("ComponentB did something interesting")


# Consumer or add-on code
class Facade:
    """Responsible for making ComponentA and ComponentB easier to use"""

    def __init__(self):
        self.a = ComponentA()
        self.b = ComponentB()

    def do_something_specific(self):
        self.a.something_unique()
        self.b.something_interesting()


# Any component can make code like this (client, core, non-core)


def some_function(facade: Facade):
    """Does some stuff

    - We don't know what our subsystem components are or how to call them,
      but we know how to talk to the facade.
    """
    facade.do_something_specific()


if __name__ == "__main__":
    some_function(Facade())
