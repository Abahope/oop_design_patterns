# Core or library code
class Component:
    """Responsible for allowing uniform treatment of the hierarchy"""

    def operation(self): ...

    def add(self, c: "Component"): ...

    def remove(self, c: "Component"): ...

    def getChild(self, i: int): ...


# Consumer or add-on code
class Composite(Component):
    """Responsible for defining the hierarchy structure and propogating down behavior"""

    children: list[Component] = []

    def add(self, c: Component):
        self.children.append(c)

    def remove(self, c: Component):
        self.children.remove(c)

    def getChild(self, i: int):
        return self.children[i]

    def operation(self):
        print("Composite operation")
        for child in self.children:
            child.operation()


class Leaf(Component):
    """Response for implementing the operation's behavior"""

    def operation(self):
        print("Leaf operation")

    def add(self, c: Component):
        raise Exception("Leafs cannot add")

    def remove(self, c: Component):
        raise Exception("Leafs cannot remove")

    def getChild(self, i: int):
        raise Exception("Leafs do not have children")


# Any component can make code like this (client, core, non-core)
def some_function(component: Component):
    """Does some stuff

    - We don't know if our component is a Leaf or Composite, but we need
      to call the behavior for the component (and its children if applicable)
    """
    component.operation()
    try:
        child = component.getChild(0)
        print("child", child)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("Leaf")
    some_function(Leaf())
    print("Composite")
    composite = Composite()
    composite.add(Leaf())
    composite.add(Leaf())
    some_function(composite)
