import pygame
import math
from queue import PriorityQueue

#Intializes Pygame environment
pygame.init()

#Creates window
WIDTH = 800
win = pygame.display.set_mode((WIDTH, WIDTH))

#Making Title
pygame.display.set_caption("A* Visualizer")

#Creating Color Variables
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)
purple = (128,0,128)
orange = (255,165,0)
grey = (128,128,128)
turquoise = (64,224,208)

#Visualizer
class Node:

    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.totalRows = totalRows
        self.color = white
        self.neighbors = []
        self.width = width

    def getPos(self):
        return self.row, self.col

    def isClosed(self):
        return self.color == red

    def isOpen(self):
        return self.color == green

    def isBarrier(self):
        return self.color == black

    def isStart(self):
        return self.color == orange

    def isEnd(self):
        return self.color == turquoise

    def reset(self):
        self.color = white

    def makeClosed(self):
        self.color = red

    def makeOpen(self):
        self.color = green

    def makeBarrier(self):
        self.color = black

    def makeStart(self):
        self.color = orange

    def makeEnd(self):
        self.color = turquoise

    def makePath(self):
        self.color = purple

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.width))

    def updateNeighbors(self, grid):
        self.neighbors = []
        if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isBarrier(): #DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].isBarrier(): #UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].isBarrier(): #LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

        if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isBarrier(): #RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])


    def __lt__(self, other):
        return False

#Drawing
def makeGrid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def drawGrid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, grey, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, grey, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(white)

    for row in grid:
        for node in row:
            node.draw(win)

    drawGrid(win, rows, width)
    pygame.display.update()


def getClickedPosition(pos, rows, width):
    gap = width // rows
    y,x = pos
    row = y // gap
    col = x // gap
    return row, col

#A* Implementation
def h(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2)+abs(y1-y2)

def reconstructPath(cameFrom, current, draw):
    while current in cameFrom:
        current = cameFrom[current]
        current.makePath()
        draw()

def astar(draw, grid, start, end):
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))
    cameFrom = {}
    gScore = {node: float("inf") for row in grid for node in row}
    gScore[start] = 0
    fScore = {node: float("inf") for row in grid for node in row}
    fScore[start] = h(start.getPos(), end.getPos())

    openSetHash = {start}

    while not openSet.empty():
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

        current = openSet.get()[2]
        openSetHash.remove(current)

        if current == end:
            reconstructPath(cameFrom, end, draw)
            end.makeEnd()
            start.makeStart()
            return True

        for neighbor in current.neighbors:
            tempGScore = gScore[current] + 1

            if tempGScore < gScore[neighbor]:
                gScore[neighbor] = tempGScore
                cameFrom[neighbor] = current
                fScore[neighbor] = tempGScore + h(neighbor.getPos(), end.getPos())
                if neighbor not in openSetHash:
                    count += 1
                    openSet.put((fScore[neighbor], count, neighbor))
                    openSetHash.add(neighbor)
                    neighbor.makeOpen()
        draw()

        if current != start:
            current.makeClosed()

    return False

#Game loop
def main(win, width, Rows):
    grid = makeGrid(Rows, width)

    start = None
    end = None

    run = True
    while run == True:
        draw(win, grid, Rows, width)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = getClickedPosition(pos, Rows, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.makeStart()

                elif not end and node != start:
                    end = node
                    end.makeEnd()

                elif node != end and node != start:
                    node.makeBarrier()


            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = getClickedPosition(pos, Rows, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None

                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.updateNeighbors(grid)
                    astar(lambda: draw(win, grid, Rows, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = makeGrid(Rows, width)


    pygame.quit()

main(win, WIDTH, 100)