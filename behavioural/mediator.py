# Core or library code
class Colleague:
    """Responsible for unifying communication with mediator"""

    def inform(self, mediator: "Mediator", what_i_did: str): ...


class Mediator:
    """Responsible for unifying behavior coordination"""

    def receive(self, colleague: Colleague, what_colleague_did: str): ...


# Consumer or add-on code


def is_colleague_a(colleague: Colleague):
    return colleague.__class__.__name__ == "ConcreteColleagueA"


def is_colleague_b(colleague: Colleague):
    return colleague.__class__.__name__ == "ConcreteColleagueB"


class ConcreteMediator(Mediator):
    """Responsible for coordinating behavior"""

    def __init__(self, colleagues: list[tuple[str, "Colleague"]]):
        self.colleagues = {key: c for key, c in colleagues}

    def receive(self, colleague: Colleague, what_colleague_did: str):
        if is_colleague_a(colleague) and what_colleague_did == "give gift":
            colleague_b = self.colleagues["colleague_b"]
            assert isinstance(colleague_b, ConcreteColleagueB)
            colleague_b.say_thank_you(self)
        elif is_colleague_b(colleague) and what_colleague_did == "say thank you":
            print("Nothing to do here")


class ConcreteColleagueA(Colleague):
    """Responsible for some behavior"""

    def give_gift(self, mediator: "Mediator"):
        print("gave a gift")
        self.inform(mediator, "give gift")

    def inform(self, mediator: "Mediator", what_i_did: str):
        mediator.receive(self, what_i_did)


class ConcreteColleagueB(Colleague):
    """Responsible for some behavior"""

    def say_thank_you(self, mediator: "Mediator"):
        print("said thank you")
        self.inform(mediator, "say thank you")

    def inform(self, mediator: "Mediator", what_i_did: str):
        mediator.receive(self, what_i_did)


# Any component can make code like this (client, core, non-core)


class Client:
    def some_function(
        self,
        concrete_colleague_a: ConcreteColleagueA,
        concrete_colleague_b: ConcreteColleagueB,
        mediator: Mediator,
    ):
        """Calls the colleague's methods

        - We don't know the colleague's colleague or mediator,
          but we don't have to worry about coordinating the behavior
        """
        print("Calling concrete_colleague_a.give_gift(mediator)")
        concrete_colleague_a.give_gift(mediator)
        print("Calling concrete_colleague_b.say_thank_you(mediator)")
        concrete_colleague_b.say_thank_you(mediator)


if __name__ == "__main__":
    client = Client()
    concrete_colleague_a = ConcreteColleagueA()
    concrete_colleague_b = ConcreteColleagueB()
    mediator = ConcreteMediator(
        [("colleague_a", concrete_colleague_a),
         ("colleague_b", concrete_colleague_b)]
    )
    client.some_function(concrete_colleague_a, concrete_colleague_b, mediator)
