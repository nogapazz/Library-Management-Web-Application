# class test():
#     def __init__(self):
#         self.x = 0
#
# class dtest(test):
#     pass
#
# def main():
#     b = dtest()
#     print(b.x)
# main()


# class MyClass:
#     def __init__(self):
#         self.__x = 5 # this is a private variable
#         self.y = 10 # this is a public variable
#         self._z = 2
#
#     def __privateMethod(self):
#         print(self.__x +  self._z)
# obj = MyClass()
# print(obj.__x) # this will raise an AttributeError
# print(obj._MyClass__x) # this will work and print 5
# print (obj._z) # this will work and print 10
# MyClass()._MyClass__privateMethod() #this will work and print 7



# class demo:
#     def __init__(self):
#         self.a = 1
#         self.__b = 1
#
#     def tomer(self):
#         return self.__b
#
#
# k = demo()
# print(k.tomer()) #this will work and print 1


#
# class position:
#     def __init__(self, name, salary=9000):
#         self.name = name
#         self.salary = salary
#     def show(self):
#         print(self.name, self.salary)
#
# welder = position('welder', 10000)
# driver = position('driver')
# welder.show() # output: welder 10000
# driver.show() # output: driver 9000
#
#
#
# class taxitem(object):
#     tax_rate = 0.23
#     def __init__(self, percent):
#         self.percent = percent
#     def calc_tax(self):
#         pass
#
#
#
# class offshore(position, taxitem):
#     def __init__(self, name, salary, percent, country):
#         position.__init__(self, name, salary)
#         taxitem.__init__(self, percent)
#         self.consractor = constractor
#         self.country = country
#     def show(self):
#         position.show(self)
#         print(self.name + '' + self.country)
#     def check_is_country(self, country):
#         if (self.country == country):
#             return True
#     def calc_tax(self):
#         return self.salary * self.tax_rate
#
#
# a = offshore('driver', 10000, 0.25, 'israel')
# print(a.name)


# class bird:
#     def flight(self):
#         print('there are many types of birds')
#
# class sparrow(bird):
#     def flight(self):
#         print('sparrows can fly')
#
# bird = bird()
# sparrow = sparrow()
#
# bird.flight()
# sparrow.flight()
# bird.flight()

################################################### Setattr() #####################################################################

#
# class person:
#     def __init__(self):
#         name = 'jack'
#         age = 36
#         country = 'norway'
#
# setattr(person, 'age', 40)
#
# x = person()
# print(x.age) #40
#
#
#
#
# class person:
#     def __init__(self, name, age, country):
#         self.name = name
#         setattr(self, 'age', age)
#         self.country = country
#
# x = person('john', 36, 'norway')
# print(x.age) # 36
# setattr(x, 'age', 40)
# print(x.age) # 40
#
#
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person('John', 30)
# print(p1.age) # 30
# setattr(p1, 'age', 35)
# print(p1.age) # 35
#

####################################################################################################################################

#
# class OnlyOne(object):
#     class __InstanceOne:
#         def __init__(self):
#             self.val = None
#         def get_val(self):
#             return  self.val
#     instance = None
#     def __new__(cls): # __new_ always a classmethod
#         print('new')
#         if not OnlyOne.instance:
#             OnlyOne.instance = OnlyOne.__InstanceOne()
#         return OnlyOne.instance
#     def __getattr__(self, name):
#         return getattr(self.instance, name)
#     def __setattr__(self, name):
#         return setattr(self.instance, name)
#
# x = OnlyOne()
# x.val = 'sausage'
# print(x.get_val())
# y = OnlyOne()
# y.val = 'eggs'
# print(y.get_val())
# z = OnlyOne()
# z.val = 'spam'
# print(z.get_val())
# print(y.get_val())
# print(x.get_val())
#
#
#
#
# class OnlyOne:
#     class __InstanceOne:
#         def __init__(self, arg):
#             self.val = arg
#         def get_val(self):
#             return  self.val
#     instance = None
#     def __init__(self, arg):
#         if not OnlyOne.instance:
#             OnlyOne.instance = OnlyOne.__InstanceOne(arg)
#         else:
#             OnlyOne.instance.val = arg
#     def __getattr__(self, name):
#         return getattr(self.instance, name)
#
# x = OnlyOne('sausage')
# print(x.get_val())
# y = OnlyOne('eggs')
# print(y.get_val())
# z = OnlyOne('spam')
# print(z.get_val())
# print(x.get_val())
# print(y.get_val())

# class Borg:
#     _shared_state = {}
#     def __init__(self):
#         self.__dict__ = self._shared_state
#
# class Singleton(Borg):
#     def __init__(self, arg):
#         Borg.__init__(self)
#         self.val = arg
#     def get_val(self):
#         return  self.val
#
# x = Singleton('sausage')
# print(x.get_val())
# y = Singleton('eggs')
# print(y.get_val())
# z = Singleton('spam')
# print(z.get_val())
# print(x.get_val())
# print(y.get_val())
#


# class OnlyOne:
#     class __InstanceOne:
#         def __init__(self, n, s):
#             self.n = n
#             self.s = s
#
#         def getSN(self):
#             ss = ""
#             for i in range(self.n):
#                 ss = ss + self.s + " "
#             return ss
#
#         def setN(self, n):
#             self.n = n
#
#         def setS(self, s):
#             self.s = s
#
#     instance = None
#
#     def __init__(self, n, s):
#         if not OnlyOne.instance:
#             OnlyOne.instance = OnlyOne.__InstanceOne(n, s)
#         else:
#             OnlyOne.instance.n = n
#             OnlyOne.instance.s = s
#
#     def __getattr__(self, name):
#         return getattr(self.instance, name)
#
#     def __setattr__(self, name, value):
#         return setattr(self.instance, name, value)
#
#
# x = OnlyOne(3, "hi")
# x.n = 2  #changes the n value of x to be 2
# print(x.getSN())
# y = OnlyOne(4, "bye!")
# print(y.getSN())
# print(x.getSN())
# x.setN(6)
# print(y.getSN())
# y.setS("LOL")
# print(x.getSN())
#


# class test:
    # _instance = None
    # def __new__(cls, a):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls, a)
    #     return cls._instance

#     def __init__(self, a):
#         self.a = str(a)
#
#
# x = test(3)
# print(x.a)
#

#
# class OnlyOne(object):
#     class __InstanceOne:
#         def __init__(self):
#             self.val = None
#
#         def get_val(self):
#             return self.val
#
#     instance = None
#
#     def __new__(cls):  # __new_ always a classmethod
#         print('new')
#         if not OnlyOne.instance:
#             OnlyOne.instance = OnlyOne.__InstanceOne()
#         return OnlyOne.instance
#
# x = OnlyOne()
# x.val = 'sausage'
# print(x.get_val())
# y = OnlyOne()
# y.val = 'eggs'
# print(y.get_val())
# z = OnlyOne()
# z.val = 'spam'
# print(z.get_val())
# print(y.get_val())
# print(x.get_val())


# def italicize(f):
#     def wrapper():
#         return '<i>' + f() + '<i>'
#     return wrapper
#
#
# def b(italicize):
#     def inner():
#         return '<b>' + italicize() + '<b>'
#     return inner
#
#
# @b
# @italicize
# def sayHi():
#     return 'hi there!'
#
# print(sayHi())
#
# class ScoreBoard:
#     class __istanceOne:
#         def __init__(self):
#             self.a = 0
#             self.b = 0
        # def UpdatescoreTeamA(self, arg):
        #     self.a = self.a + arg
        #     return self.a
        # def UpdatescoreTeamB(self,arg):
        #     self.b = self.b + arg
        #     return self.b
#         def Printscore(self):
#             print(f'the score is: (A - {self.a}, B - {self.b} )')
#     instance = None
#     def __init__(self):
#         if not ScoreBoard.instance:
#             ScoreBoard.instance = ScoreBoard.__istanceOne()
#     def __getattr__(self, item):
#         return getattr(self.instance, item)
#
# #
#
# mazcirut1 = ScoreBoard()
# mazcirut2 = ScoreBoard()
# mazcirut1.Printscore()
# setattr(mazcirut1.__istanceOne, 'a', 5)
# mazcirut1.Printscore()
# mazcirut1.UpdatescoreTeamA(2)
# mazcirut1.PrintScore()
# mazcirut1.UpdatescoreTeamA(3)




# class ScoreBoard:
#     class __istanceOne:
#         def __init__(self):
#             self.a = 0
#             self.b = 0
#         def UpdatescoreTeamA(self, arg):
#             self.a = self.a + arg
#             return self.a
#         def UpdatescoreTeamB(self,arg):
#             self.b = self.b + arg
#             return self.b
#         def Printscore(self):
#             print(f'the score is: (A - {self.a}, B - {self.b} )')
#     instance = None
#     def __new__(cls):
#         if not ScoreBoard.instance:
#             ScoreBoard.instance = ScoreBoard.__istanceOne()
#         return ScoreBoard.instance
#
#
# mazcirut1 = ScoreBoard()
# mazcirut2 = ScoreBoard()
# mazcirut1.Printscore()
# mazcirut1.UpdatescoreTeamA(2)
# mazcirut2.Printscore()
# mazcirut2.UpdatescoreTeamB(2)
# mazcirut1.Printscore()
# mazcirut1.UpdatescoreTeamA(3)
# mazcirut1.Printscore()


# class Inventory:
#     def __init__(self):
#         pass
#     def check(self):
#         print('exists')
#
# class payment:
#     def __init__(self):
#         pass
#     def pay(self):
#         print('paied')
#
# class Order:
#     def __init__(self):
#         pass
#     @staticmethod
#     def order_item():
#         checked = Inventory.check()
#         payed = payment.pay()
#         return checked + payed
#
#
#
# x = Order()
# print(x.order_item())
#


############################### composite #####################################
# class component:
#     def __init__(self):
#         pass
#     def print_data(self):
#         pass
#
#
# class composite(component):
#     def __init__(self):
#         self.lst = []
#     def add_child(self, child):
#         self.child = child
#         self.lst.append(self.child)
#     def remove_child(self, child):
#         self.child = child
#         self.lst.remove(self.child)
#     def print_data(self):
#         for child in self.lst:
#             child.print_data()
#
#
# class child(component):
#     def __init__(self,a ,b):
#         self.a = a
#         self.b = b
#     def print_data(self):
#         print('{' + self.a + ',' + self.b + '}')
#
#
#
#
# l1 = child('avi', '77')
# cm1 = composite()
# cm1.add_child(l1)
# cm1.print_data()


# class singleton:
#     class __inner:
#         def __init__(self):
#             self.n = 0
#             self.s = ''
#         def setN(self, arg):
#             self.n = arg
#         def setS(self, arg):
#             self.s = arg
#         def getNS(self):
#             print( self.n * self.s )
#     instance = None
#     def __init__(self):
#         if not singleton.instance:
#             singleton.instance = singleton.__inner()
#     def __getattr__(self, name):
#         return getattr(self.instance, name)
#
#
# x = singleton()
# x.setN(5)
# x.setS('oren ')
# x.getNS()


# from random import randrange
#
# class Galgal:
#     _shared_state = {}
#     def __init__(self):
#         self.__dict__ = self._shared_state
#
# class GalgalMazalPlayer(Galgal):
#     def __init__(self):
#         Galgal.__init__(self)
#         self.num = None
#     def roll(self):
#         self.num = randrange(1,12)
#     def shownum(self):
#         print(self.num)
#
# l = GalgalMazalPlayer()
# l.shownum()
# l.roll()
# l.shownum()


# class MyClass:
#     x = [1, 2, 3]
#     def __init__(self, y):
#         self.y = y
#
#     @classmethod
#     def tomer(cls, new_val):
#         return cls(new_val)
#
#     # @classmethod
#     # def modify_class_attr(cls, new_val):
#     #     cls.x.append(new_val)
#
# a = MyClass.tomer(7)
# print(a.y)
# a = MyClass(4)
# print(a.y)
# print(MyClass.x) # [1, 2, 3]
# MyClass.modify_class_attr(4)
# print(MyClass.x) # [1, 2, 3, 4]


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         func_output = self.func(a, b)
#         return func_output**2
#
# class Div:
#     def __init__(self, func):
#         self.func = func
#
#
#     def __call__(self, a, b):
#         func_output = self.func(a, b)
#         return (func_output/2)
#
#
# @Div
# @Power
# def multplyTogther(a, b):
#     return a*b
# print(multplyTogther(2, 5)) #50

#
class MyClass:
    y = [1, 2, 3]

    def __init__(self):
        self.x = 1

    def __private(self):
        print('eyal')

    @staticmethod
    def static_method(value):
        MyClass.y.append(value)
        print("This is a static method.")
        # print("The updated value of x is:", MyClass.self.x)  #ERROR
        print("The updated value of y is:", MyClass.y)

    @classmethod
    def class_method(cls, value):
        cls.y.append(value)
        cls.x = 4
        print("This is a class method.")
        print("The updated value of x is:", cls.x)
        print("The updated value of y is:", cls.y)



MyClass.static_method(4)
# This is a static method.
# The updated value of y is: [1, 2, 3, 4]
MyClass.class_method(5)
# This is a class method.
# The updated value of x is: 4
# The updated value of y is: [1, 2, 3, 4]
print(MyClass.x) #4
print(MyClass.y)


# def additiontext(func):
#     def inner(x,y):
#         print(f'the first input number is {x} and the second one is {y}')
#         return func(x,y)
#     return inner
#
#
# def special(func):
#     def inner(x,y):
#         if x*y < 0:
#             print('no good')
#     return inner
#
# @special
# @additiontext
# def addition(x,y):
#     x = int(x)
#     y = int(y)
#     print(x+y)
#
#
# addition(4,-15)

#
# class A:
#     def __new__(cls):
#         print('creating instance')
#         return A.__new__(cls)
#     def __init__(self):
#         print('init is called')
# A()


# class EduCourse:
#     university = 'Tel Aviv'
#     def __init__(self, MyUnvirsity, course_name, course_num):
#         university = MyUnvirsity
#         self.name = course_name
#         self.course = course_num
#
#     def details(self):
#         print(self.university)
#         print(self.name)
#         print(self.course)
#
# c = EduCourse('bash', 'infi', 101)
# print(c.__dict__)