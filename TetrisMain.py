'''
TetrisMain.py

This module contains the class "TetrisApp"

TetrisApp is a subclass of tkinter.Tk()

TetrisApp is the main module that controls the
running of the these modules:
    - Board 
    - Tetromino
    - ScoreTable
    - GameOver
    - MainMenu

last modified: August 19, 2021
by: Freeman Sun (GunesOzgur)

GitHub: GunesOzgur

---------------------------------------

TetrisApp class has these data attributes:

    - TetrisApp.keyFlagW,A,S,D: True, when the keys are pressed
        and False, when the keys are released

    - TetrisApp.gameOverFlag: True, when game over and
        False, when start or restart

    - TetrisApp.icon: App icon image handler

    - TetrisApp.canvas: tk.Canvas() of TetrisApp

    - TetrisApp.board: where the pieces move on.
        Board() object from "Board" module

    - TetrisApp.score: score table of the game.
        ScoreTable() object from "ScoreTable" module

    - TetrisApp.mainMenu: Main menu of the game.
        MainMenu() object from "MainMenu" module

    - TetrisApp.gameOver: Game Over window of the game.
        GameOver() object from "GameOver" module

    - TetrisApp.pieces: list of 7 tetrominos (tetris pieces)

    - TetrisApp.piece: current tetris piece

-----------------------------------------

TetrisApp class has these methods:

    - TetrisApp.initilize(): first initilization of TetrisApp
        datas and methods

    - TetrisApp.recursion(): recursive loop of tetris game

    - TetrisApp.keyPressed(): actions acc. to pressed keys

    - TetrisApp.keyReleased(): actions acc. to released keys
        (after press)

    - TetrisApp.newGame(): new game initilization

    - TetrisApp.newPiece(): return a random tetris piece

----------------------------------------

'''

import tkinter, random

import Board, Tetromino, ScoreTable, GameOver, MainMenu

class TetrisApp(tkinter.Tk):

    def initilize(self):
        self.keyFlagW = True
        self.keyFlagA = True
        self.keyFlagS = True
        self.keyFlagD = True
        #self.keyFlagR = True
        #self.keyFlagQ = True
        self.gameOverFlag = False
        
        self.title("Tetris")
        self.resizable(0, 0)

        # Icon
        self.icon = tkinter.PhotoImage(file="src/mino_green.png")
        self.wm_iconphoto(False, self.icon)

        self.canvas = tkinter.Canvas(self, width=450, height=350)
        self.canvas.pack()

        # Instruction image (W A S D)
        self.insImg = tkinter.PhotoImage(file="src/instruction.png")
        self.instruction = self.canvas.create_image(300+110, 232,
                                                    anchor=tkinter.NE,
                                                    image=self.insImg)

        self.board = Board.Board(self.canvas, 0, 0)
        self.score = ScoreTable.ScoreTable(self.canvas, 300, 10)
        self.mainMenu = MainMenu.MainMenu(self)
        self.gameOver = GameOver.GameOver(self.canvas, 15, 115)

        # Load pieces
        self.pieces = []
        self.pieces.append(Tetromino.T(self.board))
        self.pieces.append(Tetromino.L(self.board))
        self.pieces.append(Tetromino.J(self.board))
        self.pieces.append(Tetromino.O(self.board))
        self.pieces.append(Tetromino.I(self.board))
        self.pieces.append(Tetromino.S(self.board))
        self.pieces.append(Tetromino.Z(self.board))

        self.mainMenu.open()
        self.piece = self.newPiece()
        #self.newGame()

        self.bind("<KeyPress>", self.keyPressed)
        self.bind("<KeyRelease>", self.keyReleased)

    def recursion(self):
        if self.piece.moveDown(): # if picece can move downward
            self.board.update() # update board acc. to board.matrix
            self.canvas.after(1000, self.recursion) # repeat after a while
        else:
            self.piece.settle() # if piece settled
            for i in range(self.board.clearFulls()):
                self.score.increment() # increment score for each fulled row
            self.piece = self.newPiece()
            if self.piece.put(5,2): # if new piece can be put
                self.board.update() # update board acc. to board.matrix
                self.canvas.after(1000, self.recursion) # repeat after a while
            else: # if there is no space for a new piece
                self.gameOverFlag = True
                self.gameOver.display() # display "Game Over"
        
    def keyPressed(self, event):

        if event.char == 'w' or\
           event.char == 'W': # press "w" to rotate
            if self.keyFlagW:
                if self.piece.rotate():
                    self.board.update()
                self.keyFlagA = False
                
        elif event.char == 'a' or\
             event.char == 'A': # press "a" to move right-side
            if self.keyFlagA:
                if self.piece.moveLeft():
                    self.board.update()
                self.keyFlagA = False
                
        elif event.char == 's' or\
             event.char == 'S': # press "s" to move downward rapidly
            if self.keyFlagS:
                if self.piece.moveDown():
                    self.board.update()
                self.keyFlagS = False
            
        elif event.char == 'd' or\
             event.char == 'D': # press "d" to move left-side
            if self.keyFlagD:
                if self.piece.moveRight():
                    self.board.update()
                self.keyFlagD = False

        elif event.char == 'r' or\
             event.char == 'R': # press "r" to restart game
            if self.gameOverFlag:
                self.newGame()

        elif event.char == 'q' or\
             event.char == 'Q': # press "r" to restart game
            if self.gameOverFlag:
                self.mainMenu.open()
                #self.keyFlagQ = False
            
        elif event.char == 'm' or\
             event.char == 'M': # press "m" to print board.matrix
            self.board.printMtrx()

    def keyReleased(self, event):

        if event.char == 'w' or\
           event.char == 'W':
            self.keyFlagW = True
            
        elif event.char == 'a' or\
             event.char == 'A':
            self.keyFlagA = True
            
        elif event.char == 's' or\
             event.char == 'S':
            self.keyFlagS = True
            
        elif event.char == 'd' or\
             event.char == 'D':
            self.keyFlagD = True

        #elif event.char == 'r' or\
         #    event.char == 'R':
          #  self.keyFlagR = True

        #elif event.char == 'q' or\
         #    event.char == 'Q':
          #  self.keyFlagQ = True

        elif event.char == 'm' or\
             event.char == 'M':
            pass

    def newGame(self):
        self.score.zero()
        self.keyFlagR = False
        self.gameOverFlag = False
        self.gameOver.close()
        self.board.reset()
        self.piece.put(5,2)
        self.board.update()
        self.canvas.after(1000, self.recursion)

    def newPiece(self):
        return self.pieces[random.randint(0,len(self.pieces)-1)]
        #return self.pieces[-1]
        

if __name__ == "__main__":

    tetrisApp = TetrisApp()
    tetrisApp.initilize()
    tetrisApp.mainloop()
