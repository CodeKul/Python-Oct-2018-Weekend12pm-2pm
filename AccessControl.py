class A:
    def __init__(self, a, b, c):
        self.a = a #Public
        self._b = b #Protected
        self.__c = c #Private

    def display(self):
        print('A: {}'.format(self.a))
        print('B: {}'.format(self._b))
        print('C: {}'.format(self.__c))

    def set_a(self, a):
        self.a = a
    
    def _set_b(self, b):
        self._b = b

    def __set_c(self, c):
        self.__c = c

objA = A(10, 20, 30)

objA.display()

objA.set_a(100)
objA._set_b(200)
objA.__set_c(300)

objA.display()