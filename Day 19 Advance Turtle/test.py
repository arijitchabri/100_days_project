from turtle import Turtle

tur = Turtle()


class MC(type):
    def _repr_(self):
        return 'Wahaha!'


class C(object):
    _metaclass_ = MC


print()
