"""
This in a executable script that is responsible for
performing some_use_case using two different factories. Note that this
executable only depends on use_case.py and factory.py -- "our"
modules which encapsulate the procedural logic as well as any other external
dependencies needed.
"""
from use_case import some_use_case
from factory import FactoryOne, FactoryTwo


def main() -> None:
    some_use_case(FactoryOne())
    some_use_case(FactoryTwo())


if __name__ == "__main__":
    main()
