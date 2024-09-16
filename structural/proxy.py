import random

# Core or library code


class Subject:
    """Subject interface

    Responsible for defining interface of real subject,
    but also used to ensure proxies implement real subject's interface
    """

    def request(self): ...


class RealSubject:
    """Responsible for some behavior"""

    def request(self):
        print("RealSubject did something")


# Consumer or add-on code


class Proxy(Subject):
    """Responsible for controlling access to some real subject"""

    def __init__(self, real_subject: RealSubject):
        self.real_subject = real_subject

    def additional_behavior(self):
        print("Proxy did some additional behavior")

    def the_stars_align(self):
        true_or_false = bool(random.getrandbits(1))
        if true_or_false:
            print("The stars align")
        else:
            print("The stars do not align")
        return true_or_false

    def request(self):
        self.additional_behavior()
        if self.the_stars_align():
            self.real_subject.request()


# Any component can make code like this (client, core, non-core)


def some_function(subject: Subject):
    """Does some stuff

    - We don't know if we received a real subject or a proxy
    """
    subject.request()


if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    some_function(proxy)
