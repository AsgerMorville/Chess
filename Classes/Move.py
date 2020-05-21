# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:18:03 2020

@author: Asger

This checks an input move. Is it legal, ie. does the two squares fall within the board?
"""

class Move:
    def __init__(self,cons):
        if isinstance(cons,str):
            move = string_to_move(cons)
            self.curr = move[0]
            self.desired = move[1]
        elif isinstance(cons,list):
            self.curr = cons[0]
            self.desired = cons[1]
        else: 
            raise ValueError('Move is of illegal type. Should be either string or list')
            
    def curr(self):
        return(self.curr)
    def desired(self):
        return(self.desired)
    
def string_to_move(string):
        moves = []
        if len(string) == 4:
            moves.append(string[0:2])
            moves.append(string[2:4])
        else:
            ValueError('Move string not of length 4.')
        return moves