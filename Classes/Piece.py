# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:01:08 2020

@author: Asger
"""

class Piece:
    def __init__(self,position,type_piece):
        self.position = position
        self.type_piece = type_piece
    
    def flip_piece(self):
        diction={'a' : 'h',
                 'b' : 'g',
                 'c' : 'f',
                 'd' : 'e',
                 'e' : 'd',
                 'f' : 'c',
                 'g' : 'b',
                 'h' : 'a',
                 '1' : '8',
                 '2' : '7',
                 '3' : '6',
                 '4' : '5',
                 '5' : '4',
                 '6' : '3',
                 '7' : '2',
                 '8' : '1'}
        self.position = diction[self.position[1]]+ diction[self.position[0]]
        return None



     
     




#print(piece1.position)
#print(piece1.type_piece)