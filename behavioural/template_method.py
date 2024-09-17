class AbstractClass:
    """Responsible for enforcing implemention of sub_method and using it"""

    def sub_method(self):
        raise NotImplementedError("Sub method must be implemented")

    def template_method(self):
        print("AbstractClass is doing something common")
        self.sub_method()
        print("AbstractClass is doing something common")


class ConcreteClass(AbstractClass):
    """Responsible for implementing the sub_method"""

    def sub_method(self):
        print("ConcreteClass is doing something varying")


def some_function(obj: AbstractClass):
    """Does some stuff

    - We know how template_method is implemented,
      but we don't know what sub_method will be called
    """
    obj.template_method()


if __name__ == "__main__":
    some_function(ConcreteClass())
