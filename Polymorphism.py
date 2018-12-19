class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{} is eating...'.format(self.name))


class Tiger:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{} is eating...'.format(self.name))


def feedAnimal(animal):
    print(animal.__class__)
    animal.eat()


dog = Dog('Tommy')
tiger = Tiger('John')

feedAnimal(dog)
feedAnimal(tiger)