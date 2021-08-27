'''
Board.py

This module contains the class "Board"

Board is where the pieces move on

last modified: August 19, 2021
by: Freeman Sun (GunesOzgur)

GitHub: GunesOzgur

---------------------------------------

Board class has these data attributes:

    - Board.cnvs: Canvas() object that the board will be on
        
    - Board.x: horizontal position of the board

    - Board.y: vertical position of the board

    - Board.bgEven: square image for checked background

    - Board.bgOdd: square image for checked background

    - Board.green: green mino image for moving pieces

    - Board.red: red mino image for settled pieces

    - Board.EMPTY: value of empty squares on board matrix

    - Board.GREEN: value of green minos on board matrix

    - Board.RED: value of red minos on board matrix

    - Board.fullRows: list of filled rows

    - Board.mtrx: matrix for square values

    - Board.sqrID: matrix Canvas IDs of visible squares

-----------------------------------------

Board class has these methods:

    - Board.update(): update board acc. to board matrix

    - Board.clearFulls(): find and clear filled rows

    - Board.printMtrx(): print matrix values

    - Board.write(x, y, value): change the board matrix
        elements (square values)

    - Board.reset(): reset the board matrix

----------------------------------------

'''

import tkinter as tk

src = "src/"

class Board:

    def __init__(self, cnvs, x, y):
        self.x = x
        self.y = y
        self.cnvs = cnvs

        self.bgEven = tk.PhotoImage(file=src+"bg0.png")
        self.bgOdd = tk.PhotoImage(file=src+"bg1.png")
        self.green = tk.PhotoImage(file=src+"mino_green.png")
        self.red = tk.PhotoImage(file=src+"mino_red.png")

        self.EMPTY = 0
        self.GREEN = 2
        self.RED = 3

        self.fullRows = []

        # Matrix for square values
        #             0  1  2  3  4  5  6  7  8  9  10
        self.mtrx = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 0 invisible
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 1 invisible
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 2 invisible
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 3
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 4
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 5
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 6
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 7
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 8
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 9
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 10
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 11
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 12
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 13
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] # 14 invisible

        # Matrix for tkinter.Canvas IDs
        #              0  1  2  3  4  5  6  7  8  9  10
        self.sqrID = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 1
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 2
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 3
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 4
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 5
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 6
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 7
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 8
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 9
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 10
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 11
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 12
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] # 13
                      # for the 14th row ID not necessary
        


        # initial print of board
        # from row 3 to row 13 (the visible ones)
        for j in range(3, len(self.mtrx)-1):
            # the first and the last elements of a row are
            # parts of the board frame
            # no need to print them
            for i in range(1, len(self.mtrx[1])-1):
                # If the square is empty
                if self.mtrx[j][i] == self.EMPTY:
                    if (i+j)%2:
                        self.sqrID[j][i] = self.cnvs.create_image(
                            30*i+self.x,
                            30*(j-3)+self.y,
                            anchor=tk.NE,
                            image=self.bgOdd)
                        
                    else:
                        self.sqrID[j][i] = self.cnvs.create_image(
                            30*i+self.x,
                            30*(j-3)+self.y,
                            anchor=tk.NE,
                            image=self.bgEven)

                # If the square is green
                elif self.mtrx[j][i] == self.GREEN:
                    self.sqrID[j][i] = self.cnvs.create_image(
                        30*i+self.x,
                        30*(j-3)+self.y,
                        anchor=tk.NE,
                        image=self.green)

                # If the square is red
                elif self.mtrx[j][i] == self.RED:
                    self.sqrID[j][i] = self.cnvs.create_image(
                        30*i+self.x,
                        30*(j-3)+self.y,
                        anchor=tk.NE,
                        image=self.red)

    #def printIDs(self):
     #   for j in range(1, len(self.mtrx)-1):
      #      for i in range(1, len(self.mtrx[1])-1):
       #         print("[",j,"][",i,"]: ", self.sqrID[j][i])

    def update(self):
        for j in range(3, len(self.mtrx)-1):
            for i in range(1, len(self.mtrx[1])-1):
                if self.mtrx[j][i] == self.EMPTY:
                    if (i+j)%2:
                        self.cnvs.itemconfig(self.sqrID[j][i], image=self.bgOdd)
                    else:
                        self.cnvs.itemconfig(self.sqrID[j][i], image=self.bgEven)

                elif self.mtrx[j][i] == self.GREEN:
                    self.cnvs.itemconfig(self.sqrID[j][i], image=self.green)
                    

                elif self.mtrx[j][i] == self.RED:
                    self.cnvs.itemconfig(self.sqrID[j][i], image=self.red)

    def clearFulls(self):
        self.point = 0 # reset point
        # Look for the full rows from top to bottom
        for j in range(3, len(self.mtrx)-1):
            if self.mtrx[j].count(0) == 0:
                # If a full row is detected, crear it
                for i in range(1,len(self.mtrx[j])):
                    self.mtrx[j][i] = 0

                self.point += 1 # count point
                
                # After clearing, pull down the blocks above
                for j2 in range(-j, -1):
                    self.mtrx[-j2] = self.mtrx[-j2-1].copy()

        return self.point

    def printMtrx(self):
        for j in range(len(self.mtrx)):
            print(self.mtrx[j])

    def write(self, x, y, value):
        self.mtrx[y][x] = value

    def reset(self):
        for j in range(1, len(self.mtrx)-1):
            for i in range(1, len(self.mtrx[1])-1):
                self.mtrx[j][i] = 0
                
