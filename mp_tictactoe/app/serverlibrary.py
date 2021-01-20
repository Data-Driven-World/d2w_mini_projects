import sys

####################################
# Merge sort code
####################################
#
# Paste your merge sort code below
#
###################################

def mergesort(array, byfunc=None):
    pass

#################################

marks = ('X', 'O')

######################
# Class Move
######################
# 
# Exercise 3
#
######################

class Move:
    def __init__(self):
        pass

   def __str__(self):
        return f"row: {self.row:}, col: {self.col:}"

####################
# Class Tic Tac Toe
####################
#
# Exercise 4
#
####################

class TicTacToe:
    def __init__(self, board=None, mark='X'):
        if board == None:
            board = [['_', '_', '_'],
                     ['_', '_', '_'],
                     ['_', '_', '_']]
        self.board = board
        self.max_player = 'X'
        self.min_player = 'O'
        self.mark = mark

    def update(self, row, col, mark):
        '''
        This method is to update self.board at position (row, col)
        with the mark.

        Input:
        - row: integer 0 to 2
        - col: integer 0 to 2
        - mark: string, either 'X' or 'O'

        Output:
        - None
        '''
        pass


    def reset(self):
        '''
        This method is to reset the board to the original state.

        Input:
        - None

        Output:
        - None
        '''
        pass
			
    def checkwinning(self):
        '''
        This method is to check who the winner is.
        You should call self.evaluate() here.

        Input:
        - None

        Output:
        returns 
        - the maximizer or the minimizer if there is a winner
        - None if there is no winner.
        '''
        pass

    def evaluate(self, board):
        '''
        This method is to evaluate the state of the board.

        Input:
        - board: a list of list containing the state of the board.

        Output:
        - It returns 10 if the maximizer wins.
        - It returns -10 if the minimzer wins.
        - It returns 0 if there is no winner.
        '''
        pass

    def find_best_move(self, player):
        '''
        This method is to return the best move for the given player.

        Input:
        - player: string, indicates which player we are trying to determine its best move.

        Output:
        - returns the Move object for the best move for this player.
        '''
        best_val = -sys.maxsize if player == self.max_player else sys.maxsize
        best_move = Move()
        pass

        return best_move

    def minimax(self, board, depth, is_max_player):
        '''
        This method is to implement the minimax algorithm.

        Input:
        - board: a list of list indicating the state of the board.
        - depth: integer indicating the depth of the tree.
        - is_max_player: boolean indicating whether the current node is a maximizer or not.

        Output:
        - integer, returns the score at the current depth.
        '''
        pass

    def any_moves_left(self):
        '''
        This method is to check if there is any other possible moves left.

        Input:
        - None

        Output:
        - returns True if there is an empty cell not yet occupied.
        - Otherwise, return False.
        '''
        pass

if __name__ == "__main__":
    # board = [['x', '_', 'o'],
    #          ['_', 'x', 'o'],
    #          ['_', '_', 'x']]

    # board = [['x', '_', 'o'],
    #          ['_', 'o', 'o'],
    #          ['o', 'x', 'x']]

    # board = [['x', 'x', 'x'],
    #          ['_', 'o', 'o'],
    #          ['_', 'o', 'x']]

    # board = [['x', 'x', 'o'],
    #          ['_', 'o', 'o'],
    #          ['_', 'x', 'o']]

    # board = [['x', 'o', 'x'],
    #          ['o', 'o', 'x'],
    #          ['_', '_', '_']]

    # board = [['x', 'o', '_'],
    #          ['o', 'x', 'o'],
    #          ['_', 'x', '_']]

    board = [['X', 'O', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]
    t = TicTacToe(board)
    #best_move = t.find_best_move('X')
    print(t.checkwinning())
    #print(best_move)

                
