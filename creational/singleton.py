# Any component can make code like this (client, core, non-core)
class Singleton:
    """Responsible for ensuring a max of one instance and providing access to it"""

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        print("Gotcha: init is called even if we do not create a new instance")
        if not self._initialized:
            # subscribe to a realtime data queue (represented by this stack)
            self.stack = [5, 4, 3, 2, 1]
            self._initialized = True


# Any component can make code like this (client, core, non-core)
class Client:
    def some_method(self):
        """Does some stuff"""
        singleton_instance_1 = Singleton()
        assert singleton_instance_1.stack.pop() == 1
        singleton_instance_2 = Singleton()
        # We get the same instance as evidenced by the stack pop response
        assert singleton_instance_2.stack.pop() == 2
        assert singleton_instance_1.stack.pop() == 3
        print("Success")


if __name__ == "__main__":
    client = Client()
    client.some_function()
