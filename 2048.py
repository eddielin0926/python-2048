import pygame
import random
import math

pygame.init()

clock = pygame.time.Clock()

class Square:
    def __init__(self, num = 0, x = 0, y = 0):
        self.__num = num
        self.x = x
        self.y = y
        self.size = 125
        self.__font = pygame.font.SysFont(" ", 72, True)
        self.__bgColor = (204, 192, 180)
        self.__fontColor = (204, 192, 180)

    def setNum(self, num):
        if num == 0:
            self.__num = num
            self.__bgColor = (204, 192, 180)
            self.__fontColor = (204, 192, 180)
        elif num > 0 and num % 2 == 0:
            self.__num = num
            self.__setColor(num)

    def __setColor(self, num):
        color = [(238, 228, 218), (238, 224, 198), (242, 177, 121), (245, 149, 99), \
                 (245, 124, 95), (247, 94, 60), (235, 206, 114), (237, 203, 96), \
                 (235, 199, 79), (236, 196, 64), (237, 193, 45), (239, 102, 109), \
                 (237, 77, 89), (244, 64, 65), (114, 180, 214), (92, 160, 223), (24, 130, 204)]
        self.__bgColor = color[round(math.log2(num) - 1)]        
        if num == 2:
            self.__fontColor = (118, 109, 104)
        elif num == 4:
            self.__fontColor = (118, 109, 104)
        else:
            self.__fontColor = (251, 248, 241)

    def getNum(self):
        return self.__num

    def getColor(self):
        return self.__bgColor

    def getFontColor(self):
        return self.__fontColor
    
    def getFont(self):
        return self.__font

    def center(self, x, y):
        self.x = round(x - self.size / 2)
        self.y = round(y - self.size / 2)

# Create a window
win = pygame.display.set_mode((620, 620))
pygame.display.set_caption("2048")
boardsize = 600
width = round(5 * boardsize / 24)
interval = round(boardsize / 30)

# Create pieces
pieces = []
for row in range(4):
    pieces.append([])
    for column in range(4):
        pieces[row].append(Square(0, 30 + row * (width + interval), 30 + column * (width + interval)))

# Main loop
def main():
    run = True
    while run:
        clock.tick(30)

        # run = endGame()

        # Close the window
        for event in pygame .event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Keyboard Function
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if horizontal_move(0, 1):
                randpiece(1)
            print("<-")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if horizontal_move(1, -1):
                randpiece(1)
            print("->")
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if vertical_move(0, 1):
                randpiece(1)
            print("^")
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if vertical_move(1, -1):
                randpiece(1)
            print("v")
        if keys[pygame.K_SPACE]:
            print("Space")

        redrawGameWindow()
    
    # win.fill((248, 248, 238))
    # font = pygame.font.SysFont(" ", 72, True)
    # text = font.render("End", 1, (204, 192, 180))
    # textRect = text.get_rect()
    # textRect.center = (310, 310)
    # win.blit(text, textRect)

# Update the window
def redrawGameWindow():
    # Background Color
    win.fill((248, 248, 238))
    # Icon 
    # pygame.draw.rect(win, (237, 194, 1), (10, 42, 60, 60))
    # Score
    # pygame.draw.rect(win, (185, 173, 159), (94, 42, 55, 53))
    # Best score
    # pygame.draw.rect(win, (185, 173, 159), (158, 42, 55, 53))
    # Board
    pygame.draw.rect(win, (185, 173, 159), (10, 10, 600, 600))
    for i in range(0, 4):
        for j in range(0, 4):
            pygame.draw.rect(win, (204, 192, 180), (30 + i * (width + interval), 30 + j * (width + interval), width, width))

    for i in range(0, 4):
        for j in range(0, 4):
            pygame.draw.rect(win, pieces[i][j].getColor(), (pieces[i][j].x, pieces[i][j].y, pieces[i][j].size, pieces[i][j].size))
            text = pieces[i][j].getFont().render(str(pieces[i][j].getNum()), 1, pieces[i][j].getFontColor())
            textRect = text.get_rect()
            textRect.center = (30 + i * (width + interval) + width // 2, 30 + j * (width + interval) + width // 2)
            win.blit(text, textRect)
    pygame.display.update()

# Pop up animation
def animationPopUp(piecesList):
    c_x = []
    c_y = []
    for i in piecesList:
        c_x.append(pieces[i[0]][i[1]].x + pieces[i[0]][i[1]].size / 2)
        c_y.append(pieces[i[0]][i[1]].y + pieces[i[0]][i[1]].size / 2)
    for j in range(30, 126, 15):
        clock.tick(50)
        k = 0
        for i in piecesList:
            pieces[i[0]][i[1]].size = j
            pieces[i[0]][i[1]].center(c_x[k], c_y[k])
            k += 1
        redrawGameWindow()
    for i in piecesList:
        pieces[i[0]][i[1]].x = 30 + i[0] * (width + interval)
        pieces[i[0]][i[1]].y = 30 + i[1] * (width + interval)
        pieces[i[0]][i[1]].size = width

# Move animation
def animationMove():
    object_list = []
    target_list = []
    for i in object_list:
        return

# Create new piece(Problem: when it reach 16 it won't end)
def randpiece(amount):
    piecesList = []
    for i in range(amount):
        x, y = random.randint(0, 3), random.randint(0, 3)
        while pieces[x][y].getNum() != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        pieces[x][y].setNum(random.randint(1, 2) * 2)
        piecesList.append((x, y))
    animationPopUp(piecesList)

# Check the event
def horizontal_move(a, b, move = True):
    flag = False
    for k in range(0, 4):
        for i in range(0, 4):
            x = (i + a) * b
            if pieces[x][k].getNum() > 0:
                for j in range(i + 1, 4):
                    y = (j + a) * b
                    if pieces[y][k].getNum() > 0:
                        if pieces[y][k].getNum() == pieces[x][k].getNum():
                            if move:
                                pieces[x][k].setNum(pieces[x][k].getNum() * 2)
                                pieces[y][k].setNum(0)
                            flag = True
                        break
        for i in range(0, 4):
            x = (i + a) * b
            if pieces[x][k].getNum() == 0:
                for j in range(i + 1, 4):
                    y = (j + a) * b
                    if pieces[y][k].getNum() > 0:
                        if move:
                            pieces[x][k].setNum(pieces[y][k].getNum())
                            pieces[y][k].setNum(0)
                        flag = True
                        break
    return flag

def vertical_move(a, b, move = True):
    flag = False
    for k in range(0, 4):
        for i in range(0, 4):
            x = (i + a) * b
            if pieces[k][x].getNum() > 0:
                for j in range(i + 1, 4):
                    y = (j + a) * b
                    if pieces[k][y].getNum() > 0:
                        if pieces[k][y].getNum() == pieces[k][x].getNum():
                            if move:
                                pieces[k][x].setNum(pieces[k][x].getNum() * 2)
                                pieces[k][y].setNum(0)
                            flag = True
                        break
        for i in range(0, 4):
            x = (i + a) * b
            if pieces[k][x].getNum() == 0:
                for j in range(i + 1, 4):
                    y = (j + a) * b
                    if pieces[k][y].getNum() > 0:
                        if move:
                            pieces[k][x].setNum(pieces[k][y].getNum())
                            pieces[k][y].setNum(0)
                        flag = True
                        break
    return flag

def endGame():
    if horizontal_move(0, 1, False) or vertical_move(0, 1, False) or horizontal_move(1, -1, False) or vertical_move(1, -1, False):
        return True
    else:
        return False

# Start
randpiece(2)
main()
pygame.quit()