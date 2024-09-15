# Core or library code
class AbstractProduct:
    """Responsible for unifying behavior of all products

    - Alternatively, you can create an abstract product for each type of product
      ie AbstractProductA, AbstractProductB. In my opinion, that is a more convincing
      usecase because it means that product A and product B are sufficiently different
      to warrant different classes.
    """

    ...


class AbstractFactory:
    """Responsible for determining what constitutes a set of compatible products"""

    def create_product_A(self) -> AbstractProduct: ...

    def create_product_B(self) -> AbstractProduct: ...


# Consumer or add-on code
class ConcreteProductGreenA(AbstractProduct):
    """Product A from the Green set"""

    def __repr__(self):
        return "GreenA"


class ConcreteProductGreenB(AbstractProduct):
    """Product B from the Green set"""

    def __repr__(self):
        return "GreenB"


class ConcreteFactoryGreen(AbstractFactory):
    """Responsible for determiing how products from the Green set get created"""

    def create_product_A(self) -> AbstractProduct:
        return ConcreteProductGreenA()

    def create_product_B(self) -> AbstractProduct:
        return ConcreteProductGreenB()


# Any component can make code like this (client, core, non-core)
def add_to_basket(products: list[AbstractProduct]):
    """Adds products to a basket"""
    print(f"Adding {products} to basket")


class Client:
    def some_method(self, unknown_factory_a: AbstractFactory):
        """Does some stuff


        - We don't know: (1) our factory, (2) our products or (3) how our product
          gets created, but we know our products are going to be a set under the factory
          /compatible
        """
        unknown_product_a = unknown_factory_a.create_product_A()
        unknown_product_b = unknown_factory_a.create_product_B()

        # We know they belong together
        add_to_basket([unknown_product_a, unknown_product_b])
        # You can also extend the product interface(s)
        # unknown_product_a.gracefully_interact_with(unknown_product_b)


if __name__ == "__main__":
    client = Client()
    client.some_method(ConcreteFactoryGreen())
