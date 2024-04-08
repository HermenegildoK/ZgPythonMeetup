from abc import ABC, abstractmethod


class PeroBase(ABC):

    @abstractmethod
    def count_bugs(self, bugs_list):
        ...


class Jure(PeroBase):
    def count_bugs(self, bugs_list):
        return len([b for b in bugs_list if b.failed])


class Duje(PeroBase):
    pass


class Bug:
    def __init__(self, failed):
        self.failed = failed


bugs = [Bug(failed=True), Bug(failed=False), Bug(failed=True), Bug(failed=False)]


def example_1():
    jure = Jure()
    print(jure.count_bugs(bugs_list=bugs))


# if we uncomment this we can not even import this module
# duje = Duje()

def example_2():
    duje = Duje()
    print(duje.count_bugs(bugs_list=bugs))


if __name__ == '__main__':
    print("Starting!")
    example_1()
    # uncomment to see how it fails
    # example_2()
