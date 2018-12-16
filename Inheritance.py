import math

class Polygon:

    def __init__(self, no_sides):
        self.no_sides = no_sides
        self.sides = []

    def input_sides(self):
        for n in range(self.no_sides):
            side = input('Enter side{}: '.format(n+1))
            self.sides.append(side)

    def display(self):
        print('Number of sides: {}\nSides: '.format(self.no_sides))
        for side in self.sides:
            print(side)

    def perimeter(self):
        sum_sides = 0
        for side in self.sides:
            sum_sides += side

        return sum_sides

# p1 = Polygon(6)
# p1.input_sides()
# p1.display()
# print(p1.perimeter())

class Triangle(Polygon):

    def __init__(self):
        Polygon.__init__(self, 3)
    
    def area(self):
        p = self.perimeter()/2.0
        sq_area = p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2])
        print(p)
        return math.sqrt(sq_area)

# t1 = Triangle()
# t1.input_sides()
# t1.display()
# print('Area: {}'.format(t1.area()))

class Rectangle(Polygon):

    def __init__(self):
        Polygon.__init__(self, 4)
    
    def input_sides(self):
        length = input("Enter Length: ")
        breadth = input("Enter Breadth: ")
        for n in range(self.no_sides):
            if n % 2 == 0:
                self.sides.append(length)
            else:
                self.sides.append(breadth)

    def area(self):
        return(self.sides[0]*self.sides[1])
        

# r1 = Rectangle()
# r1.input_sides()
# r1.display()
# print('Area: {}'.format(r1.area()))


class Square(Rectangle):
    def __init__(self):
        Rectangle.__init__(self)
    
    def input_sides(self):
        side = input("Enter Side: ")
        for n in range(self.no_sides):
            self.sides.append(side)

    def area(self):
        return(self.sides[0]**2)
    

s1 = Square()
s1.input_sides()
s1.display()
print('Area: {}'.format(s1.area()))
