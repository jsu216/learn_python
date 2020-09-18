class Things:
    def __init__(self, name):
        self.name = name


class Animate(Things):
    pass


class Animals(Animate):
    def breathe(self):
        print(f"{self.name} is breathing")

    def move(self):
        print(f"{self.name} is moving")

    def eat_food(self):
        print(f"{self.name} is eating")


class Mammals(Animals):
    def feed_young_with_milk(self):
        print(f"{self.name} is feed young with milk")


class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print(f"{self.name} is eating leaves")


jason = Giraffes("Jason")
jason.move()
jason.eat_leaves_from_trees()

jeremy = Giraffes("Jeremy")
jeremy.move()
jeremy.eat_leaves_from_trees()
