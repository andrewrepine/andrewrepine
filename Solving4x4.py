from random import randint
import math

class Board:

  def __init__(self, board):
    self.position = board
  def randomAiMove(self):
    while True:
      random = randint(0, 15)
      if self.position[random-random&4][random%4] == 0:
        self.position[random-random&4][random%4] = -1
        return
      
  def printBoard(self):
    print(self.position[0])
    print(self.position[1])
    print(self.position[2])
    print(self.position[3])
  def evaluate(self):
    for i in range(0,4):
      if self.position[i][0] == self.position[i][1] == self.position[i][2] & self.position[i][0] != 0:
        return self.position[i][0]
      
      elif self.position[i][1] == self.position[i][2] == self.position[i][3] & self.position[i][1] != 0:
        return self.position[i][1]
    for i in range(0,4):
      if self.position[0][i] == self.position[1][i] == self.position[2][i] & self.position[0][i] != 0:
        return self.position[0][i]
      elif self.position[1][i] == self.position[2][i] == self.position[3][i] & self.position[1][i] != 0:
        return self.position[1][i]
    for i in range(0,2):
      if self.position[i+0][i+0] == self.position[i+1][i+1] == self.position[i+2][i+2] & self.position[i+0][i+0] != 0:
        return self.position[i-0][i-0]
    for i in range(0,2):
      if self.position[1-i][0+i] == self.position[2-i][1+i] == self.position[3-i][2+i] & self.position[1-i][i] != 0:
        return self.position[1-i][0+i]
    for i in range(0,2):
      if self.position[2+i][0+i] == self.position[1+i][1+i] == self.position[0+i][2+i] & self.position[2+i][0+i] != 0:
        return self.position[2+i][0+i]
    for i in range(0,2):
      if self.position[3-i][i] == self.position[2-i][1+i] == self.position[1-i][2+i] & self.position[3-i][i] != 0:
        return self.position[1-i][0+i]
    return 0
  def move(self):
    loc = int(input("Input a square: "))
    sum1 = sum(map(sum, self.position))
    if sum1 == 0:
      sum1 = 1
    else:
      sum1 = -1
    if self.position[loc-loc&4][loc%4] == 0:
      self.position[loc-loc&4][loc%4] = sum1
      return
    print("\n-Invalid Coordinates-")
    self.printBoard()
    self.move()

  def make_best_move(self):
    return
    bestScore = -math.inf
    bestMove = None
    for move in self.position.get_possible_moves():
        ticTacBoard.make_move(move)
        score = minimax(False, aiPlayer, ticTacBoard)
        ticTacBoard.undo()
        if (score > bestScore):
            bestScore = score
            bestMove = move
    ticTacBoard.make_move(bestMove)

def minimax(isMaxTurn, maximizerMark, board):
    return
    state = board.get_state()
    if (state is State.DRAW):
        return 0
    elif (state is State.OVER):
        return 1 if board.get_winner() is maximizerMark else -1

    scores = []
    for move in board.get_possible_moves():
        board.make_move(move)
        scores.append(minimax(not isMaxTurn, maximizerMark, board))
        board.undo()

    return max(scores) if isMaxTurn else min(scores)
    
test = Board([[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]])
while test.evaluate() == 0:
  test.printBoard()
  test.move()
  test.randomAiMove()
print("Winner is: " + str(test.evaluate()))