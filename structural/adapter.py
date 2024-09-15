# Core or library code
class Adapter:
    """Responsible for unifying an interface for the client"""

    def operation(self): ...


# Add-on code
class Adaptee:
    def adapted_operation(self):
        print("Compensating operation")


class ConcreteAdapter(Adapter):
    """Responsible for adapting the adaptee to the client"""

    adaptee = Adaptee()

    def operation(self):
        # Maybe modify input here for adaptee
        print("Adapter operation")
        self.adaptee.adapted_operation()


# Any component can make code like this (client, core, non-core)
class Client:
    def some_method(self, adapter: Adapter):
        """Does some stuff

        - We don't know our adaptee/its interface, but we know how to call it
        """
        adapter.operation()


if __name__ == "__main__":
    client = Client()
    adapter = ConcreteAdapter()
    client.some_function(adapter)
