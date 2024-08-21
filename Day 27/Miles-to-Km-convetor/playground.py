# def add(*a):
#     sum = 0
#     for i in a:
#         sum += i
#     return sum
#
# print(add(3,2,1))
#
# def my_function(*arg):
#     print(arg)
#
#
# my_function(1,2,3,4,5,6,7,8)

# class Car:
#     def __init__(self, **k):
#         self.make = k['w']
#
#
# my_car = Car(w='k')
#
# print(my_car.make)

def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)