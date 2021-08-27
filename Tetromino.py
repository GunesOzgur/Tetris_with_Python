'''
Tetromino.py

This module contains the class "Tetromino"
and its subclasses "T", "L", "J", "O", "I", "S", "Z"

last modified: August 19, 2021
by: Freeman Sun (GunesOzgur)

GitHub: GunesOzgur

---------------------------------------

Tetromino class and subclasses have these data attributes:

     - Tetromino.brd: The board that the pieces will move on
     
     - Tetromino.x0: mino 0 x position
     
     - Tetromino.y0: mino 0 y position
     
     - Tetromino.x1: mino 1 x position
     
     - Tetromino.y1: mino 1 y position
     
     - Tetromino.x2: mino 2 x position
     
     - Tetromino.y2: mino 2 y position
     
     - Tetromino.x3: mino 3 x position
     
     - Tetromino.y3: mino 3 y position

     - Tetromino.position: position info for rotation

     - Tetromino.bottom: list of squares at just under
     
     - Tetromino.left: list of squares at just left
     
     - Tetromino.right: list of squares at just right

     - Tetromino.mID0: mino 0 Canvas ID
     
     - Tetromino.mID1: mino 1 Canvas ID
     
     - Tetromino.mID2: mino 2 Canvas ID
     
     - Tetromino.mID3: mino 3 Canvas ID

-----------------------------------------

Tetromino class has these methods:

    - Tetromino.settle(): turn red the settled pieces

    - Tetromino.moveDown(): move the piece to the downward

    - Tetromino.moveLeft(): move the piece to the left-side

    - Tetromino.moveRight(): move the piece to the right-side


Tetromino subclasses have these methods:

    - Tetromino.put(): put the (new) piece on the board

    - Tetromino.rotate(): rotate the piece

    - Tetromino.updateNeighbor(): update Tetromino.bottom,
         Tetromino.right, and Tetromino.left

----------------------------------------

'''

import random

class Tetromino:

     def __init__(self, board):
          self.brd = board
          self.x0 = 0
          self.y0 = 0
          self.x1 = 0
          self.y1 = 0
          self.x2 = 0
          self.y2 = 0
          self.x3 = 0
          self.y3 = 0

          self.position = 0

          # neighbor matrices
          self.bottom=[]
          self.left=[]
          self.right=[]

          self.mID0 = 0
          self.mID1 = 0
          self.mID2 = 0
          self.mID3 = 0

# Tetromino.settle() : turn red settled blocks
     def settle(self):
          self.brd.write(self.x0, self.y0, self.brd.RED)
          self.brd.write(self.x1, self.y1, self.brd.RED)
          self.brd.write(self.x2, self.y2, self.brd.RED)
          self.brd.write(self.x3, self.y3, self.brd.RED)

# Tetromino.moveDown() : move blocks to down-side
     def moveDown(self):
          a = True
          for j in range(len(self.bottom)):
               a &=  not bool(self.brd.mtrx[self.bottom[j][1]][self.bottom[j][0]])
                    
          if a:
               self.brd.write(self.x0, self.y0, self.brd.EMPTY)
               self.brd.write(self.x1, self.y1, self.brd.EMPTY)
               self.brd.write(self.x2, self.y2, self.brd.EMPTY)
               self.brd.write(self.x3, self.y3, self.brd.EMPTY)
               self.y0 += 1
               self.y1 += 1
               self.y2 += 1
               self.y3 += 1
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)
               
               self.updateNeighbor()
               return True
          else:
               return False

# Tetromino.moveLeft() : move blocks to left-side
     def moveLeft(self):
          a = True
          for j in range(len(self.left)):
               a &=  not bool(self.brd.mtrx[self.left[j][1]][self.left[j][0]])
                    
          if a:
               self.brd.write(self.x0, self.y0, self.brd.EMPTY)
               self.brd.write(self.x1, self.y1, self.brd.EMPTY)
               self.brd.write(self.x2, self.y2, self.brd.EMPTY)
               self.brd.write(self.x3, self.y3, self.brd.EMPTY)
               self.x0 -= 1
               self.x1 -= 1
               self.x2 -= 1
               self.x3 -= 1
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)
               
               self.updateNeighbor()
               return True
          else:
               return False


# Tetromino.moveRight() : move blocks to right-side
     def moveRight(self):
          a = True
          for j in range(len(self.right)):
               a &=  not bool(self.brd.mtrx[self.right[j][1]][self.right[j][0]])
                    
          if a:
               self.brd.write(self.x0, self.y0, self.brd.EMPTY)
               self.brd.write(self.x1, self.y1, self.brd.EMPTY)
               self.brd.write(self.x2, self.y2, self.brd.EMPTY)
               self.brd.write(self.x3, self.y3, self.brd.EMPTY)
               self.x0 += 1
               self.x1 += 1
               self.x2 += 1
               self.x3 += 1
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)
               
               self.updateNeighbor()
               return True
          else:
               return False


class T(Tetromino):
#    1  0  3
#    _  _  _
#   |_||_||_|
#      |_|
#       2

# T.put()
     def put(self, x0, y0):
          self.x0 = x0
          self.y0 = y0
          self.x1 = x0-1
          self.y1 = y0
          self.x2 = x0
          self.y2 = y0+1
          self.x3 = x0+1
          self.y3 = y0

          if self.brd.mtrx[self.y0][self.x0] == 0 and \
             self.brd.mtrx[self.y1][self.x1] == 0 and \
             self.brd.mtrx[self.y2][self.x2] == 0 and \
             self.brd.mtrx[self.y3][self.x3] == 0:
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)

               self.position = 0

               self.updateNeighbor()
               return True
          else:
               return False

# T.rotate()
     def rotate(self):

          # Mino 1 to top of Mino 0
          if self.position == 0:
               if self.brd.mtrx[self.y0-1][self.x0] == 0:
                    self.brd.mtrx[self.y1][self.x1] = 0
                    self.x1 = self.x0
                    self.y1 = self.y0-1
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN

                    self.position = 1
                    self.updateNeighbor()
                    return True
               else:
                    return False

          # Mino 2 to left of Mino 0
          elif self.position == 1:
               if self.brd.mtrx[self.y0][self.x0-1] == 0:
                    self.brd.mtrx[self.y2][self.x2] = 0
                    self.x2 = self.x0-1
                    self.y2 = self.y0
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN

                    self.position = 2
                    self.updateNeighbor()
                    return True
               else:
                    return False

          # Mino 3 to under Mino 0
          elif self.position == 2:
               if self.brd.mtrx[self.y0+1][self.x0] == 0:
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x3 = self.x0
                    self.y3 = self.y0+1
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 3
                    self.updateNeighbor()
                    return True
               else:
                    return False

          # Back to the 1st position
          elif self.position == 3:
               if self.brd.mtrx[self.y0][self.x0+1] == 0:
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.x1 = self.x0-1
                    self.y1 = self.y0
                    self.x2 = self.x0
                    self.y2 = self.y0+1
                    self.x3 = self.x0+1
                    self.y3 = self.y0
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 0
                    self.updateNeighbor()
                    return True
               else:
                    return False

# T.updateNeighbor()
     def updateNeighbor(self):
          if self.position == 0:
               self.bottom = [[self.x1, self.y1+1],
                              [self.x2, self.y2+1],
                              [self.x3, self.y3+1]]
               
               self.left = [[self.x1-1, self.y1],
                            [self.x2-1, self.y2]]
          
               self.right = [[self.x2+1, self.y2],
                             [self.x3+1, self.y3]]

          elif self.position == 1:
               self.bottom = [[self.x2, self.y2+1],
                              [self.x3, self.y3+1]]

               self.left = [[self.x0-1, self.y0],
                            [self.x1-1, self.y1],
                            [self.x2-1, self.y2]]

               self.right = [[self.x1+1, self.y1],
                             [self.x2+1, self.y2],
                             [self.x3+1, self.y3]]

          elif self.position == 2:
               self.bottom = [[self.x0, self.y0+1],
                              [self.x2, self.y2+1],
                              [self.x3, self.y3+1]]

               self.left = [[self.x1-1, self.y1],
                            [self.x2-1, self.y2]]

               self.right = [[self.x1+1, self.y1],
                             [self.x3+1, self.y3]]

          elif self.position == 3:
               self.bottom = [[self.x2, self.y2+1],
                              [self.x3, self.y3+1]]
               

               self.left = [[self.x1-1, self.y1],
                            [self.x2-1, self.y2],
                            [self.x3-1, self.y3]]

               self.right = [[self.x0+1, self.y0],
                             [self.x1+1, self.y1],
                             [self.x3+1, self.y3]]



class L(Tetromino):
#      _
#   1 |_|
#   0 |_| _
#   2 |_||_|
#         3

# L.put()
     def put(self, x0, y0):
          self.x0 = x0
          self.y0 = y0
          self.x1 = x0
          self.y1 = y0-1
          self.x2 = x0
          self.y2 = y0+1
          self.x3 = x0+1
          self.y3 = y0+1

          if self.brd.mtrx[self.y0][self.x0] == 0 and \
             self.brd.mtrx[self.y1][self.x1] == 0 and \
             self.brd.mtrx[self.y2][self.x2] == 0 and \
             self.brd.mtrx[self.y3][self.x3] == 0:
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)

               self.position = 0

               self.updateNeighbor()
               return True
          else:
               return False

# L.rotate()
     def rotate(self):

# L position 0 to postion 1
          if self.position == 0:
               if self.brd.mtrx[self.y0][self.x0-1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0][self.x0+1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0+1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0-1
                    self.y1 = self.y0
                    self.x2 = self.x0+1
                    self.y2 = self.y0
                    self.x3 = self.x0+1
                    self.y3 = self.y0-1
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 1
                    self.updateNeighbor()
                    return True
               else:
                    return False

# L position 1 to postion 2
          elif self.position == 1:
               if self.brd.mtrx[self.y0+1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0-1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0
                    self.y1 = self.y0+1
                    self.x2 = self.x0
                    self.y2 = self.y0-1
                    self.x3 = self.x0-1
                    self.y3 = self.y0-1
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 2
                    self.updateNeighbor()
                    return True
               else:
                    return False

# L position 2 to postion 3
          elif self.position == 2:
               if self.brd.mtrx[self.y0][self.x0+1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0][self.x0-1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0+1][self.x0-1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0+1
                    self.y1 = self.y0
                    self.x2 = self.x0-1
                    self.y2 = self.y0
                    self.x3 = self.x0-1
                    self.y3 = self.y0+1
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 3
                    self.updateNeighbor()
                    return True
               else:
                    return False

# L position 3 to postion 0
          elif self.position == 3:
               if self.brd.mtrx[self.y0-1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0+1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0+1][self.x0+1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0
                    self.y1 = self.y0-1
                    self.x2 = self.x0
                    self.y2 = self.y0+1
                    self.x3 = self.x0+1
                    self.y3 = self.y0+1
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 0
                    self.updateNeighbor()
                    return True
               else:
                    return False

# L.updateNeighbor()
     def updateNeighbor(self):

# L position 0
          if self.position == 0:
               self.bottom = [[self.x2, self.y2+1],
                              [self.x3, self.y3+1]]
               
               self.left = [[self.x0-1, self.y0],
                            [self.x1-1, self.y1],
                            [self.x2-1, self.y2]]
          
               self.right = [[self.x0+1, self.y0],
                             [self.x1+1, self.y1],
                             [self.x3+1, self.y3]]

# L position 1
          elif self.position == 1:
               self.bottom = [[self.x0, self.y0+1],
                              [self.x1, self.y1+1],
                              [self.x2, self.y2+1]]

               self.left = [[self.x1-1, self.y1],
                            [self.x3-1, self.y3]]

               self.right = [[self.x2+1, self.y2],
                             [self.x3+1, self.y3]]

# L position 2
          elif self.position == 2:
               self.bottom = [[self.x1, self.y1+1],
                              [self.x3, self.y3+1]]

               self.left = [[self.x0-1, self.y0],
                            [self.x1-1, self.y1],
                            [self.x3-1, self.y3]]

               self.right = [[self.x0+1, self.y0],
                             [self.x1+1, self.y1],
                             [self.x2+1, self.y2]]

# L position 3
          elif self.position == 3:
               self.bottom = [[self.x0, self.y0+1],
                              [self.x1, self.y1+1],
                              [self.x3, self.y3+1]]
               
               self.left = [[self.x2-1, self.y2],
                            [self.x3-1, self.y3]]

               self.right = [[self.x1+1, self.y1],
                             [self.x3+1, self.y3]]


class J(Tetromino):
#        _
#       |_|1
#     _ |_|0
#   3|_||_|2
#      

# J.put()
     def put(self, x0, y0):
          self.x0 = x0
          self.y0 = y0
          self.x1 = x0
          self.y1 = y0-1
          self.x2 = x0
          self.y2 = y0+1
          self.x3 = x0-1
          self.y3 = y0+1

          if self.brd.mtrx[self.y0][self.x0] == 0 and \
             self.brd.mtrx[self.y1][self.x1] == 0 and \
             self.brd.mtrx[self.y2][self.x2] == 0 and \
             self.brd.mtrx[self.y3][self.x3] == 0:
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)

               self.position = 0

               self.updateNeighbor()
               return True
          else:
               return False

# J.rotate()
     def rotate(self):

     # J position 0 to postion 1
          if self.position == 0:
               if self.brd.mtrx[self.y0][self.x0-1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0][self.x0+1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0+1][self.x0+1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0-1
                    self.y1 = self.y0
                    self.x2 = self.x0+1
                    self.y2 = self.y0
                    self.x3 = self.x0+1
                    self.y3 = self.y0+1
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 1
                    self.updateNeighbor()
                    return True
               else:
                    return False

     # J position 1 to postion 2
          elif self.position == 1:
               if self.brd.mtrx[self.y0+1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0+1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0
                    self.y1 = self.y0+1
                    self.x2 = self.x0
                    self.y2 = self.y0-1
                    self.x3 = self.x0+1
                    self.y3 = self.y0-1
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 2
                    self.updateNeighbor()
                    return True
               else:
                    return False

     # J position 2 to postion 3
          elif self.position == 2:
               if self.brd.mtrx[self.y0][self.x0+1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0][self.x0-1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0-1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0+1
                    self.y1 = self.y0
                    self.x2 = self.x0-1
                    self.y2 = self.y0
                    self.x3 = self.x0-1
                    self.y3 = self.y0-1
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 3
                    self.updateNeighbor()
                    return True
               else:
                    return False

     # J position 3 to postion 0
          elif self.position == 3:
               if self.brd.mtrx[self.y0-1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0+1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0+1][self.x0-1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0
                    self.y1 = self.y0-1
                    self.x2 = self.x0
                    self.y2 = self.y0+1
                    self.x3 = self.x0-1
                    self.y3 = self.y0+1
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 0
                    self.updateNeighbor()
                    return True
               else:
                    return False

# J.updateNeighbor()
     def updateNeighbor(self):

     # J position 0
          if self.position == 0:
               self.bottom = [[self.x2, self.y2+1],
                              [self.x3, self.y3+1]]
               
               self.left = [[self.x0-1, self.y0],
                            [self.x1-1, self.y1],
                            [self.x3-1, self.y3]]
          
               self.right = [[self.x0+1, self.y0],
                             [self.x1+1, self.y1],
                             [self.x2+1, self.y2]]

     # J position 1
          elif self.position == 1:
               self.bottom = [[self.x0, self.y0+1],
                              [self.x1, self.y1+1],
                              [self.x3, self.y3+1]]

               self.left = [[self.x1-1, self.y1],
                            [self.x3-1, self.y3]]

               self.right = [[self.x2+1, self.y2],
                             [self.x3+1, self.y3]]

     # J position 2
          elif self.position == 2:
               self.bottom = [[self.x1, self.y1+1],
                              [self.x3, self.y3+1]]

               self.left = [[self.x0-1, self.y0],
                            [self.x1-1, self.y1],
                            [self.x2-1, self.y2]]

               self.right = [[self.x0+1, self.y0],
                             [self.x1+1, self.y1],
                             [self.x3+1, self.y3]]

     # J position 3
          elif self.position == 3:
               self.bottom = [[self.x0, self.y0+1],
                              [self.x1, self.y1+1],
                              [self.x2, self.y2+1]]
               
               self.left = [[self.x2-1, self.y2],
                            [self.x3-1, self.y3]]

               self.right = [[self.x1+1, self.y1],
                             [self.x3+1, self.y3]]

class O(Tetromino):
#     _  _
#   0|_||_|3
#   1|_||_|2
#      

# O.put()
     def put(self, x0, y0):
          self.x0 = x0
          self.y0 = y0
          self.x1 = x0
          self.y1 = y0+1
          self.x2 = x0+1
          self.y2 = y0+1
          self.x3 = x0+1
          self.y3 = y0

          if self.brd.mtrx[self.y0][self.x0] == self.brd.EMPTY and \
             self.brd.mtrx[self.y1][self.x1] == self.brd.EMPTY and \
             self.brd.mtrx[self.y2][self.x2] == self.brd.EMPTY and \
             self.brd.mtrx[self.y3][self.x3] == self.brd.EMPTY:
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)

               self.position = 0

               self.bottom = [[self.x1, self.y1+1],
                              [self.x2, self.y2+1]]
               
               self.left = [[self.x0-1, self.y0],
                            [self.x1-1, self.y1]]
          
               self.right = [[self.x2+1, self.y2],
                             [self.x3+1, self.y3]]
               return True
          else:
               return False

# O.rotate()
     def rotate(self):
          pass
     
# O.updateNeighbor()
     def updateNeighbor(self):
          self.bottom = [[self.x1, self.y1+1],
                         [self.x2, self.y2+1]]
               
          self.left = [[self.x0-1, self.y0],
                       [self.x1-1, self.y1]]
          
          self.right = [[self.x2+1, self.y2],
                        [self.x3+1, self.y3]]


class I(Tetromino):
#        _  _  _  _
#       |_||_||_||_|
#        1  0  2  3


# I.put()
     def put(self, x0, y0):
          self.x0 = x0
          self.y0 = y0
          self.x1 = x0-1
          self.y1 = y0
          self.x2 = x0+1
          self.y2 = y0
          self.x3 = x0+2
          self.y3 = y0

          if self.brd.mtrx[self.y0][self.x0] == 0 and \
             self.brd.mtrx[self.y1][self.x1] == 0 and \
             self.brd.mtrx[self.y2][self.x2] == 0 and \
             self.brd.mtrx[self.y3][self.x3] == 0:
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)

               self.position = 0

               self.updateNeighbor()
               return True
          else:
               return False

# I.rotate()
     def rotate(self):

     # I position 0 to postion 1
          if self.position == 0:
               if self.brd.mtrx[self.y0+1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-2][self.x0] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0
                    self.y1 = self.y0+1
                    self.x2 = self.x0
                    self.y2 = self.y0-1
                    self.x3 = self.x0
                    self.y3 = self.y0-2
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 1
                    self.updateNeighbor()
                    return True
               else:
                    return False

     # I position 1 to postion 0
          elif self.position == 1:
               if self.brd.mtrx[self.y0][self.x0-1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0][self.x0+1] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0][self.x0+2] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y1][self.x1] = self.brd.EMPTY
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x1 = self.x0-1
                    self.y1 = self.y0
                    self.x2 = self.x0+1
                    self.y2 = self.y0
                    self.x3 = self.x0+2
                    self.y3 = self.y0
                    self.brd.mtrx[self.y1][self.x1] = self.brd.GREEN
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 0
                    self.updateNeighbor()
                    return True
               else:
                    return False


# I.updateNeighbor()
     def updateNeighbor(self):

     # I position 0
          if self.position == 0:
               self.bottom = [[self.x0, self.y0+1],
                              [self.x1, self.y1+1],
                              [self.x2, self.y2+1],
                              [self.x3, self.y3+1]]
               
               self.left = [[self.x1-1, self.y1]]
          
               self.right = [[self.x3+1, self.y3]]

     # I position 1
          elif self.position == 1:
               self.bottom = [[self.x1, self.y1+1]]

               self.left = [[self.x0-1, self.y0],
                            [self.x1-1, self.y1],
                            [self.x2-1, self.y2],
                            [self.x3-1, self.y3]]

               self.right = [[self.x0+1, self.y0],
                             [self.x1+1, self.y1],
                             [self.x2+1, self.y2],
                             [self.x3+1, self.y3]]


class S(Tetromino):
     
#        2  3
#        _  _
#     _ |_||_|
#    |_||_|
#
#     1  0


# S.put()
     def put(self, x0, y0):
          self.x0 = x0
          self.y0 = y0
          self.x1 = x0-1
          self.y1 = y0
          self.x2 = x0
          self.y2 = y0-1
          self.x3 = x0+1
          self.y3 = y0-1

          if self.brd.mtrx[self.y0][self.x0] == 0 and \
             self.brd.mtrx[self.y1][self.x1] == 0 and \
             self.brd.mtrx[self.y2][self.x2] == 0 and \
             self.brd.mtrx[self.y3][self.x3] == 0:
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)

               self.position = 0

               self.updateNeighbor()
               return True
          else:
               return False

# S.rotate()
     def rotate(self):

     # S position 0 to postion 1
          if self.position == 0:
               if self.brd.mtrx[self.y0+1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0-1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x2 = self.x0
                    self.y2 = self.y0+1
                    self.x3 = self.x0-1
                    self.y3 = self.y0-1
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 1
                    self.updateNeighbor()
                    return True
               else:
                    return False

     # S position 1 to postion 0
          elif self.position == 1:
               if self.brd.mtrx[self.y0-1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0+1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x2 = self.x0
                    self.y2 = self.y0-1
                    self.x3 = self.x0+1
                    self.y3 = self.y0-1
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 0
                    self.updateNeighbor()
                    return True
               else:
                    return False


# S.updateNeighbor()
     def updateNeighbor(self):

     # S position 0
          if self.position == 0:
               self.bottom = [[self.x0, self.y0+1],
                              [self.x1, self.y1+1],
                              [self.x3, self.y3+1]]
               
               self.left = [[self.x1-1, self.y1],
                            [self.x2-1, self.y2]]
          
               self.right = [[self.x0+1, self.y0],
                             [self.x3+1, self.y3]]

     # S position 1
          elif self.position == 1:
               self.bottom = [[self.x1, self.y1+1],
                              [self.x2, self.y2+1]]

               self.left = [[self.x1-1, self.y1],
                            [self.x2-1, self.y2],
                            [self.x3-1, self.y3]]

               self.right = [[self.x0+1, self.y0],
                             [self.x2+1, self.y2],
                             [self.x3+1, self.y3]]


class Z(Tetromino):
     
#     3  2
#     _  _
#    |_||_| _
#       |_||_|
#
#        0  1


# Z.put()
     def put(self, x0, y0):
          self.x0 = x0
          self.y0 = y0
          self.x1 = x0+1
          self.y1 = y0
          self.x2 = x0
          self.y2 = y0-1
          self.x3 = x0-1
          self.y3 = y0-1

          if self.brd.mtrx[self.y0][self.x0] == 0 and \
             self.brd.mtrx[self.y1][self.x1] == 0 and \
             self.brd.mtrx[self.y2][self.x2] == 0 and \
             self.brd.mtrx[self.y3][self.x3] == 0:
               self.brd.write(self.x0, self.y0, self.brd.GREEN)
               self.brd.write(self.x1, self.y1, self.brd.GREEN)
               self.brd.write(self.x2, self.y2, self.brd.GREEN)
               self.brd.write(self.x3, self.y3, self.brd.GREEN)

               self.position = 0

               self.updateNeighbor()
               return True
          else:
               return False

# S.rotate()
     def rotate(self):

     # Z position 0 to postion 1
          if self.position == 0:
               if self.brd.mtrx[self.y0+1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0+1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x2 = self.x0
                    self.y2 = self.y0+1
                    self.x3 = self.x0+1
                    self.y3 = self.y0-1
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 1
                    self.updateNeighbor()
                    return True
               else:
                    return False

     # Z position 1 to postion 0
          elif self.position == 1:
               if self.brd.mtrx[self.y0-1][self.x0] == self.brd.EMPTY and\
                  self.brd.mtrx[self.y0-1][self.x0-1] == self.brd.EMPTY:
                    
                    self.brd.mtrx[self.y2][self.x2] = self.brd.EMPTY
                    self.brd.mtrx[self.y3][self.x3] = self.brd.EMPTY
                    self.x2 = self.x0
                    self.y2 = self.y0-1
                    self.x3 = self.x0-1
                    self.y3 = self.y0-1
                    self.brd.mtrx[self.y2][self.x2] = self.brd.GREEN
                    self.brd.mtrx[self.y3][self.x3] = self.brd.GREEN

                    self.position = 0
                    self.updateNeighbor()
                    return True
               else:
                    return False


# Z.updateNeighbor()
     def updateNeighbor(self):

     # Z position 0
          if self.position == 0:
               self.bottom = [[self.x0, self.y0+1],
                              [self.x1, self.y1+1],
                              [self.x3, self.y3+1]]
               
               self.left = [[self.x0-1, self.y0],
                            [self.x3-1, self.y3]]
          
               self.right = [[self.x1+1, self.y1],
                             [self.x2+1, self.y2]]

     # Z position 1
          elif self.position == 1:
               self.bottom = [[self.x1, self.y1+1],
                              [self.x2, self.y2+1]]

               self.left = [[self.x0-1, self.y0],
                            [self.x2-1, self.y2],
                            [self.x3-1, self.y3]]

               self.right = [[self.x1+1, self.y1],
                             [self.x2+1, self.y2],
                             [self.x3+1, self.y3]]

