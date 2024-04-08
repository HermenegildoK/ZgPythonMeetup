import urllib.request
from typing import Protocol


class SupportsCall(Protocol):
    def call(self, url: str) -> str:
        ...


class ImplicitExample:
    def call(self, url: str) -> str:
        with urllib.request.urlopen(url=url) as f:
            return f.read()


class ExplicitExample(SupportsCall):
    def call(self, url: str) -> str:
        with urllib.request.urlopen(url=url) as f:
            return f.read()


if __name__ == '__main__':
    implicit = ImplicitExample()
    response_1 = implicit.call("https://duckduckgo.com/")
    print(response_1)

    explicit = ExplicitExample()

    response_2 = explicit.call("https://duckduckgo.com/")
    print(response_2)
