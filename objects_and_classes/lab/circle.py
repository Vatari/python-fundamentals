class Circle:
    def __init__(self, diameter):
        self.__pi = 3.14
        self.diameter = diameter
        self.radius = diameter / 2
        self.area = self.__pi * self.radius / 2

    def calculate_circumference(self):
        res = self.diameter * self.__pi
        return res

    def calculate_area(self):
        res = self.__pi * self.radius * self.radius
        return res

    def calculate_area_of_sector(self, angle):
        area = (angle / 360) * self.__pi * self.radius * self.radius
        return area


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
