# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:01:08 2020

@author: Asger
"""

class Piece:
    def __init__(self,position,type_piece):
        self.position = position
        self.type_piece = type_piece
    



     
     



piece1 = Piece("a3","rook")
piece2 = Piece("b3","rook")
piece3 = Piece("a4","knight")
piece4 = Piece("a5","rook")
piece5 = Piece("a6","rook")
piece6 = Piece("a7","rook") 

x2 = [[piece1,piece2],[piece3,piece4]]

#2dlist = [[piece1,piece2,piece3],[piece4,piece5,piece6]]
#x = [["a" for item in range(0,5)],["a" for item in range(0,5)]]
for p in x2[1]:
    if p.position == "a4":
        print(p.type_piece)


#print(piece1.position)
#print(piece1.type_piece)