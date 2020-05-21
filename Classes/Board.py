# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:00:59 2020

@author: Asger
"""
import numpy as np
from .Piece import Piece


class Board:
    def __init__(self):
        self.pieces = self.array_initializer()
        self.castling = True
        self.turn = "W"
        self.piece_list = self.init()
        self.pseudo_legal_moves = self.pseudo_legal_moves()
        self.real_legal_moves = self.real_legal_moves()
        
    def real_legal_moves(self):
        pass
    def pseudo_legal_moves(self):
        moves = []
        for p in self.piece_list[self.turn_index(self.turn)]:
            moves.append(self.piece_moves(p))
        return(moves)
    
    def piece_moves(self,piece):
        if piece.type_piece == "pawn":
            return(self.pawn_moves(piece.position))
        if piece.type_piece == "knight":
            return(self.knight_moves(piece.position))
        if piece.type_piece == "bishop":
            return(self.bishop_moves(piece.position))
        if piece.type_piece == "rook":
            return(self.rook_moves(piece.position))
        if piece.type_piece == "queen":
            return(self.queen_moves(piece.position))
        if piece.type_piece == "king":
            return(self.king_moves(piece.position))
    
    @staticmethod
    def pos_converter(pos):
        #pos is a string
        diction = {
        'a' : 2,
        'b' : 3,
        'c' : 4,
        'd' : 5,
        'e' : 6,
        'f' : 7,
        'g' : 8,
        'h' : 9,
        '1' : 9,
        '2' : 8,
        '3' : 7,
        '4' : 6,
        '5' : 5,
        '6' : 4,
        '7' : 3,
        '8' : 2
        }
        return((diction[pos[1]],diction[pos[0]]))
        
    def pawn_moves(self,pos):
        #Convert position
        curr = self.pos_converter(pos)
        legals = []
        
        oneupped = self.oneUp(curr)
        if self.pieces[oneupped] == 0:
            legals.append(oneupped)
            
        twoupped = self.twoUp(curr)
        if self.pieces[twoupped] == 0 and curr[0] == 8:
            legals.append(twoupped)
            
        upright = self.oneUp(self.right(curr))
        if -10 < self.pieces[upright] < 0:
            legals.append(upright)
            
        upleft = self.oneUp(self.left(curr))
        if -10 < self.pieces[upleft] < 0:
            legals.append(upleft)
            
        return legals
    
    @staticmethod
    def knight_moves(pos):
        pass
    @staticmethod
    def bishop_moves(pos):
        pass
    @staticmethod
    def rook_moves(pos):
        pass
    @staticmethod
    def queen_moves(pos):
        pass
    @staticmethod
    def king_moves(pos):
        pass
    @staticmethod
    def oneUp(tup):
        return(tup[0]-1,tup[1])
    def twoUp(self,tup):
        return(self.oneUp(self.oneUp(tup)))
    @staticmethod
    def left(tup):
        return(tup[0],tup[1]-1)
    @staticmethod
    def right(tup):
        return(tup[0],tup[1]+1)
    @staticmethod
    def down(tup):
        return(tup[0]+1,tup[1])
    @staticmethod
    def turn_index(turnstring):
        if turnstring == "W":
            return 1
        return 0
    def update_pos(self,move):
        desired = self.pos_converter(move.desired())
        current = self.pos_converter(move.current())
        self.pieces[desired] = self.pieces[current]
        self.pieces[current] = 0
        for p in self.piece_list[self.turn_index(self.turn)]:
            if p.position == move.desired():
                p = 0
            if p.position == move.current():
                p.position = move.desired()
        return
        
        
        
    def push(self,move):
        #move is a move object.
        if self.turn == "B":
            self.flip_board()
            move = self.flip_move(move)
        #Check1: is this in the set of pseudo-legal moves? Fast-check.
        self.pseudo_legal_moves()
        if move in self.pseudo_legal_moves:
            print("ue")
            if self.turn == "B":
                move = self.flip_move(move)
                self.flip_board()
            self.update_pos(move)
            return
        raise Exception("Move is not legal.")
        return
    
    def helper(self,startpos,direction,result):
        if self.pieces[direction(startpos)] != 0:
            return(result)
        else:
            return(self.helper(self,direction(startpos),direction,result.append(direction(startpos))))

    
    
    def piece_list(self):
        return self.castling
        
    def not_over(self):
        return True
    
    def arr_to_letter_list(self):
        diction = {
            1 : '\033[1;32;1m P',
            2 : '\033[1;32;1m H',
            3 : '\033[1;32;1m B',
            4 : '\033[1;32;1m R',
            5 : '\033[1;32;1m Q',
            6 : '\033[1;32;1m K',
            -1 : '\033[1;31;1m P',
            -2 : '\033[1;31;1m H',
            -3 : '\033[1;31;1m B',
            -4 : '\033[1;31;1m R',
            -5 : '\033[1;31;1m Q',
            -6 : '\033[1;31;1m K',
            0 : '\033[1;30;1m o',
            99 : 't',
            -99 : 't2'
            }
        pieces2 = []
        for lister in self.pieces:
            #print([diction[spec] for spec in lister])
            pieces2.append([diction[spec] for spec in lister])
        return pieces2
    
    def display_board(self):
        
        pieces2 = self.arr_to_letter_list()
        
        #Plotting. Get labels on axes
        a1 = ['\033[1;30;1m 8']
        b1 = ['\033[1;30;1m 7']
        c1 = ['\033[1;30;1m 6']
        d1 = ['\033[1;30;1m 5']
        e1 = ['\033[1;30;1m 4']
        f1 = ['\033[1;30;1m 3']
        g1 = ['\033[1;30;1m 2']
        h1 = ['\033[1;30;1m 1']
        frmt = "{:>3}"*9
        
        a1.extend(pieces2[2][2:10])
        b1.extend(pieces2[3][2:10])
        c1.extend(pieces2[4][2:10])
        d1.extend(pieces2[5][2:10])
        e1.extend(pieces2[6][2:10])
        f1.extend(pieces2[7][2:10])
        g1.extend(pieces2[8][2:10])
        h1.extend(pieces2[9][2:10])
        print(frmt.format(*a1))
        print(frmt.format(*b1))
        print(frmt.format(*c1))
        print(frmt.format(*d1))
        print(frmt.format(*e1))
        print(frmt.format(*f1))
        print(frmt.format(*g1))
        print(frmt.format(*h1))
        test = ['\033[1;30;1m -', '\033[1;30;1m a','\033[1;30;1m b',
                '\033[1;30;1m c','\033[1;30;1m d','\033[1;30;1m e',
               '\033[1;30;1m f','\033[1;30;1m g','\033[1;30;1m h']
        print(frmt.format(*test))
        
    @staticmethod
    def init():
        xwhite = [Piece("a2","pawn"),Piece("b2","pawn"),
         Piece("c2","pawn"),Piece("d2","pawn"),
         Piece("e2","pawn"),Piece("f2","pawn"),
         Piece("g2","pawn"),Piece("h2","pawn"),
         Piece("a1","rook"),Piece("b1","knight"),
         Piece("c1","bishop"),Piece("d1","queen"),
         Piece("e1","king"),Piece("f1","bishop"),
         Piece("g1","knight"),Piece("h1","rook")]
        
        xblack =   [Piece("a7","pawn"),Piece("b7","pawn"),
                     Piece("c7","pawn"),Piece("d7","pawn"),
                     Piece("e7","pawn"),Piece("f7","pawn"),
                     Piece("g7","pawn"),Piece("h8","pawn"),
                     Piece("a8","rook"),Piece("b8","knight"),
                     Piece("c8","bishop"),Piece("d8","queen"),
                     Piece("e8","king"),Piece("f8","bishop"),
                     Piece("g8","knight"),Piece("h8","rook")]
        return([xwhite,xblack])

    def array_initializer(self):
        return(np.pad( np.array([[-4, -2, -3, -5, -6, -3, -2, -4],
                         [-1,-1,-1,-1,-1,-1,-1,-1], 
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [1,1,1,1,1,1,1,1],
                         [4,2,3,5,6,3,2,4]]), 
           (2, 2), 
           'constant',
           constant_values=(99)))