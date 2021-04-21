from threading import Thread
from random import choice
from time import sleep

_foods = [
    '羊肉卷',
    '牛肉卷',
    '豆腐皮',
    '青菜',
    '捞面',
    '鸭血',
    '虾滑',
    '鱼丸',
    '牛肉丸',
    '豆腐',
    '土豆片'
]


class Member:
    def __init__(self, family_name: str, status='大佬'):
        self.family_name = family_name
        self.status = status

    def greet(self):
        print(f'{self.family_name}{self.status}: "乌拉！"')

    def eat(self, limit=10):
        def eat_in_thread(num: int):
            while num := num - 1:
                sleep(1)
                food = choice(_foods)
                print(f'{self.family_name}{self.status} just ate a {food}.\n', end='')
        Thread(target=eat_in_thread, args=(limit, )).start()
