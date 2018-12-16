class Car:

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def display(self):
        print("Color: {}\nSpeed: {}".format(self.color, self.speed))

    def repaint(self, color):
        print("Changing the car color from {} to {}".format(self.color, color))
        self.color = color


c1 = Car("Red", 150)
c1.display()
c1.speed = 200
c1.display()

c1.repaint("White")
c1.display()