# Core or library code


class Element:
    """Responsible for defining how to welcome a visitor"""

    def accept(self, v: "Visitor"): ...


class Visitor:
    """Responsible for enforcing visiting of all elements"""

    def visit_element_a(self, a: "ConcreteElementA"): ...

    def visit_element_b(self, b: "ConcreteElementB"): ...


# Consumer or add-on code
class ConcreteElementA(Element):
    """Responsible for welcoming a visitor"""

    def accept(self, v: "Visitor"):
        print("ConcreteElementA is welcoming the visitor")
        v.visit_element_a(self)


class ConcreteElementB(Element):
    """Responsible for welcoming a visitor"""

    def accept(self, v: "Visitor"):
        print("ConcreteElementB is welcoming the visitor")
        v.visit_element_b(self)


# Any component can make code like this (client, core, non-core)


class ConcreteVisitor(Visitor):
    """Responsible for integrating its behavior with the concrete elements"""

    def visit_element_a(self, a: ConcreteElementA):
        print("ConcreteVisitor is integrating its behavior with ConcreteElementA")

    def visit_element_b(self, b: ConcreteElementB):
        print("ConcreteVisitor is integrating its behavior with ConcreteElementB")


def some_function(visitor: Visitor, elements: list[Element]):
    """Does some stuff

    - We don't know the visitor or the elements, but we know the visitor
      can integrate its behavior with the elements
    """
    for el in elements:
        el.accept(visitor)


if __name__ == "__main__":
    some_function(ConcreteVisitor(), [ConcreteElementA(), ConcreteElementB()])
