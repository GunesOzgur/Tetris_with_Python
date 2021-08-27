'''
MainMenu.py

This module contains the class "MainMenu"

last modified: August 19, 2021
by: Freeman Sun (GunesOzgur)

GitHub: GunesOzgur

---------------------------------------

MainMenu class has these data attributes:

    - MainMenu.root: Tk() object (or subclass) that the
        main menu will be on

    - MainMenu.cnvs: Canvas() object that the main menu
        will be on
        
    - MainMenu.img: main menu background image
    
    - MainMenu.ID: main menu Canvas ID

    - MainMenu.StartX: x position of "start" button

    - MainMenu.StartY: y position of "start" button

    - MainMenu.startFlag: True, when "start" is pressed
        and False when "start" is released

    - MainMenu.sRlsImg: released "start" button image

    - MainMenu.sPrsImg: pressed "start" button image
    
    - MainMenu.startID: "start" button Canvas ID

    - MainMenu.QuitX: x position of "quit" button

    - MainMenu.QuitY: y position of "quit" button

    - MainMenu.quitFlag: True, when "quit" is pressed
        and False when "quit" is released

    - MainMenu.qRlsImg: released "quit" button image

    - MainMenu.qPrsImg: pressed "quit" button image
    
    - MainMenu.quitID: "quit" button Canvas ID

-----------------------------------------

MainMenu class has these methods:

    - MainMenu.open(): open (or make visible) the mainmenu
        window

    - MainMenu.close(): close (or make invisible) the mainmenu
        window

    - MainMenu._clicked(): make pressed the released
        buttons when clicked on them

    - MainMenu._released(): release the pressed buttons

----------------------------------------

'''

import tkinter as tk

src = "src/"

class MainMenu:

    def __init__(self, root):
        self.root = root
        self.cnvs = self.root.canvas

        self.img = tk.PhotoImage(file=src+"MainMenu.png")
        self.ID = self.cnvs.create_image(450, 0, anchor=tk.NE,
                                         image=self.img, state="hidden")
        # Put "start" button
        self.startX = 280
        self.startY = 200
        self.startFlag = False
        self.sRlsImg = tk.PhotoImage(file=src+"startButtonReleased.png")
        self.sPrsImg = tk.PhotoImage(file=src+"startButtonPressed.png")
        self.startID = self.cnvs.create_image(self.startX, self.startY,
                                              anchor=tk.NE,
                                              image=self.sRlsImg,
                                              state="hidden")
        # Put "quit" button        
        self.quitX = 280
        self.quitY = 260
        self.quitFlag = False
        self.qRlsImg = tk.PhotoImage(file=src+"quitButtonReleased.png")
        self.qPrsImg = tk.PhotoImage(file=src+"quitButtonPressed.png")
        self.quitID = self.cnvs.create_image(self.quitX, self.quitY,
                                             anchor=tk.NE,
                                             image=self.qRlsImg,
                                             state="hidden")
        

        self.cnvs.bind("<Button 1>", self._clicked)
        self.cnvs.bind("<ButtonRelease>", self._released)

    # open (or make visible) the mainmenu window
    def open(self):
        self.cnvs.itemconfig(self.ID, state="normal")
        self.cnvs.itemconfig(self.startID, state="normal")
        self.cnvs.itemconfig(self.quitID, state="normal")
        self.cnvs.tag_raise(self.ID)
        self.cnvs.tag_raise(self.startID)
        self.cnvs.tag_raise(self.quitID)

    # close (or make invisible) the mainmenu window
    def close(self):
        self.cnvs.itemconfig(self.ID, state="hidden")
        self.cnvs.itemconfig(self.startID, state="hidden")
        self.cnvs.itemconfig(self.quitID, state="hidden")

    # make pressed the released buttons when clicked on them
    def _clicked(self, event):
        # If "start" clicked
        if event.x < self.startX and\
           event.x > self.startX-120 and\
           event.y < self.startY+40 and\
           event.y > self.startY:
            self.startFlag= True
            self.cnvs.itemconfig(self.startID, image=self.sPrsImg)

        # If "quit" clicked
        elif event.x < self.quitX and\
             event.x > self.quitX-120 and\
             event.y < self.quitY+40 and\
             event.y > self.quitY:
            self.quitFlag= True
            self.cnvs.itemconfig(self.quitID, image=self.qPrsImg)

    # release the pressed buttons
    def _released(self, event):
        # If "start" button is pressed, release it
        if self.startFlag:
            self.startFlag = False
            self.cnvs.itemconfig(self.startID, image=self.sRlsImg)
            self.close()
            self.root.newGame()

        # If "quit" button is pressed, release it
        if self.quitFlag:
            self.quitFlag = False
            self.cnvs.itemconfig(self.quitID, image=self.qRlsImg)
            self.root.destroy()
