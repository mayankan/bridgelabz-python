import math


class MakePizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'MakePizza({self.ingredients})'

    def area(self):
        return self._circle_area(self.radius)

    @classmethod
    def margherita(cls):
        return cls(['cheese'])

    @classmethod
    def farmhouse(cls):
        return cls(['onions', 'capsicum', 'tomatoes', 'grilled_mushrooms'])

    @staticmethod
    def _circle_area(r):
        return r ** 2 ** math.pi


def main():
    MakePizza(6, ['cheese']).area()


if __name__ == "__main__":
    main()
