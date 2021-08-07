import pygame
import sys
import time
import random


#             GAME CO-ORDINATE SYSTEM
#
#   1,1   2,1   3,1   4,1   5,1   6,1   7,1   8,1
#   1,2   2,2   3,2   4,2   5,2   6,2   7,2   8,2
#   1,3   2,3   3,3   4,3   5,3   6,3   7,3   8,3
#   1,4   2,4   3,4   4,4   5,4   6,4   7,4   8,4
#   1,5   2,5   3,5   4,5   5,5   6,5   7,5   8,5
#   1,6   2,6   3,6   4,6   5,6   6,6   7,6   8,6
#   1,7   2,7   3,7   4,7   5,7   6,7   7,7   8,7
#   1,8   2,8   3,8   4,8   5,8   6,8   7,8   8,8
#




# initialisation and setting up the window.

pygame.init()
width, height = 700, 700
Screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aditya Rai's Chess")
# pygame.display.set_icon()

# ==================================================================================================Data Members

# importing required images.

board = pygame.image.load("res/images/board/background.png")
blue_box = pygame.image.load("res/images/squares/bluebox.png")
green_box = pygame.image.load("res/images/squares/greenbox.png")
purple_box = pygame.image.load("res/images/squares/purplebox.png")
red_box = pygame.image.load("res/images/squares/redbox.png")

imgpawnblack = pygame.image.load("res/images/pieces/pawnB.png")
imgrockblack = pygame.image.load("res/images/pieces/rockB.png")
imgknightblack = pygame.image.load("res/images/pieces/knightB.png")
imgbishopblack = pygame.image.load("res/images/pieces/bishopB.png")
imgkingblack = pygame.image.load("res/images/pieces/kingB.png")
imgqueenblack = pygame.image.load("res/images/pieces/queenB.png")

imgpawnwhite = pygame.image.load("res/images/pieces/pawnW.png")
imgrockwhite = pygame.image.load("res/images/pieces/rockW.png")
imgknightwhite = pygame.image.load("res/images/pieces/knightW.png")
imgbishopwhite = pygame.image.load("res/images/pieces/bishopW.png")
imgkingwhite = pygame.image.load("res/images/pieces/kingW.png")
imgqueenwhite = pygame.image.load("res/images/pieces/queenW.png")

blackwins = pygame.image.load("res/images/declaration/blackwins.png")
whitewins = pygame.image.load("res/images/declaration/whitewins.png")


# declaring class piece, the datatype of all pieces on the board.

class piece():

    def __init__(self, posx_, posy_, type_, img_, points_):
        self.posx = posx_
        self.posy = posy_
        self.piecetype = type_
        self.imgsrc = img_
        self.points = points_


# Creating the list of pieces of black and white side along with their positions and the points they carry
# points are meant to be used by the bot.

white = [piece(1, 7, 'pawn', imgpawnwhite, 1), piece(1, 8, 'rock', imgrockwhite, 4),
         piece(2, 7, 'pawn', imgpawnwhite, 1), piece(2, 8, 'knight', imgknightwhite, 4),
         piece(3, 7, 'pawn', imgpawnwhite, 1), piece(3, 8, 'bishop', imgbishopwhite, 4),
         piece(4, 7, 'pawn', imgpawnwhite, 1), piece(4, 8, 'queen', imgqueenwhite, 7),
         piece(5, 7, 'pawn', imgpawnwhite, 1), piece(5, 8, 'king', imgkingwhite, 500),
         piece(6, 7, 'pawn', imgpawnwhite, 1), piece(6, 8, 'bishop', imgbishopwhite, 4),
         piece(7, 7, 'pawn', imgpawnwhite, 1), piece(7, 8, 'knight', imgknightwhite, 4),
         piece(8, 7, 'pawn', imgpawnwhite, 1), piece(8, 8, 'rock', imgrockwhite, 4)]
black = [piece(1, 2, 'pawn', imgpawnblack, 1), piece(1, 1, 'rock', imgrockblack, 4),
         piece(2, 2, 'pawn', imgpawnblack, 1), piece(2, 1, 'knight', imgknightblack, 4),
         piece(3, 2, 'pawn', imgpawnblack, 1), piece(3, 1, 'bishop', imgbishopblack, 4),
         piece(4, 2, 'pawn', imgpawnblack, 1), piece(4, 1, 'queen', imgqueenblack, 7),
         piece(5, 2, 'pawn', imgpawnblack, 1), piece(5, 1, 'king', imgkingblack, 500),
         piece(6, 2, 'pawn', imgpawnblack, 1), piece(6, 1, 'bishop', imgbishopblack, 4),
         piece(7, 2, 'pawn', imgpawnblack, 1), piece(7, 1, 'knight', imgknightblack, 4),
         piece(8, 2, 'pawn', imgpawnblack, 1), piece(8, 1, 'rock', imgrockblack, 4)]


# declaring tuples storing the position of black and white kind respectively.

blackKingPos = ( 5, 1,)
whiteKingPos = ( 5, 8,)


# declaring important data members
gameover_ = False
winner = 'none'

operator = 'player'
Turn = 'white'

BlackCheck = False
WhiteCheck = False

selectedpiece = -1

possible_path = list()
occupied = list()
occupied_white = list()
occupied_black = list()
dangerforblack = list()
dangerforwhite = list()

# ==================================================================================================Data Members ends

frame_rate = pygame.time.Clock()


# ==================================================================================================Member Functions

def getposx(i, j):
    # returns the x coordinate after converting it from pixels to game unit.
    val = [30, 110, 190, 270, 350, 430, 510, 590]
    if j < 1 or j > 8:
        return -100
    return val[j - 1]


def getposy(i, j):
    # returns the y coordinate after converting it from pixels to game unit.
    val = [30, 110, 190, 270, 350, 430, 510, 590]
    if i < 1 or i > 8:
        return -100
    return val[i - 1]


def drawpieces():
    # draw the pieces on their specified positions on the chess board.
    for piece_ in black:
        Screen.blit(piece_.imgsrc, (getposy(piece_.posx, piece_.posy), getposx(piece_.posx, piece_.posy)))
    for piece_ in white:
        Screen.blit(piece_.imgsrc, (getposy(piece_.posx, piece_.posy), getposx(piece_.posx, piece_.posy)))


def draw_possible_path( T, OW, OB):
    # highlights the coordinates stored in the list storing the possible paths.
    if len(possible_path) == 0:
        return
    for path_ in possible_path:
        if path_ == blackKingPos or path_ == whiteKingPos:
            continue
        if T == 'white':
            if path_ in OB:
                Screen.blit(red_box, (getposy(path_[0], path_[1]), getposx(path_[0], path_[1])))
            else:
                Screen.blit(green_box, (getposy(path_[0], path_[1]), getposx(path_[0], path_[1])))
        else:
            if path_ in OW:
                Screen.blit(red_box, (getposy(path_[0], path_[1]), getposx(path_[0], path_[1])))
            else:
                Screen.blit(green_box, (getposy(path_[0], path_[1]), getposx(path_[0], path_[1])))



def getmousepos(x):
    # returns the position of mouse in game coordinate system.
    val = [30, 110, 190, 270, 350, 430, 510, 590, 670]
    _X, _y = -100, -100
    for i in range(8):
        if val[i] <= x[0] <= val[i + 1]:
            _x = i + 1
        if val[i] <= x[1] <= val[i + 1]:
            _y = i + 1
    if x[0] < 30 or x[0] > 670:
        _x = -1
    if x[1] < 30 or x[1] > 670:
        _y = -1
    return _x, _y


def isvalid(__X, __Y):
    # returns true if the co-ordinates lies within the limit of the game's coordinate system.
    if 1 <= __X <= 8 and 1 <= __Y <= 8:
        return True
    return False


def knightpath(__X, __Y, occ):
    # returns the positions a knight can move to.
    L = []
    if isvalid(__X + 2, __Y + 1) and (__X + 2, __Y + 1) not in occ:
        L.append((__X + 2, __Y + 1))
    if isvalid(__X + 2, __Y - 1) and (__X + 2, __Y - 1) not in occ:
        L.append((__X + 2, __Y - 1))
    if isvalid(__X + 1, __Y + 2) and (__X + 1, __Y + 2) not in occ:
        L.append((__X + 1, __Y + 2))
    if isvalid(__X - 1, __Y + 2) and (__X - 1, __Y + 2) not in occ:
        L.append((__X - 1, __Y + 2))
    if isvalid(__X - 2, __Y + 1) and (__X - 2, __Y + 1) not in occ:
        L.append((__X - 2, __Y + 1))
    if isvalid(__X - 2, __Y - 1) and (__X - 2, __Y - 1) not in occ:
        L.append((__X - 2, __Y - 1))
    if isvalid(__X + 1, __Y - 2) and (__X + 1, __Y - 2) not in occ:
        L.append((__X + 1, __Y - 2))
    if isvalid(__X - 1, __Y - 2) and (__X - 1, __Y - 2) not in occ:
        L.append((__X - 1, __Y - 2))
    return L
def knightattackpath(__X, __Y, occ):
    # to be used by the bot.
    L = []
    L.append((__X + 2, __Y + 1))
    L.append((__X + 2, __Y - 1))
    L.append((__X + 1, __Y + 2))
    L.append((__X - 1, __Y + 2))
    L.append((__X - 2, __Y + 1))
    L.append((__X - 2, __Y - 1))
    L.append((__X + 1, __Y - 2))
    L.append((__X - 1, __Y - 2))
    return L


def rockpath(__X, __Y, occ, occE):
    # returns the positions a rock can move to.
    L = []

    i, j = __X + 1, __Y
    while (isvalid(i, j)):
        if (i, j) in occ:
            break
        L.append((i, j,))
        if (i, j) in occE:
            break

        i += 1
    i, j = __X - 1, __Y
    while (isvalid(i, j)):
        if (i, j) in occ:
            break
        L.append((i, j,))

        if (i, j) in occE:
            break

        i -= 1
    i, j = __X, __Y + 1
    while (isvalid(i, j)):
        if (i, j) in occ:
            break
        L.append((i, j,))
        if (i, j) in occE:
            break

        j += 1
    i, j = __X, __Y - 1
    while (isvalid(i, j)):
        if (i, j) in occ:
            break
        L.append((i, j,))
        if (i, j) in occE:
            break

        j -= 1
    return L

def bishoppath(__X, __Y, occ, occE):
    # returns the positions a bishop can move to.
    L = []
    i, j = __X + 1, __Y + 1
    while (isvalid(i, j)):
        if (i, j) in occ:
            break
        L.append((i, j,))
        if (i, j) in occE:
            break

        i += 1
        j += 1
    i, j = __X - 1, __Y - 1
    while (isvalid(i, j)):
        if (i, j) in occ:
            break
        L.append((i, j,))
        if (i, j) in occE:
            break

        i -= 1
        j -= 1
    i, j = __X + 1, __Y - 1
    while (isvalid(i, j)):
        if (i, j) in occ:
            break
        L.append((i, j,))
        if (i, j) in occE:
            break

        i += 1
        j -= 1
    i, j = __X - 1, __Y + 1
    while (isvalid(i, j)):
        if (i, j) in occ:
            break
        L.append((i, j,))
        if (i, j) in occE:
            break

        i -= 1
        j += 1

    return L


def pawnpath(__X, __Y, col, occ, occE):
    # returns the positions a pawn can move to.
    L = []
    if col == 'white':
        if (__X, __Y - 1) not in occ and (__X, __Y - 1) not in occE:
            L.append((__X, __Y - 1,))

        if (__X + 1, __Y - 1) in occE:
            L.append((__X + 1, __Y - 1,))

        if (__X - 1, __Y - 1) in occE:
            L.append((__X - 1, __Y - 1,))

        if (__X, __Y - 1) in L:
            if (__X, __Y - 2) not in occ and (__X, __Y - 2) not in occE and __Y == 7:
                L.append((__X, __Y - 2,))
        return L

    else:
        if (__X, __Y + 1) not in occ and (__X, __Y + 1) not in occE:
            L.append((__X, __Y + 1,))

        if (__X + 1, __Y + 1) in occE:
            L.append((__X + 1, __Y + 1,))

        if (__X - 1, __Y + 1) in occE:
            L.append((__X - 1, __Y + 1,))

        if (__X, __Y + 1) in L:
            if (__X, __Y + 2) not in occ and (__X, __Y + 2) not in occE and __Y == 2:
                L.append((__X, __Y + 2,))

    return L
def pawnattackpath( __X, __Y, col, occ, occE):
    # to be used by the bot.
    L = []
    if col == 'white':

        L.append((__X + 1, __Y - 1,))
        L.append((__X - 1, __Y - 1,))
        return L

    else:

        L.append((__X + 1, __Y + 1,))
        L.append((__X - 1, __Y + 1,))

    return L


def queenpath(__X, __Y, occ, occE):
    # returns the positions a Queen can move to.
    L = []

    L.extend( rockpath( __X, __Y, occ, occE))
    L.extend( bishoppath( __X, __Y, occ, occE))

    return L

def kingpath(__X, __Y, occ, danger):
    # returns the postions on which a king can move.
    L = []
    x, y = __X, __Y - 1
    if isvalid(x, y) and (x, y) not in occ: # and (x, y) not in danger:
        L.append((x, y,))
    x, y = __X, __Y + 1
    if isvalid(x, y) and (x, y) not in occ: # and (x, y) not in danger:
        L.append((x, y,))
    x, y = __X + 1, __Y
    if isvalid(x, y) and (x, y) not in occ: # and (x, y) not in danger:
        L.append((x, y,))
    x, y = __X - 1, __Y
    if isvalid(x, y) and (x, y) not in occ: # and (x, y) not in danger:
        L.append((x, y,))

    x, y = __X - 1, __Y - 1
    if isvalid(x, y) and (x, y) not in occ: # and (x, y) not in danger:
        L.append((x, y,))
    x, y = __X + 1, __Y - 1
    if isvalid(x, y) and (x, y) not in occ: # and (x, y) not in danger:
        L.append((x, y,))
    x, y = __X + 1, __Y + 1
    if isvalid(x, y) and (x, y) not in occ: # and (x, y) not in danger:
        L.append((x, y,))
    x, y = __X - 1, __Y + 1
    if isvalid(x, y) and (x, y) not in occ: # and (x, y) not in danger:
        L.append((x, y,))

    return L
def kingattackpath(__X, __Y, occ, danger):
    # to be used by the bot.
    L = []
    x, y = __X, __Y - 1
    if isvalid(x, y):
        L.append((x, y,))
    x, y = __X, __Y + 1
    if isvalid(x, y):
        L.append((x, y,))
    x, y = __X + 1, __Y
    if isvalid(x, y):
        L.append((x, y,))
    x, y = __X - 1, __Y
    if isvalid(x, y):
        L.append((x, y,))

    x, y = __X - 1, __Y - 1
    if isvalid(x, y):
        L.append((x, y,))
    x, y = __X + 1, __Y - 1
    if isvalid(x, y):
        L.append((x, y,))
    x, y = __X + 1, __Y + 1
    if isvalid(x, y):
        L.append((x, y,))
    x, y = __X + 1, __Y - 1
    if isvalid(x, y):
        L.append((x, y,))

    return L

def blackcheck( bkpos, wh):
    # returns true if black in checked.
    dfb = list()
    for itr in range(len(wh)):
        dfb.extend(getattackpath(itr, 'white'))
    if bkpos in dfb:
        return True
    return False
def whitecheck( wkpos, bk):
    # returns true if white is checked.
    dfw = list()
    for itr in range(len(bk)):
        dfw.extend(getattackpath(itr, 'black'))
    if wkpos in dfw:
        return True
    return False

def draw_kings_status():
    # highlights the king's position with purple color if he is checked.
    if blackcheck( blackKingPos, white):
        Screen.blit( purple_box, (getposy( blackKingPos[0], blackKingPos[1]), getposx( blackKingPos[0], blackKingPos[1])))
    if whitecheck( whiteKingPos, black):
        Screen.blit( purple_box, (getposy( whiteKingPos[0], whiteKingPos[1]), getposx( whiteKingPos[0], whiteKingPos[1])))
    return


def getpath(selectedp, st):
    # returns the possible path for the selected pieces.
    if selectedp == -1:
        return [(-100, -100,)]

    if st == 'white':
        pieceforpath = white[selectedp]

        if pieceforpath.piecetype == 'knight':
            return knightpath(pieceforpath.posx, pieceforpath.posy, occupied_white)
        elif pieceforpath.piecetype == 'pawn':
            return pawnpath(pieceforpath.posx, pieceforpath.posy, 'white', occupied_white, occupied_black)
        elif pieceforpath.piecetype == 'rock':
            return rockpath(pieceforpath.posx, pieceforpath.posy, occupied_white, occupied_black)
        elif pieceforpath.piecetype == 'bishop':
            return bishoppath(pieceforpath.posx, pieceforpath.posy, occupied_white, occupied_black)
        elif pieceforpath.piecetype == 'queen':
            return queenpath(pieceforpath.posx, pieceforpath.posy, occupied_white, occupied_black)
        else:
            return kingpath(pieceforpath.posx, pieceforpath.posy, occupied_white, dangerforwhite)
    else:
        pieceforpath = black[selectedp]

        if pieceforpath.piecetype == 'knight':
            return knightpath(pieceforpath.posx, pieceforpath.posy, occupied_black)
        elif pieceforpath.piecetype == 'pawn':
            return pawnpath(pieceforpath.posx, pieceforpath.posy, 'black', occupied_black, occupied_white)
        elif pieceforpath.piecetype == 'rock':
            return rockpath(pieceforpath.posx, pieceforpath.posy, occupied_black, occupied_white)
        elif pieceforpath.piecetype == 'bishop':
            return bishoppath(pieceforpath.posx, pieceforpath.posy, occupied_black, occupied_white)
        elif pieceforpath.piecetype == 'queen':
            return queenpath(pieceforpath.posx, pieceforpath.posy, occupied_black, occupied_white)
        else:
            return kingpath(pieceforpath.posx, pieceforpath.posy, occupied_black, dangerforblack)
def getattackpath( selectedp, st):
    # to be used by the bot.
    if selectedp == -1:
        return [(-100, -100,)]

    if st == 'white':
        pieceforpath = white[selectedp]

        if pieceforpath.piecetype == 'knight':
            return knightattackpath(pieceforpath.posx, pieceforpath.posy, occupied_white)
        elif pieceforpath.piecetype == 'pawn':
            return pawnattackpath(pieceforpath.posx, pieceforpath.posy, 'white', occupied_white, occupied_black)
        elif pieceforpath.piecetype == 'rock':
            return rockpath(pieceforpath.posx, pieceforpath.posy, occupied_white, occupied_black)
        elif pieceforpath.piecetype == 'bishop':
            return bishoppath(pieceforpath.posx, pieceforpath.posy, occupied_white, occupied_black)
        elif pieceforpath.piecetype == 'queen':
            return queenpath(pieceforpath.posx, pieceforpath.posy, occupied_white, occupied_black)
        else:
            return kingattackpath(pieceforpath.posx, pieceforpath.posy, occupied_white, dangerforwhite)
    else:
        pieceforpath = black[selectedp]

        if pieceforpath.piecetype == 'knight':
            return knightattackpath(pieceforpath.posx, pieceforpath.posy, occupied_black)
        elif pieceforpath.piecetype == 'pawn':
            return pawnattackpath(pieceforpath.posx, pieceforpath.posy, 'black', occupied_black, occupied_white)
        elif pieceforpath.piecetype == 'rock':
            return rockpath(pieceforpath.posx, pieceforpath.posy, occupied_black, occupied_white)
        elif pieceforpath.piecetype == 'bishop':
            return bishoppath(pieceforpath.posx, pieceforpath.posy, occupied_black, occupied_white)
        elif pieceforpath.piecetype == 'queen':
            return queenpath(pieceforpath.posx, pieceforpath.posy, occupied_black, occupied_white)
        else:
            return kingattackpath(pieceforpath.posx, pieceforpath.posy, occupied_black, dangerforblack)




# ==================================================================================================Member Functions
# ends


while True:
    # main loop.
    mouseclicked = False
    Screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclicked = True
    pseudomousepos = pygame.mouse.get_pos()



    if not gameover_:
        # if game is not over,
        mousepos = getmousepos(pseudomousepos)

        # all lists are cleared at the beginning of each iterations.
        occupied.clear()
        occupied_white.clear()
        occupied_black.clear()
        dangerforblack.clear()
        dangerforwhite.clear()

        for itr in range(len(black)):

            # converts the black pawn into black queen if the pawn is in the 8th row.
            temp_piece = black[itr]
            if temp_piece.piecetype == 'pawn' and temp_piece.posy == 8:
                temp_x_ = temp_piece.posx
                temp_y_ = temp_piece.posy
                black.pop(itr)
                black.append(piece(temp_x_, temp_y_, 'queen', imgqueenblack, 7))

            occupied.append((black[ itr].posx, black[ itr].posy,)) # occupied by any piece.
            occupied_black.append((black[ itr].posx, black[ itr].posy,)) # occupied by a black piece.
            dangerforwhite.extend( getattackpath( itr, 'black')) # to be used by the bot.



        for itr in range(len(white)):

            # converts the white pawn into white queen if the pawn is in the 1st row.
            temp_piece = white[itr]
            if temp_piece.piecetype == 'pawn' and temp_piece.posy == 1:
                temp_x_ = temp_piece.posx
                temp_y_ = temp_piece.posy
                white.pop(itr)
                white.append(piece(temp_x_, temp_y_, 'queen', imgqueenwhite, 7))

            occupied.append((white[ itr].posx, white[ itr].posy,)) # occupied by any piece.
            occupied_white.append(( white[ itr].posx, white[ itr].posy,)) # occupied by a white piece.
            dangerforblack.extend( getattackpath( itr, 'white')) # to be used by the bot.



        # ==================================================================================================Driver code

        if Turn == 'white':


            for piece_ in range(len(white)): # selects the desired piece.
                if white[piece_].posx == mousepos[0] and white[piece_].posy == mousepos[1] and mouseclicked == True:
                    selectedpiece = piece_

            possible_path = getpath(selectedpiece, 'white') # takes and stored the possible paths of the selected piece.
            # possible paths are the paths on which the piece can move. There is no guarantee of survival on possibla paths.

            if mousepos in possible_path and mouseclicked:
                # moves the piece to the new selected coordinate.
                white[ selectedpiece].posx = mousepos[ 0]
                white[ selectedpiece].posy = mousepos[ 1]

                if( white[ selectedpiece].piecetype == 'king'):
                    # if the selected piece is king, updates the variable storing the position of the king.
                    whiteKingPos = ( mousepos[ 0], mousepos[ 1],)

                Turn = 'black' # changes the value of the variable deciding the player who's turn is it next..

                val = 0
                while( val < len( black)):
                    # iterates over the black pieces looking wether if any piece is present at the selected coordinate.
                    if black[ val].posx == mousepos[ 0] and black[ val].posy == mousepos[ 1]:
                        # if a piece is present at the selected coordinate, deletes that piece immediately.
                        deletedelement = black[val]
                        black.pop( val)

                        if deletedelement.piecetype == 'king':
                            # if the deleted piece is the king, assigns True to the variable gameover_ and also declares white as the winner.
                            gameover_ = True
                            winner = 'w'
                            break


                    val += 1


                possible_path = []
                selectedpiece = -1










        if Turn == 'black':
            # the same program is repeated again with opposite values to that what was used for white.

            for piece_ in range(len(black)):
                if black[piece_].posx == mousepos[0] and black[piece_].posy == mousepos[1] and mouseclicked == True:
                    selectedpiece = piece_

            possible_path = getpath(selectedpiece, 'black')

            if mousepos in possible_path and mouseclicked:

                black[ selectedpiece].posx = mousepos[ 0]
                black[ selectedpiece].posy = mousepos[ 1]

                if( black[ selectedpiece].piecetype == 'king'):
                    blackKingPos = ( mousepos[ 0], mousepos[ 1])

                Turn = 'white'

                val = 0
                while( val < len( white)):

                    if white[ val].posx == mousepos[ 0] and white[ val].posy == mousepos[ 1]:
                        deletedelement = white[ val]
                        white.pop( val)

                        if deletedelement.piecetype == 'king':
                            gameover_ = True
                            winner = 'b'
                            break


                    val += 1

                selectedpiece = -1
                possible_path = []



        # ==================================================================================================Driver code ends


        # the status of the screen is updated.
        Screen.blit(board, (0, 0))
        Screen.blit(blue_box, (getposy(mousepos[0], mousepos[1]), getposx(mousepos[0], mousepos[1])))
        draw_possible_path( Turn, occupied_white, occupied_black)
        draw_kings_status()

        drawpieces()


    else:
        # if games is over,
        # the winner is displayed on the screen.
        if winner == 'w':
            Screen.blit( whitewins, ( 0, 0))
        elif winner == 'b':
            Screen.blit( blackwins, ( 0, 0))

    pygame.display.flip()
    # screen is updated with a descent frame rate.
    frame_rate.tick(20)

