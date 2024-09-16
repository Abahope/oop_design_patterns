# Core or library code
class Iterator:
    """Responsible for defining how to iterate through a list"""

    def next(self) -> str | int: ...


class Aggregate:
    """Responsible for defining how to create an interator and get data"""

    def create_iterator(self) -> Iterator: ...

    def get(self, ptr: str | int): ...


# Consumer or add-on code


class ConcreteIterator(Iterator):
    """Responsible for keeping track of the iteration state"""

    def __init__(self):
        self.ptr = 0

    def next(self):
        res = self.ptr
        self.ptr += 1
        return res


class ConcreteAggregate(Aggregate):
    """Responsible for holding and allowing access to some data"""

    def __init__(self):
        self.data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get(self, ptr: int):
        return self.data[ptr]

    def create_iterator(self) -> Iterator:
        return ConcreteIterator()


# Any component can make code like this (client, core, non-core)


class Client:
    def some_method(self, aggregate: Aggregate):
        """Does some stuff

        - We don't know where the data is or how it's organized,
          but we know how to iterate through it
        - We can also have multiple iteration states
        """
        iterator_1 = aggregate.create_iterator()
        iterator_2 = aggregate.create_iterator()
        data_0 = aggregate.get(iterator_1.next())
        print("data_0 from iterator_1", data_0)
        data_1 = aggregate.get(iterator_1.next())
        print("data_1 from iterator_1", data_1)
        data_0_from_iterator_2 = aggregate.get(iterator_2.next())
        print("data_0_from_iterator_2", data_0_from_iterator_2)


if __name__ == "__main__":
    Client().some_method(ConcreteAggregate())
