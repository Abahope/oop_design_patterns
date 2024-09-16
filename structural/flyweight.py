# Core or library code


class Flyweight:
    """Responsible for allowing uniform treatment of the flyweights"""

    def operation(self, extrinsic_state): ...


def does_not_change_small_unshared_state(extrinsic_state: int): ...


class ConcreteFlyweight(Flyweight):
    """Responsible for managing the large shared state

    - If state changes here, it'll change state for all flyweights that use it
    """

    def __init__(self, large_shared_state: str):
        self._large_shared_state = large_shared_state

    @property
    def large_shared_state(self):
        """Allows reading the large shared state"""
        return self._large_shared_state

    @large_shared_state.setter
    def large_shared_state(self, value):
        """Prevents changing the large shared state"""
        raise AttributeError("Cannot set large_shared_state")

    def operation(self, extrinsic_state: int):
        print("ConcreteFlyweight does not need to respond to extrinsic state")

    def __repr__(self):
        original = super().__repr__()
        return f"{original} shared_state: {self.large_shared_state}"


class UnsharedConcreteFlyweight(Flyweight):
    """Responsible for managing some unique state"""

    def __init__(self, concrete_flyweight: ConcreteFlyweight,
                 unshared_state=0):
        self.concrete_flyweight = concrete_flyweight
        self.unshared_state = unshared_state

    def operation(self, extrinsic_state: int):
        if does_not_change_small_unshared_state(extrinsic_state):
            return
        # Now use extrinsic state to change the small unshared state
        self.unshared_state += extrinsic_state
        # If necessary, can also access concrete_flyweight.large_shared_state
        # here

    def __repr__(self):
        original = super().__repr__()
        return f"{original}, unshared_state: {self.unshared_state}, shared_state: {self.concrete_flyweight.large_shared_state}"


class FlyweightFactory:

    def __init__(self):
        self.key_to_concrete_flyweight = {}

    def get_flyweight(self, key) -> Flyweight:
        if key not in self.key_to_concrete_flyweight:
            large_shared_state = "some large shared state"
            self.key_to_concrete_flyweight[key] = ConcreteFlyweight(
                large_shared_state)
            return self.key_to_concrete_flyweight[key]
        return UnsharedConcreteFlyweight(
            concrete_flyweight=self.key_to_concrete_flyweight[key]
        )


# Any component can make code like this (client, core, non-core)
def flyweight_creation(flyweight_factory: FlyweightFactory) -> list[Flyweight]:
    key = "some key"
    # The first one will be concrete
    concrete_flyweight = flyweight_factory.get_flyweight(key=key)
    # Subsequent ones will be unshared
    unshared_concrete_flyweight_1 = flyweight_factory.get_flyweight(key=key)
    unshared_concrete_flyweight_2 = flyweight_factory.get_flyweight(key=key)
    flyweights = [
        concrete_flyweight,
        unshared_concrete_flyweight_1,
        unshared_concrete_flyweight_2,
    ]
    return flyweights


def manipulate_flyweights(flyweights: list[Flyweight], extrinsic_state: int):
    """Does some stuff

    - We don't know which of our flyweights contain the large immutable shared state,
      but we can treat them uniformly
    """
    for f in flyweights:
        f.operation(extrinsic_state)


if __name__ == "__main__":
    flyweights = flyweight_creation(FlyweightFactory())
    print("Before manipulate_flyweights")
    for f in flyweights:
        print(f)
    manipulate_flyweights(flyweights=flyweights, extrinsic_state=1)
    print("After manipulate_flyweights 1")
    for f in flyweights:
        print(f)
