# Core or library code
class Product:
    """Responsible for determining product family behaviors"""

    def do_family_thing(self): ...


class Creator:
    """Responsible for unifying the interface for creating products"""

    def create_product(self) -> Product: ...


# Consumer or add-on code
class ConcreteProductA(Product):
    """Unique product in a family"""

    def do_family_thing(self):
        print("I am ConcreteProductA and this is my special trick")


class ConcreteCreatorA(Creator):
    """Responsible for creating ConcreteProductA"""

    def create_product(self) -> ConcreteProductA:
        return ConcreteProductA()


# Any component can make code like this (client, core, non-core)
def some_function(unknown_creator: Creator):
    """Does some stuff

    - We don't know: (1) our creator, (2) product or (3) how our product
      gets created, but we can (a) delay creation up to this function and
      (b) still know what our product can do
    """
    unknown_concrete_product = unknown_creator.create_product()
    unknown_concrete_product.do_family_thing()


if __name__ == "__main__":
    some_function(ConcreteCreatorA())
