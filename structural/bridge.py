# Core or library code


class Implementor:
    """Responsible for unifying an interface for the abstraction"""

    def operation_1_impl(self): ...


class Abstraction1:
    """Responsible for abstracting a functionality"""

    def __init__(self, implementor: Implementor):
        self.implementor = implementor

    def operation(self):
        self.implementor.operation_1_impl()


# Consumer or add-on code
class ConcreteImplementorA(Implementor):
    """Responsible for implementing a functionality"""

    def operation_1_impl(self):
        print("ConcreteImplementor operation_1_impl")


# Any component can make code like this (client, non-core)
def some_function(implementor):
    """Does some stuff

    - We rather not call the implementor directly because
      * we do not have insight to its type or behavior,
      * its interface changes regularly,
      * or the interface is out of our development control...
    - This way, the implementor can be changed without changing the client code
    """
    abstraction = Abstraction1(implementor)
    abstraction.operation()


if __name__ == "__main__":
    some_function(ConcreteImplementorA())
