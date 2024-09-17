# Core or library


class Strategy:
    """Responsible for unifying how a behavior is called"""

    def execute(self): ...


# Consumer or add-on code


class ConcreteStrategyA(Strategy):
    """Responsible for encapsulating a behavior"""

    def execute(self):
        print("Executing strategy A")


class ConcreteStrategyB(Strategy):
    """Responsible for encapsulating another behavior"""

    def execute(self):
        print("Executing strategy B")


# Any component can make code like this (client, core, non-core)


class Context:
    """Responsible for some behavior that can be different based on strategy"""

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def do_something(self):
        print("Context is doing something")
        print("Context is going to use strategy")
        self.strategy.execute()


def some_function(strategy: Strategy):
    """Does some stuff

    - We don't know how the strategy works, but we know the context can use
      it
    """
    context = Context(strategy)
    context.do_something()


if __name__ == "__main__":
    print("Using strategy A")
    some_function(ConcreteStrategyA())
    print("Using strategy B")
    some_function(ConcreteStrategyB())
