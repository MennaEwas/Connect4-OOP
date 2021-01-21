"""
Mennatullah Abdelrahman 
120180009
Assignment 1 
Problem 2
Connect4
CSE 312
Date : 12/6/2020
The game will ended once one of the players got win and the winner is the last player as I put it as an error so the window will close.
""" 
from itertools import groupby, chain
EMP = '.'
Star = '*'
Ring = 'O'

def positive_dig(mx, col, row): #diagonal from left bottom to right top and it takes the grid, col and row
    forming = [[(c, r - c) for c in range(col)] for r in range(col + row - 1)]
    for dig in (forming): 
        yield [mx[r][c] for r, c in dig if r >= 0 and c >= 0 and r < col and c < row] #yield is better than return because the variables will still with its own values

def negative_dig(mx, col, row): #from left top to right bottom
    forming = [[(c, r - col + c + 1) for c in range(col)] for r in range(col + row - 1)]
    for dig in (forming):
        yield [mx[r][c] for r, c in dig if r >= 0 and c >= 0 and r < col and c < row] #same as the positive
''' In the last 2 functions we defined the positive and negative diagonal'''        
class Connect4(object):
    def __init__(self, row = 6, col = 7, minn = 4): #Define our class and all we need in the game.
        self.row = row
        self.col = col
        self.win = minn
        self.board = [[EMP]*row for _ in range(col)]   
    def print_board(self): #method to see our game grid
            print(' '.join(map(str, range(self.col))))
            for y in range(self.row):
                print(' '.join(str(self.board[x][y]) for x in range(self.col)))
            print()
            '''this function is to print the grid while playing'''       

        
    def whowins(self): #new function to identify who is the winner
        gw = self.get_winner() #to import the winner and if it is not empty and there is a player
        if gw:
            self.print_board()
            print (gw + '  is the winner in this game')
            raise Exception (gw + '  is the winner in this game')
                
    def get_winner(self): #get the winner in the current board
        lines = (self.board, 
                 zip(*self.board),
                 positive_dig(self.board, self.col, self.row),
                 negative_dig(self.board, self.col, self.row)
        ) #this is the positive diagonal from outside the class
        for p in chain(*lines): 
            for c, g in groupby(p):
                if c != EMP and len(list(g)) >= self.win:
                    return c
    def play_one(self, column, color):
        #put the color you want in the desired col
            bc = self.board[column]
            if bc[0] != EMP: 
                raise Exception('No place for new inputs') #tell the user there is an error if the col is full
            counter = -1 
            while bc[counter] != EMP: #if it is not full 
                counter -= 1 #decrement the counter by one 
            bc[counter] = color #making an indexed string by colors to help checking the winner
            '''This function is to put the new input or the play '''
            self.whowins() #other method to identify which one is the winner
                    
          
#  The main code to start executing the game
if __name__ == '__main__':
	g = Connect4()
	roundd = Star
while True:
		g.print_board()
		row = input('{}\'s round: '.format('Star' if roundd == Star else 'Ring')) 
		g.play_one(int(row), roundd)
		roundd = Ring if roundd == Star else Star
            
        