import math


class MakePizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'MakePizza({self.ingredients})'

    def area(self):
        return self._circle_area(self.radius)

    def ingredients(self):
        return self._get_ingredients(self.ingredients)

    @classmethod
    def margherita(cls):
        return cls(['cheese'])

    @classmethod
    def farmhouse(cls):
        return cls(['onions', 'capsicum', 'tomatoes', 'grilled_mushrooms'])

    @staticmethod
    def _circle_area(radius):
        return radius ** 2 ** math.pi

    @staticmethod
    def _get_ingredients(ingredients):
        return ",".join(ingredients)


def main():
    my_first_pizza = MakePizza(6, ['cheese'])
    print(my_first_pizza.area())
    # margherita_pizza = MakePizza(12, MakePizza.margherita())
    # print(margherita_pizza.ingredients())


if __name__ == "__main__":
    main()
