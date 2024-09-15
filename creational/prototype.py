# Core or library code
class Prototype:
    """Responsible for unifying the interface for cloning an item"""

    def clone(self) -> "Prototype": ...


# Consumer or add-on code
class ConcretePrototype(Prototype):
    """Some clonable object"""

    def clone(self) -> "ConcretePrototype":
        print("Cloning a ConcretePrototype")
        return ConcretePrototype()


# Any component can make code like this (client, core, non-core)


class Client:
    def some_method(self, unknown_object: Prototype):
        """Does some stuff

        - We don't know our product, but we know how to get a copy of it
        """
        unknown_object_duplicate = unknown_object.clone()


if __name__ == "__main__":
    client = Client()
    client.some_function(ConcretePrototype())
