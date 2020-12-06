
class Square:
    square_list = []

    def __init__(self, len):
        self.len = len
        self.square_list.append(self)

    def __repr__(self):
        sl = str(self.len)
        return "{} by {} by {} by {}".format(sl, sl, sl, sl)

class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

class Person:
    def __init__(self):
        self.name = 'Bob'

def isSame(obj1, obj2):
    return obj1 is obj2

sq1 = Square(10)
sq2 = sq1
sq3 = Square(10)

print(isSame(sq1, sq2))
print(isSame(sq1, sq3))