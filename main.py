from datetime import datetime as dt


class Player:
    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property
    def lvl(self):
        return self.__lvl, f'{dt.now() - self.__born}'

    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += Player.__typeTest(numeric)
        if self.__lvl >= 100:
            self.__lvl = 100

    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = Player.__typeTest(lvl)
        cls.__HEALTH = Player.__typeTest(health)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Must be int')

# class Purse:
#     def __init__(self, valuta, name='Unknown'):
#         if valuta not in ('USD', 'EUR'):
#             raise ValueError
#         self.__money = 0.00
#         self.valuta = valuta
#         self.name = name
#
#     def top_up_balance(self, howmany):
#         self.__money = self.__money + howmany
#         return howmany
#
#     def top_down_balance(self, howmany):
#         if self.__money - howmany < 0:
#             print('Недостаточно средств')
#             raise ValueError('Недостаточно средств')
#         self.__money = self.__money - howmany
#         return howmany
#
#     def info(self):
#         print(self.__money)
#
#     def __del__(self):
#         print('Кошелек удален')
#
#
# x = Purse('USD')
# y = Purse('USD', 'Bill')
# y.top_up_balance(10)
# x.top_up_balance(y.top_down_balance(7))
# x.info()
# y.info()
