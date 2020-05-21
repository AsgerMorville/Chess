# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:44:41 2020

@author: Asger
"""

"""This class is the main chess-class. 
Holds:
 - Board object
 - List of Pieces alive
 - Whose turn is it?

Defs:
 - List of possible moves. (each move is a move object)
 - Handling the turn.
 	 - Update the board
 - Printing method.
 - playGame()
 """
 
from .Board import Board
from .Move import Move

class Chess:
    def __init__(self):
        self.board = Board()
        #self.pieces = Board.piece_list()
        self.pieces = 1
        self.turn = "W"
        self.counter = 0
    
    
    def handle_turn(self):
        rawmove = input("Put in your move: ")
        if rawmove == "done":
            raise ValueError("Game aborted")
            
        move = Move(rawmove)
        self.board.push(move)

    
    def switch_turn(self):
        if self.board.turn == "W":
            self.board.turn = "B"
        elif self.board.turn == "B":
            self.board.turn = "W"
        return None
    
    def possibleMoves():
        pass
    
    def play_game(self):
        print("Welcome to Chess. You will start as white.")
        self.board = Board()
        while self.board.not_over():
            self.board.display_board()
            self.handle_turn()
            self.switch_turn()
        return
    


    
         