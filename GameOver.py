'''
GameOver.py

This module contains the class "GameOver"

last modified: August 19, 2021
by: Freeman Sun (GunesOzgur)

GitHub: GunesOzgur

---------------------------------------

GameOver class has these data attributes:

    - GameOver.cnvs: Canvas() object that the "Game Over"
        will be on
        
    - GameOver.x: horizontal position of the "Game Over"

    - GameOver.y: vertical position of the "Game Over"

    - GameOver.img: "Game Over" image

    - GameOver.ID: "Game Over" ID for Canvas

-----------------------------------------

ScoreTable class has these methods:

    - GameOver.display(): display "Game Over"
        VALUE

    - GameOver.close(): close (make invisible) "Game Over"

----------------------------------------

'''

import tkinter as tk

src = "src/"

class GameOver:

    def __init__(self, cnvs, x, y):
        self.cnvs = cnvs
        self.x = x+240
        self.y = y

        self.img = tk.PhotoImage(file=src+"GameOver.png")
        self.ID = self.cnvs.create_image(self.x, self.y, anchor=tk.NE,
                                         image=self.img, state='hidden')

    def display(self):
        self.cnvs.itemconfig(self.ID, state='normal')
        self.cnvs.tag_raise(self.ID)

    def close(self):
        
        self.cnvs.itemconfig(self.ID, state='hidden')
