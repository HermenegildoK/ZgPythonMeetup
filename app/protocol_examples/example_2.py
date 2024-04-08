import urllib.request
from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsCall(Protocol):
    def call(self, url):
        ...


class ImplicitExample:
    def call(self, url):
        return urllib.request.urlopen(url=url)


class ExplicitExample(SupportsCall):
    def call(self, url):
        return urllib.request.urlopen(url=url)


if __name__ == '__main__':
    implicit = ImplicitExample()
    request_1 = implicit.call("https://duckduckgo.com/")
    print(request_1.headers)

    explicit = ExplicitExample()

    request_2 = explicit.call("https://duckduckgo.com/")
    print(request_2.headers)

    # without decorator this fails with:
    # TypeError: Instance and class checks can only be used with @runtime_checkable protocols
    print(isinstance(implicit, SupportsCall))
    print(isinstance(explicit, SupportsCall))
