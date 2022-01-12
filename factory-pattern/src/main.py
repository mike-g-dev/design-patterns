from use_cases import some_use_case
from creator import ConcreteCreatorOne, ConcreteCreatorTwo


def main() -> None:
    some_use_case(ConcreteCreatorOne())
    some_use_case(ConcreteCreatorTwo())


if __name__ == "__main__":
    main()