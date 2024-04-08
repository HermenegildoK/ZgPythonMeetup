from typing import Protocol, runtime_checkable, TypeVar


@runtime_checkable
class SupportsRead(Protocol):

    def read(self) -> str:
        ...


@runtime_checkable
class ResponseProtocol(Protocol):
    def __enter__(self) -> SupportsRead:
        ...

    def __exit__(self, exc_type, exc_value, exc_tb):
        ...


@runtime_checkable
class SupportsCall(Protocol):
    def call(self, url: str) -> ResponseProtocol:
        ...


class MockIO:
    def __init__(self, url: str, response_string: str):
        self.url = url
        self.response = response_string

    def read(self) -> str:
        return f"Calling {self.url}. Response: {self.response}"


class MockResponse(ResponseProtocol):

    def __init__(self, url: str, mocked_response: str):
        self.url = url
        self.mocked_response = mocked_response

    def __enter__(self) -> SupportsRead:
        return MockIO(url=self.url, response_string=self.mocked_response)

    def __exit__(self, exc_type, exc_value, exc_tb):
        return None


class MockCallerImplicit:
    def call(self, url: str) -> ResponseProtocol:
        return MockResponse(url=url, mocked_response="Pero Implicit")


class MockCallerExplicit(SupportsCall):
    def call(self, url: str) -> ResponseProtocol:
        return MockResponse(url=url, mocked_response="Pero Explicit")


class FakeCall:

    def call(self):
        return "Fake!"


def call_something(caller: SupportsCall) -> str:
    with caller.call(url="https://duckduckgo.com/") as f:
        response = f.read()
    return response


S = TypeVar("S", bound=SupportsCall)


def call_and_print(caller: S) -> None:
    with caller.call(url="https://duckduckgo.com/") as f:
        response = f.read()
    print(response)


if __name__ == '__main__':
    # this fails mypy check:
    # error: Argument "caller" to "call_something" has incompatible type "object"; expected "SupportsCall"  [arg-type]
    for caller_implementation in [MockCallerExplicit(), MockCallerImplicit()]:
        print(call_something(caller=caller_implementation))
        call_and_print(caller=caller_implementation)

    # this does not:
    for caller_implementation in [MockCallerExplicit()]:
        print(call_something(caller=caller_implementation))
        call_and_print(caller=caller_implementation)

    # this fails mypy and raises runtime exception
    # call_something(caller=FakeCall())
    # call_and_print(caller=FakeCall())
