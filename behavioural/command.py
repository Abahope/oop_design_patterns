from enum import Enum

# Core or library code

position = [0, 0]


class Command:
    """Responsible for unifying the interface for calling commands"""

    def execute(self): ...


# Consumer or add-on code
class KeysEnum(Enum):
    UP = "up"
    LEFT = "left"


class ReceiverUp:
    """Responsible for Up behavior"""

    def action(self):
        print("ReceiverUp action")
        position[1] += 1


class ReceiverUpReversal:
    """Responsible for reversing Up behavior"""

    def action(self):
        print("ReceiverUpReversal action")
        position[1] -= 1


class ReceiverLeft:
    """Responsible for Left behavior"""

    def action(self):
        print("ReceiverLeft action")
        position[0] -= 1


class ReceiverLeftReversal:
    """Responsible for reversing Left behavior"""

    def action(self):
        print("ReceiverLeftReversal action")
        position[0] += 1


class ConcreteCommandUp(Command):
    """Responsible for encapsulating some instructions"""

    def execute(self):
        print("ConcreteCommandUp execute")
        ReceiverUp().action()


class ConcreteCommandUpReversal(Command):
    """Responsible for encapsulating some instructions"""

    def execute(self):
        print("ConcreteCommandUpReversal execute")
        ReceiverUpReversal().action()


class ConcreteCommandLeft(Command):
    """Responsible for encapsulating some instructions"""

    def execute(self):
        print("ConcreteCommandLeft execute")
        ReceiverLeft().action()


class ConcreteCommandLeftReversal(Command):
    """Responsible for encapsulating some instructions"""

    def execute(self):
        print("ConcreteCommandLeftReversal execute")
        ReceiverLeftReversal().action()


class Invoker:
    """Responsible for managing the behavior"""

    def __init__(
        self,
        key_to_command: dict[KeysEnum, Command],
        key_to_command_reversal: dict[KeysEnum, Command],
    ):
        self.key_to_command = key_to_command
        self.key_to_command_reversal = key_to_command_reversal
        self.executed_commands = []

    def undo(self):
        last_executed = self.executed_commands.pop()
        self.key_to_command_reversal[last_executed].execute()

    def do_something(self, key: KeysEnum):
        self.key_to_command[key].execute()
        self.executed_commands.append(key)


# Any component can make code like this (client, core, non-core)


class Client:
    def some_method(self, invoker: Invoker):
        """Does some stuff
        -  We don't know who the actors/receivers are,
           but we can indirectly invoke them and undo
        """
        # start at state = 0
        # go to state = 1
        invoker.do_something(KeysEnum.UP)
        print("Position: ", position)
        # go to state = 2
        invoker.do_something(KeysEnum.LEFT)
        print("Position: ", position)
        # undo to state = 1
        invoker.undo()
        print("Position: ", position)


if __name__ == "__main__":
    invoker = Invoker(
        {
            KeysEnum.UP: ConcreteCommandUp(),
            KeysEnum.LEFT: ConcreteCommandLeft(),
        },
        {
            KeysEnum.UP: ConcreteCommandUpReversal(),
            KeysEnum.LEFT: ConcreteCommandLeftReversal(),
        },
    )
    Client().some_method(invoker)
