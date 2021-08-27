'''
ScoreTable.py

This module contains the class "ScoreTable"

last modified: August 19, 2021
by: Freeman Sun (GunesOzgur)

GitHub: GunesOzgur

---------------------------------------

ScoreTable class has these data attributes:

    - ScoreTable.cnvs: Canvas() object that th score table
        will be on
        
    - ScoreTable.x: horizontal position of the score table

    - ScoreTable.y: vertical position of the score table

    - ScoreTable.value: the score value that will be displayed
        on the score table

    - ScoreTable.img: score table image

    - ScoreTable.figs[]: list of figures (from 0 to 9) that
        will be displayed

    - ScoreTable.ID: Score table's ID for Canvas

    - ScoreTable.d0ID: Digit0's ID for Canvas. Digit0 means
        the least significant digit (10e0)

    - ScoreTable.d1ID: digit1's ID for Canvas (10e1)

    - ScoreTable.d2ID: Digit2's ID for Canvas. Digit2 means
        the most significant digit (10e2)

-----------------------------------------

ScoreTable class has these methods:

    - ScoreTable.set(value): sets ScoreTable.value to VALUE

    - ScoreTable.increment(): increments ScoreTable.value by 1

    - ScoreTable.zero(): zeros the score table

----------------------------------------

'''

from tkinter import PhotoImage, NE

imgSrc = "src/"

class ScoreTable:

    def __init__(self, cnvs, x, y):
        self.cnvs = cnvs
        self.x = x
        self.y = y
        self.value = 0

        self.img = PhotoImage(file=imgSrc+"score.png")

        self.figs = []
        self.figs.append(PhotoImage(file=imgSrc+"0-30x40.png"))
        self.figs.append(PhotoImage(file=imgSrc+"1-30x40.png"))
        self.figs.append(PhotoImage(file=imgSrc+"2-30x40.png"))
        self.figs.append(PhotoImage(file=imgSrc+"3-30x40.png"))
        self.figs.append(PhotoImage(file=imgSrc+"4-30x40.png"))
        self.figs.append(PhotoImage(file=imgSrc+"5-30x40.png"))
        self.figs.append(PhotoImage(file=imgSrc+"6-30x40.png"))
        self.figs.append(PhotoImage(file=imgSrc+"7-30x40.png"))
        self.figs.append(PhotoImage(file=imgSrc+"8-30x40.png"))
        self.figs.append(PhotoImage(file=imgSrc+"9-30x40.png"))
        
        self.ID = self.cnvs.create_image(self.x+110, self.y, anchor=NE, image=self.img)

        self.d2ID =self.cnvs.create_image(self.x+36, self.y+34, anchor=NE, image=self.figs[0])
        self.d1ID =self.cnvs.create_image(self.x+70, self.y+34, anchor=NE, image=self.figs[0])
        self.d0ID =self.cnvs.create_image(self.x+104, self.y+34, anchor=NE, image=self.figs[0])

    def set(self, value):
        self.value = value
        self.cnvs.itemconfig(self.d0ID, image=self.figs[self.value%10])
        self.cnvs.itemconfig(self.d1ID, image=self.figs[int(self.value/10)%10])
        self.cnvs.itemconfig(self.d2ID, image=self.figs[int(self.value/100)%10])

    def increment(self):
        self.value += 1
        self.set(self.value)

    def zero(self):
        self.value = 0
        self.set(self.value)
