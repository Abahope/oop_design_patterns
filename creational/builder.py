# Core or library code
class Builder:
    """Responsible for determining the type of parts to be built"""

    def build_part_1(self): ...

    def build_part_2(self): ...

    def get_result(self): ...


class Director:
    """Responsible for determining what constitutes a full/lite product"""

    def build_full(self, builder: Builder):
        builder.build_part_1()
        builder.build_part_2()
        return builder.get_result()

    def build_lite(self, builder: Builder):
        builder.build_part_1()
        return builder.get_result()


# Consumer or add-on code
class ConcreteBuilderA(Builder):
    """Responsible for determining what parts to use"""

    product = []

    def build_part_1(self):
        print("I, ConcreteBuilderA, am going to add a special part 1")
        self.product += ["1"]

    def build_part_2(self):
        print("I, ConcreteBuilderA, am going to add a special part 2")
        self.product += ["2"]

    def get_result(self):
        out = self.product
        self.product = []
        return out


# Any component can make code like this (client, core, non-core)
def some_function(unknown_builder: Builder):
    """Does some stuff

    - We don't know: (1) our builder, (2) our product or (3) how our product
      gets created, but we know it's going to be a full product
    """
    director = Director()
    full_product = director.build_full(unknown_builder)
    print(f"full_product: {full_product}")

    lite_product = director.build_lite(unknown_builder)
    print(f"lite_product: {lite_product}")


if __name__ == "__main__":
    some_function(ConcreteBuilderA())
