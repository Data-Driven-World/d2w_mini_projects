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
        if isinstance(board, str):
            board = self.str_to_board(board)
        self.board = board
        self.max_player = 'X'
        self.min_player = 'O'
        self.mark = mark
        
    ##############
    # Task 1
    ##############
    def reset(self):
        '''
        This method is to reset the board to the original state.
        Set all tile to '_'. 

        Input:
        - None

        Output:
        - None
        '''
        pass

    def str_to_board(self, boardstr):
        '''
        This method is to transform the single string board state into a nested list.

        Input:
       - boardstr: a string of 9 character representing the board

        Output:
        - a nested list representing the state of the board
        '''
        board = []
        for row in range(3):
            rowlist = []
            for col in range(3):
                rowlist.append(boardstr[row * 3 + col])
            board.append(rowlist)
        return board

    #############################################################
    # Your code here for the computed property
    # property name: board_to_str
    # output: a single string representing the state of the board
    #############################################################

    @property
    def board_to_str(self):
        retval = ''
        for row in self.board:
            for col in row:
                retval += col
        return retval
    
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

    #############
    # Task 2
    #############
    def checkwinner(self, cell):
        '''
        This method is to  return who the winner by looking at a cell.
        The method should return 10 if the winner is the maximiser,
        or return -10 if the winner is the minimizer.

        Input:
        - cell: which is one of the cell that forms a winning line

        Output:
        - either 10 (maximizer) or -10 (minimizer)
        '''
        
        pass
    
    ###########
    # Task 3
    ###########
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
        
        for idx in range(3):
            # check for each row and return proper score
            # below is written as an example for you
            # we have predefined 'marks' as a set of 'X' and 'O'
            if (board[idx][0] == board[idx][1] == board[idx][2]) and \
               board[idx][0] in marks:
                return self.checkwinner(board[idx][0])
            
            # check for each col and return proper score
            # write your code below
            pass
        
        # check for the two diagonals for winning pattern
        pass
    
        # if there is no winner, return 0
        return 0
  
    ##########
    # Task 4
    ##########
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
        
        # call evaluate() method to get the score
        score = None
        
        # replace return None when appropriate
        if score == 10:
            return None
        elif score == -10:
            return None
        else:
            return None
        pass
    
    #########
    # Task 5
    #########
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


    ###########
    # Task 6
    ###########
    def find_best_move(self, player):
        '''
        This method is to return the best move for the given player.

        Input:
        - player: string, indicates which player we are trying to determine its best move.

        Output:
        - returns the Move object for the best move for this player.
        '''
        # this is step 1 to initialize best move score
        best_val = -sys.maxsize if player == self.max_player else sys.maxsize
        
        # this is step 2 to initialize best move to NULL
        best_move = Move()
        
        # this is step 3 to check every possible move
        for row in range(3):
            for col in range(3):
                # check if cell is empty
                # write the boolean condition and replace the None
                empty = None
                if empty:
                    # make the move
                    # replace the None
                    self.board[row][col] = None
                    
                    # The next two steps are to compute the evaluation function
                    # first, check if current player is maximizer
                    is_max = None
                    
                    # second, call minimax to get the score
                    # the minimax method has the following arguments:
                    # def minimax(board, depth, is_max_player)
                    # - board is the state of the board
                    # - depth is an integer and indicates the level of the minimax algorithm, set to 0 
                    # - is_max_player is a boolean whether the current player 
                    #   is a maximizer or not
                    # Note: if the current player is a maximizer,
                    #.      => you should call the minimax as a minimizer
                    #.      if the current player is a minimizer,
                    #.      => you should call the minimax as a maximizer
                    move_val = None
                    
                    # undo the move
                    self.board[row][col] = None
                    
                    # check if it is better
                    if (is_max and move_val > best_val) or \
                       ((not is_max) and move_val < best_val):
                        # set the property for the best move
                        best_move.row = None
                        best_move.col = None
                        best_val = None

        return best_move

    ############
    # Task 7
    ############
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
        score = self.evaluate(board)
        # write the boolean condition to check if there is a winner
        any_winner = None
        if any_winner:
            return score

        # write the boolean condition to check if there is no more move
        no_more_move = None
        if no_more_move:
            return 0

        if is_max_player:
            # this is to store the best score so far
            best = -sys.maxsize 
            
            for row in range(3):
                for col in range(3):
                    # if there is a possible move
                    if board[row][col] == '_':
                        # set the board to the maximiser mark
                        board[row][col] = None
                        
                        # compute evaluation function through recursion
                        # ensuring: 
                        # - increase level by 1
                        # - alternate to minimizer
                        score = None
                        
                        # set the best score so far
                        best = None
                        
                        # undo the move
                        board[row][col] = None
            return best
        else:
            # this is the step if it is the minimizer
            # do the same as the above
            # with the following differences:
            # - initial value for the best score will be opposite
            # - set the mark to minimizer when trying the move
            # - change to maximizer when going deeper to the next level
            pass

    
if __name__ == "__main__":
    ########################
    # Exercise 3
    ########################
    #
    # Test Move class
    # 
    # Write your test case to make sure that 
    # the row and col properties accept only index 
    # between 0 and 2
    #
    ########################
    pass

    ########################
    # Exercise 4
    ########################
    #
    # Test TicTacToe class
    # 
    # Comment out sys.exit(1) 
    # to run the test cases
    #
    ########################
    
    sys.exit(1)
    
    board1 = [['X', '_', 'O'],
             ['_', 'X', 'O'],
             ['_', '_', 'X']]

    t = TicTacToe(board1)
    t.reset()
    assert t.board == [['_', '_', '_'],
                       ['_', '_', '_'],
                       ['_', '_', '_']]
    assert t.board_to_str == '_________'
 
    t.update(0, 0, 'X')
    t.update(0, 2, 'O')
    t.update(1, 1, 'X')
    t.update(1, 2, 'O')
    t.update(2, 2, 'X')
    assert t.board == board1
    assert t.board_to_str == 'X_O_XO__X' 

    assert t.checkwinner('X') == 10
    
    assert t.checkwinner('O') == -10

    board2 = [['X', '_', 'O'],
             ['_', 'O', 'O'],
             ['O', 'X', 'X']]

    t = TicTacToe(board2, 'O')
    assert t.evaluate(board2) == -10
    
    board3 = [['X', 'X', 'X'],
             ['_', 'O', 'O'],
             ['_', 'O', 'X']]
    
    assert t.evaluate(board3) == 10

    board4 = [['O', 'X', 'O'],
             ['X', 'O', 'O'],
             ['X', 'O', 'X']]
    
    assert t.evaluate(board4) == 0
    
    t = TicTacToe(board1)
    assert t.checkwinning() == 'X' 
    
    t = TicTacToe(board2)
    assert t.checkwinning() == 'O' 

    t = TicTacToe(board3)
    assert t.checkwinning() == 'X' 
    
    t = TicTacToe(board4)
    assert t.checkwinning() == None
    assert not t.any_moves_left()
    
    board5 = [['X', 'O', 'X'],
             ['O', 'O', 'X'],
             ['_', '_', '_']]

    t = TicTacToe(board5)
    assert t.checkwinning() == None
    assert t.any_moves_left()
    
    
    t = TicTacToe(board5)
    assert str(t.find_best_move('X')) == "row: 2, col: 2"
    assert str(t.find_best_move('O')) == "row: 2, col: 1"

    board6 = [['X', '_', '_'],
              ['O', 'X', 'O'],
              ['_', 'X', 'O']]
    
    t = TicTacToe(board6)
    assert str(t.find_best_move('X')) == "row: 0, col: 1"
    assert str(t.find_best_move('O')) == "row: 0, col: 2"
    
    board7 = [['X', 'O', '_'],
              ['O', 'X', 'O'],
              ['_', 'X', '_']]
    
    t = TicTacToe(board7)
    assert str(t.find_best_move('X')) == "row: 0, col: 2"
    assert str(t.find_best_move('O')) == "row: 2, col: 2"
