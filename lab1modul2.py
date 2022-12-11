import doctest
class facebooksubs:
    def __init__(self, subscribers: int, subscribes: int):
        """
        Обьект - Фейсбук Подписки
        subscrubers = подписчики, subscribes = подписки
        >>>Пример: facebooksubs( 625, 110)
         """
        if not isinstance(subscribers, int):
            raise TypeError("Подписчики - только цифры")
        if subscribers < 0:
            raise ValueError("Подписчиков не может быть меньше 0")
        self.subscribers = subscribers
        if not isinstance(subscribes, int):
            raise TypeError("Подписки - только цифры")
        if subscribes < 0:
            raise ValueError("Подписок не может быть меньше 0")
        self.subscribes = subscribes
    def subscribersGrow(self, newsub: int) -> None:
        """
        Функция роста подписчиков
        ValyeError когда рост равен 0 и меньше
        >>>Пример: facebooksubs(625, 110)
        >>>instagramsubs.subscribersGrow(30)
        """
        if newsub < 1:
            raise ValueError("новых подписчиков не может быть меньше 1")
    def subscriberLose(self, sub: int) -> None:
        """Функция отписки подписчиков
              ValyeError когда отписки равены 0 и меньше"""
        if sub < 1:
            raise ValueError("отписок не может быть меньше 1")

class MoneyInBank:
    def __init__(self, rub: int, dollar: int, euro: int):
        """
        :param rub:
        :param dollar:
        :param euro:
        """
        self.rub = rub
        self.dollar = dollar
        self.euro = euro
        if not isinstance(rub, int):
            raise TypeError("Деньги - это число")
        if rub < 0:
            raise ValueError("Денег не может быть меньше 0")
        if not isinstance(dollar, int):
            raise TypeError("Деньги - это число")
        if dollar < 0:
            raise ValueError("Денег не может быть меньше 0")
        if not isinstance(euro, int):
            raise TypeError("Деньги - это число")
        if euro < 0:
            raise ValueError("Денег не может быть меньше 0")
    def euroGain(self, newEuro: int) -> None:
        """
        >>>MoneyInBank.euroGain(self, newEuro=10)
        :param newEuro:
        :return:
        """
        ...

    def dollarGain(self, newdollar: int) -> None:

        ...


class Phonecharge:
    def __init__(self, chargeleft: int, chargeright: int, lengthOfWire: [int, float]):
        self.chargeleft = chargeleft
        self.chargeright = chargeright
        self.lengthOfWire = lengthOfWire
        if not isinstance(chargeright, (int, float)):
            raise TypeError("Заряд только цифрой")
        if chargeleft < 0:
            raise ValueError("зарядки не может быть меньше 0")
        if not isinstance(chargeright, (int, float)):
            raise TypeError("Заряд только цифрой")
        if chargeright < 0:
            raise ValueError("зарядки не может быть меньше 0")
        if chargeright > 100:
            raise ValueError("Зарядки не может быть больше 100 процентов")
        if chargeleft > 100:
            raise ValueError("Зарядки не может быть больше 100 процентов")
        if lengthOfWire < 0:
            raise ValueError("Провод не может быть такой короткий")


    def charge(self, charging: int) -> None:

        """
        Зарядка Телефона
        :param charging: проценты заряда
        :return: количество финального заряда
        """

if __name__ == "__main__":
    doctest.testmod()
    pass