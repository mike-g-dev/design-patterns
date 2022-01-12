from flyweight import FlyweightFactory


def add_car_to_database(
        factory: FlyweightFactory,
        plates: str,
        owner: str,
        brand: str,
        model: str,
        color: str
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight({"brand": brand, "model": model, "color": color})
    flyweight.operation({"plates": plates, "owner": owner})