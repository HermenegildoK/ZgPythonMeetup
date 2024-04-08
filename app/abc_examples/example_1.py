from abc import ABC
from collections.abc import Iterator


class PeroBase(ABC):

    def count_bugs(self, bugs):
        raise NotImplementedError


class Jure(PeroBase):
    def count_bugs(self, bugs):
        return len([b for b in bugs if b.failed])


class Duje(PeroBase):
    pass


class Bug:
    def __init__(self, failed):
        self.failed = failed


bugs_list = [Bug(failed=True), Bug(failed=False), Bug(failed=True), Bug(failed=False)]


def example_1():
    jure = Jure()
    print(jure.count_bugs(bugs=bugs_list))


def example_2():
    duje = Duje()
    print(duje.count_bugs(bugs=bugs_list))


def example_3():
    class Stipe:
        def __next__(self):
            'Return the next item from the iterator. When exhausted, raise StopIteration'
            raise StopIteration

        def __iter__(self):
            return self

    stipe = Stipe()
    print(isinstance(stipe, Iterator))


if __name__ == '__main__':
    example_1()
    example_2()
    example_3()
