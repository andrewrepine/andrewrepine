
class Rook:

    def __init__(self, location, color):
        self.location = location
        self.color = color
        self.letter = 'R'
        self.symbol = '{0}{1}'.format(self.color[0], self.letter)
        self.moves = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0,5), (0,6), (0,7), (-1,0), (-2, 0), (-3,0), (-4,0), (-5,0), (-6,0), (-7,0), (0, -1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7)]


class Pawn:

    def __init__(self, location, color, moved=False):
        self.location = location
        self.color = color
        self.moved = moved
        self.letter = 'P'
        self.symbol = '{0}{1}'.format(self.color[0], self.letter)
        self.moves = [(0, 1), (0, 2)]


class Bishop:

    def __init__(self, location, color):
        self.location = location
        self.color = color
        self.letter = 'B'
        self.symbol = '{0}{1}'.format(self.color[0], self.letter)


class King:

    def __init__(self, location, color, moved=False):
        self.location = location
        self.color = color
        self.moved = moved
        self.letter = 'K'
        self.symbol = '{0}{1}'.format(self.color[0], self.letter)


class Queen:

    def __init__(self, location, color):
        self.location = location
        self.color = color
        self.letter = 'Q'
        self.symbol = '{0}{1}'.format(self.color[0], self.letter)


class Knight:

    def __init__(self, location, color):
        self.location = location
        self.color = color
        self.letter = 'N'
        self.symbol = '{0}{1}'.format(self.color[0], self.letter)


class ChessBoard:

    def __init__(self):
        self.row1 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.row2 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.row3 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.row4 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.row5 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.row6 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.row7 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.row8 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.columns = [self.row1, self.row2, self.row3, self.row4, self.row5, self.row6, self.row7, self.row8]
        self.column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.piece_list = []

    def on_board(self, square):
        square = square.upper()
        column = self.column.index(square[0])
        row = int(square[1]) - 1
        piece = None
        try:
            piece = self.columns[row][column]
        except:
            piece = None

        if piece != None:
            return True
        else:
            return False

    def is_empty(self, square):
        if not self.on_board(square):
            return True
        square = square.upper()
        column = self.column.index(square[0])
        row = int(square[1]) - 1
        if self.columns[row][column] == '  ':
            return True
        else:
            return False

    def possible_moves(self, piece):
      location = piece.location
      column = self.column.index(location[0])
      row = int(location[1]) - 1
      coords = (row, column)
      if type(piece) == Pawn:
        if not piece.moved:
          square1 = f'{self.column[coords[1]]}{coords[0] + 2}'
          square2 = f'{self.column[coords[1]]}{coords[0] + 3}'
          if self.is_empty(square1):
            self.columns[coords[0]+ 1][coords[1]] = '<>'
            Return = True
          if self.is_empty(square2):
            self.columns[coords[0]+ 2][coords[1]] = '<>'
            Return = True
          else:
            Return = False
        elif piece.moved:
          square1 = f'{self.column[coords[1]]}{coords[0] + 2}'
          if self.is_empty(square1):
            self.columns[coords[0]+ 1][coords[1]] = '<>'
            Return = True
          else:
            Return = False
            
      return Return


    def print_board(self):
        print(' |-----------------------|')
        print('8|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|'.format(self.row8[0], self.row8[1], self.row8[2], self.row8[3],
                                                          self.row8[4], self.row8[5], self.row8[6], self.row8[7]))
        print(' |-----------------------|')
        print('7|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|'.format(self.row7[0], self.row7[1], self.row7[2], self.row7[3],
                                                          self.row7[4], self.row7[5], self.row7[6], self.row7[7]))
        print(' |-----------------------|')
        print('6|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|'.format(self.row6[0], self.row6[1], self.row6[2], self.row6[3],
                                                          self.row6[4], self.row6[5], self.row6[6], self.row6[7]))
        print(' |-----------------------|')
        print('5|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|'.format(self.row5[0], self.row5[1], self.row5[2], self.row5[3],
                                                          self.row5[4], self.row5[5], self.row5[6], self.row5[7]))
        print(' |-----------------------|')
        print('4|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|'.format(self.row4[0], self.row4[1], self.row4[2], self.row4[3],
                                                          self.row4[4], self.row4[5], self.row4[6], self.row4[7]))
        print(' |-----------------------|')
        print('3|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|'.format(self.row3[0], self.row3[1], self.row3[2], self.row3[3],
                                                          self.row3[4], self.row3[5], self.row3[6], self.row3[7]))
        print(' |-----------------------|')
        print('2|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|'.format(self.row2[0], self.row2[1], self.row2[2], self.row2[3],
                                                          self.row2[4], self.row2[5], self.row2[6], self.row2[7]))
        print(' |-----------------------|')
        print('1|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|'.format(self.row1[0], self.row1[1], self.row1[2], self.row1[3],
                                                          self.row1[4], self.row1[5], self.row1[6], self.row1[7]))
        print(' |-----------------------|')
        print(' |A |B |C |D |E |F |G |H |')

    def create_board(self):
        color = 'White'
        num = 1
        self.wrook1 = Rook('A'+str(num), color)
        self.wrook2 = Rook('H'+str(num), color)
        self.wknight1 = Knight('B'+str(num), color)
        self.wknight2 = Knight('G'+str(num), color)
        self.wbishop1 = Bishop('C'+str(num), color)
        self.wbishop2 = Bishop('F'+str(num), color)
        self.wqueen = Queen('D'+str(num), color)
        self.wking = King('E'+str(num), color)
        num = 2
        self.wpawn1 = Pawn('A'+str(num), color)
        self.wpawn2 = Pawn('B' + str(num), color)
        self.wpawn3 = Pawn('C' + str(num), color)
        self.wpawn4 = Pawn('D' + str(num), color)
        self.wpawn5 = Pawn('E' + str(num), color)
        self.wpawn6 = Pawn('F' + str(num), color)
        self.wpawn7 = Pawn('G' + str(num), color)
        self.wpawn8 = Pawn('H' + str(num), color)

        color = 'Black'
        num = 8
        self.brook1 = Rook('A' + str(num), color)
        self.brook2 = Rook('H' + str(num), color)
        self.bknight1 = Knight('B' + str(num), color)
        self.bknight2 = Knight('G' + str(num), color)
        self.bbishop1 = Bishop('C' + str(num), color)
        self.bbishop2 = Bishop('F' + str(num), color)
        self.bqueen = Queen('D' + str(num), color)
        self.bking = King('E' + str(num), color)
        num = 7
        self.bpawn1 = Pawn('A' + str(num), color)
        self.bpawn2 = Pawn('B' + str(num), color)
        self.bpawn3 = Pawn('C' + str(num), color)
        self.bpawn4 = Pawn('D' + str(num), color)
        self.bpawn5 = Pawn('E' + str(num), color)
        self.bpawn6 = Pawn('F' + str(num), color)
        self.bpawn7 = Pawn('G' + str(num), color)
        self.bpawn8 = Pawn('H' + str(num), color)

        self.piece_list = [self.wrook1, self.wrook2, self.wknight1, self.wknight2, self.wbishop1, self.wbishop2, self.wqueen, self.wking, self.brook1, self.brook2, self.bknight1,
                           self.bknight2, self.bbishop1, self.bbishop2, self.bqueen, self.bking, self.wpawn1, self.wpawn2, self.wpawn3, self.wpawn4, self.wpawn5, self.wpawn6,
                           self.wpawn7, self.wpawn8, self.bpawn1, self.bpawn2, self.bpawn3, self.bpawn4, self.bpawn5, self.bpawn6, self.bpawn7, self.bpawn8]
        for piece in self.piece_list:
            column = self.column.index(piece.location[0])
            row = int(piece.location[1]) - 1
            self.columns[row][column] = piece.symbol
        #self.print_board()

    def update_position(self, piece, new_square):
        new_square = new_square.upper()
        old_location = piece.location
        piece.location = new_square
        row = self.column.index(new_square[0])
        column = int(new_square[1]) - 1
        print(column, row)
        print(piece.location)
        self.columns[column][row] = piece.symbol
        print(self.columns[column][row], (column, row))
        row1 = self.column.index(old_location[0])
        column1 = int(old_location[1]) - 1
        print(column1, row1)
        self.columns[column1][row1] = '  '
        print(piece.location)
        self.print_board()

    def move_piece(self, square):
        square = square.upper()
        if self.on_board(square) == False:
            print('\n\nPlease enter new square')
        else:
            row = int(square[1]) - 1
            column = self.column.index(square[0])
            current_piece = None
            for i in self.piece_list:
                if i.location == square:
                    current_piece = i
                else:
                    continue
            if type(current_piece) == Rook:
                for i in range(0, 9):
                    continue
            print(self.is_empty(square))
            self.print_board()

    def play_game(self):
        won = False
        color = True
        while won == False:
            if color == True:
                color1 = 'White'
            else:
                color1 = 'Black'
            square = input(f'{color1} which piece would you like to move (ex. A5): ')
            while self.is_empty(square):
                square = input(f'{color1} please do not input an empty or off the board square (ex. A5): ')
            square = square.upper()
            piece = None
            for i in self.piece_list:
                if i.location == square:
                    piece = i
                else:
                    continue
            while piece.color != color1:
                square = input(f'{color1} please select your own piece (ex. A5): ')
                while self.is_empty(square):
                    square = input(f'{color1} please do not input an empty or off the board square (ex. A5): ')
                square = square.upper()
                piece = None
                for i in self.piece_list:
                    if i.location == square:
                        piece = i
            if color == True:
                color = False
            else:
                color = True
            self.move_piece(piece.location)

    def tester(self):
      print(self.possible_moves(self.wpawn1))
      self.print_board()

