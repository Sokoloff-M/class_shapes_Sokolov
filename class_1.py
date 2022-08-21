class Table:
    legs = 4
    width = 100
    depth = 80
    height = 70

    def print():
        print(f'<{Table.legs}-legstable: '
              f'{Table.width}x{Table.depth}x{Table.height}>')


# создание экземпляров класса
table1 = Table()
table2 = Table()

print(f'{table1 = }\n{type(table1) = }\n')
print(f'{table2 = }\n{type(table2) = }\n')

print(f'{table1.legs = }')
print(f'{table1.height = }\n')
try:
    print('table1.ptint()')
    table1.print()
except TypeError as e:
    print('TypeError:', e)
    print('Вызов метода table.print() становится вызовом фкнкции Table.print(table1)')
