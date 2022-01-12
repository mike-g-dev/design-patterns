from factory import AbstractFactory


def some_use_case(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"useful function = {product_a.useful_function()}")
    print(f"another useful function = {product_b.another_useful_function()}")