import sys

desk = [[' '] + list(range(3)),
          [0] + [None] * 3,
          [1] + [None] * 3,
          [2] + [None] * 3]

def print_desk(obj=''):

    none_count = 0

    for i in desk:
        for j in i:
            if j is None:
                j = '-'
                none_count += 1
            print(j, end=' ')
        print()

    if ((obj == desk[1][1] == desk[1][2] == desk[1][3]) # строки
            or (obj == desk[2][1] == desk[2][2] == desk[2][3])
            or (obj == desk[3][1] == desk[3][2] == desk[3][3])
            or (obj == desk[1][1] == desk[2][1] == desk[3][1]) # столбцы
            or (obj == desk[1][2] == desk[2][2] == desk[3][2])
            or (obj == desk[1][3] == desk[2][3] == desk[3][3])
            or (obj == desk[1][1] == desk[2][2] == desk[3][3]) # диагонали
            or (obj == desk[3][1] == desk[2][2] == desk[1][3])):
        print(f'Победил {obj}!')
        sys.exit(0)

    if none_count == 0:
        print('Ничья :)')
        sys.exit(0)

def process(obj):
    while True:
        try:
            x, y = [int(x) + 1 for x in input(f'Введите координаты для {obj} через пробел: ').split(' ')]
        except ValueError:
            print('Введите 2 числа через пробел')
            continue
        if (1 <= x <= 3) and (1 <= y <= 3):
            if desk[x][y] is None:
                desk[x][y] = obj
                print_desk(obj)
                break
            else:
                print('Координаты заняты')
        else:
            print('Координаты должы быть в диапазоне от 0 до 2')

if __name__ == '__main__':
    print_desk()
    while True:
        try:
            process('X')
            process('O')
        except KeyboardInterrupt:
            break
