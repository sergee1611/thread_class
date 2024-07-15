from threading import Thread
from time import sleep
from pprint import pprint


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        pprint(f'{self.name}, на нас напали!')
        days_num = 0
        enemy_num = 100
        while enemy_num > 0:
            enemy_num -= self.power
            days_num += 1
            sleep(1)
            pprint(f'{self.name} сражается {days_num}..., осталось {enemy_num} воинов.')
        pprint(f'{self.name} одержал победу спустя {days_num} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')
