from abc import abstractmethod


class Pentagon:
    @abstractmethod
    def pentagon(self):
        pass


class Triangle(Pentagon):
    def pentagon(self):
        print("it has 4 sides")


class Polygon(Pentagon):
    def pentagon(self):
        print("it has 5 sides")


class Hexagon(Pentagon):
    def pentagon(self):
        print("it has 4 sides")


class Quadrilateral(Pentagon):
    def pentagon(self):
        print("it has 5 sides")


a = Triangle()
a.pentagon()
a = Quadrilateral()
a.pentagon()
a = Hexagon()
a.pentagon()
a = Polygon()
a.pentagon()