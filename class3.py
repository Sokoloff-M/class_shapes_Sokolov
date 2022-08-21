from random import randrange as rr, choice, sample

CAT_COLORS = ['black', 'white', 'sand', 'grey', 'brown', 'orange']


class Cat:
    def __init__(self, name: str, sex: str, weight: float, colors: list[str]):
        self.name = name
        self.sex = sex
        self.weght = weight
        self.colors = colors

    def __str__(self):
        return f'<{self.name.title()}: {self.sex}, ' - '.join()self.colors>'

    @staticmethod
    def meow(self) -> None:
        print('Meow!')

    def ask_of_food(self):
        for _ in range(rr(3, 6)):
            self.meow()

    def reproduce(self) -> 'Cat':
        if self.sex == 'F':
            return Cat('<name>', choice('MF'), 0.05, sample(CAT_COLORS, k=rr(1, 4)))


# для обычных методов
# isinstance.method() -> Class.method(isinstance,*args)

# для статических методов
# isinstance.method() -> Class.method(*args)


cat1 = Cat('Killer', 'M', 3, ['orange', 'black', 'white'])
print(cat1)

cat1.meow()
print()

cat1.ask_of_food()
print()
