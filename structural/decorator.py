# Core or library code
class Component:
    """Responsible for unifying the interface for concrete components and decorators"""

    def operation(self): ...


class Decorator(Component):
    """Responsible for defining the link between the decorator and decoratee"""

    def __init__(self, component: Component):
        self.component = component

    def operation(self): ...


# Consumer or add-on code


class ConcreteComponent(Component):
    """Responsible for some undefined behavior"""

    def operation(self):
        print("I can do this")


class ConcreteDecoratorN(Decorator):
    """Responsible for adding some behavior"""

    def added_behavior(self):
        print("I can do N")

    def operation(self):
        self.added_behavior()
        self.component.operation()


# Any component can make code like this (client, core, non-core)


def some_function(component: Component):
    """Does some stuff

    - We don't know what our component is, but we know how to add behaviors to it
    - We can also take in a decorator class as input
    """
    print("Initial component behavior:")
    component.operation()
    print("-" * 10)
    print("decorating component with N")
    component_v2 = ConcreteDecoratorN(component)
    print("Component with N behavior:")
    component_v2.operation()
    # We can layer on additional behaviors
    print("-" * 10)
    print("decorating component with N")
    component_v3 = ConcreteDecoratorN(component_v2)
    print("Component with N behavior:")
    component_v3.operation()


if __name__ == "__main__":
    component = ConcreteComponent()
    some_function(component)
