# This is a VERY simple demonstration of
# [Protocol](https://typing.readthedocs.io/en/latest/spec/protocol.html) and
# [Abstract Base Classes](https://docs.python.org/3/library/abc.html#module-abc)

from app.abc_examples.example_1 import example_1 as e_11, example_2 as e_12, example_3 as e_13
from app.abc_examples.examples_2 import example_1 as e_21, example_2 as e_22

if __name__ == '__main__':
    print("Starting!")
    print("ABC examples")
    e_11()
    try:
        e_12()
    except NotImplementedError as e:
        print(f"Calling app.abc_examples.examples_abc_1.example_2 failed with: {e.__class__}")
    e_13()

    print("Protocol examples")
    e_21()
    try:
        e_22()
    except TypeError as e:
        print(f"Calling app.abc_examples.examples_abc_2.example_2 failed with: {e}")
    print("Done!")
