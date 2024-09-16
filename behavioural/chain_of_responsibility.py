import random
from typing import Optional


# Core or library code


class Handler:
    """Responsible for defining how the handlers can be chained and called"""

    def __init__(self, successor: Optional["Handler"] = None):
        self.successor = successor

    def i_will_handle_request(self, request) -> bool: ...

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)
        else:
            print("No successor to handle the request")


# Consumer or add-on code


class ConcreteHandler1(Handler):
    """One way to handle a request"""

    def i_will_handle_request(self, request) -> bool:
        true_or_false = bool(random.getrandbits(1))
        if true_or_false:
            print("ConcreteHandler1 will handle the request")
        else:
            print("ConcreteHandler1 will not handle the request")
        return true_or_false

    def handle_request(self, request):
        if self.i_will_handle_request(request):
            print("ConcreteHandler1 handled the request")
        else:
            super().handle_request(request)


class ConcreteHandler2(Handler):
    """One way to handle a request"""

    def i_will_handle_request(self, request) -> bool:
        true_or_false = bool(random.getrandbits(1))
        if true_or_false:
            print("ConcreteHandler2 will handle the request")
        else:
            print("ConcreteHandler2 will not handle the request")
        return true_or_false

    def handle_request(self, request):
        if self.i_will_handle_request(request):
            print("ConcreteHandler2 handled the request")
        else:
            super().handle_request(request)


# Any component can make code like this (client, core, non-core)


class Client:
    def some_method(self, handler: Handler):
        """Does some stuff

        - We don't know which handler, if any, will handle the request
        """
        handler.handle_request({"type": "A", "msg": "do something"})


if __name__ == "__main__":
    # we can chain the handlers however we want, dynamically
    handler_chain_a = ConcreteHandler1(ConcreteHandler2())
    handler_chain_b = ConcreteHandler2()

    print("Handler chain A:")
    Client().some_function(handler_chain_a)
    print("Handler chain B:")
    Client().some_function(handler_chain_b)
