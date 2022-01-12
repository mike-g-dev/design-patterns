import json
from typing import Dict


class Flyweight:
    def __init__(self, shared_state: Dict) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: Dict) -> None:
        shared = json.dumps(self._shared_state)
        unique = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({shared}) and unique ({unique})")


class FlyweightFactory:
    _flyweights = Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict[str, Flyweight]) -> None:
        for state in initial_flyweights.items():
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        key = self.get_key(shared_state)
        if key not in self._flyweights:
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            flyweight = Flyweight(shared_state)
            self._flyweights[key] = flyweight
            return flyweight
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())))
