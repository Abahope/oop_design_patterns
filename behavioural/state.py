# Core or library code


class State:
    """Responsible for unifying the state call"""

    def handle(self, event): ...


# Consumer or add-on code
class ConcreteState1(State):
    """Responsible for handling events in a specific way"""

    def handle(self, event):
        print("Handling event in ConcreteState1")


class ConcreteState2(State):
    """Responsible for handling events in a different specific way"""

    def handle(self, event):
        print("Handling event in ConcreteState2")


class Context:
    """Responsible for determining which concrete state class gets called"""

    def __init__(self, state_to_handler: dict[str, State]):
        self.state = "basic_state"
        self.state_to_handler = state_to_handler

    def request(self, event):
        self.state_to_handler[self.state].handle(event)


# Any component can make code like this (client, core, non-core)


def some_function(event: str, context: Context):
    """Does some stuff

    - We don't know what handlers are in the context, but we know that
      its state will determine how it handles the request
    """
    print(f"Sending event {event} in state {context.state}")
    context.request(event)
    # change the behavior of the context
    context.state = "advanced_state"
    print(f"Sending event {event} in state {context.state}")
    context.request(event)


if __name__ == "__main__":
    state_to_handler = {
        "basic_state": ConcreteState1(),
        "advanced_state": ConcreteState2(),
    }
    context = Context(state_to_handler)
    some_function("some_event", context)
