class CrossZero:
    fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    go = 1
    x = []
    o = []
    slip_winner = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

    def draw(self):
        a = self.fields
        print(f' {a[0]} |', f' {a[1]}  |', f' {a[2]} ', '\n-------------', f'\n {a[3]} |', f' {a[4]}  |', f' {a[5]} ',
              '\n-------------', f'\n {a[6]} |', f' {a[7]}  |', f' {a[8]} ')

    def game(self):
        try:
                if self.go % 2 != 0:
                    a = int(input(f'Ход крестика {self.go}, введите номер клетки >>> '))
                    if isinstance(self.fields[a-1], int):
                        self.go += 1
                        self.fields[a-1] = 'X'
                        self.x.append(a)
                else:
                    a = int(input(f'Ход нолика {self.go}, введите номер клетки >>> '))
                    if isinstance(self.fields[a-1], int):
                        self.go += 1
                        self.fields[a-1] = 'O'
                        self.o.append(a)
                    else:
                        print('Полe занято!')
        except ValueError:
            print('Введите число!')

        except IndexError:
            print('Недопустимое число!')

    def winner(self):
        if 4 < self.go <= 9 and self.go % 2 == 0:
            for item in self.slip_winner:
                if item[0] in self.x and item[1] in self.x and item[2] in self.x:
                    print('>>>  Win - X')
                    exit()
        elif 5 < self.go <= 8 and self.go % 2 != 0:
            for item in self.slip_winner:
                if item[0] in self.o and item[1] in self.o and item[2] in self.o:
                    print('>>>  Win - O')
                    exit()
        if self.go == 10:
            print('>>> Draw')
            exit()

    def __init__(self):
        while True:
            self.draw()
            self.game()
            self.winner()




if __name__ == '__main__':
    CrossZero()


