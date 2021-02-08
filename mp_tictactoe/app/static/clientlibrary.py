from org.transcrypt.stubs.browser import *


def update_computer(row, col, player):
    '''
    Write your code here to construct the cell id,
    and get the computer's mark.

    Input:
    - row: int, 0 to 2
    - col: int, 0 to 2
    - player: str, either 'X' or 'O'

    Replace the None with your code.

    The cell id is in the following format: cellxy
    - where x is the row, and y is the column
    - x and y values are from 0 to 2

    For example, the cell in the middle of the Tic Tac Toe grid
    is given by 'cell11'.
    '''

    computer = None
    cell_id = None
    console.log(cell_id)
    document.getElementById(cell_id).innerText = computer

def winning(player, winner):
    '''
    If the winner is the same mark as the player, 
    then the player wins, otherwise, the player loses.

    Use document.getElemntById().innerText = "sometext"

    The HTML id is "winner".

    Write your code here. 
    '''
    pass

def click_cell(username, row, col, mark):
    '''
    Replace None to create the cell id string. e.g. 'cell11'
    from the row and the column index.

    This function will call 'clicked' event in the server.

    Update the TicTacToe grid cell with the mark. 

    '''
    cellid = None
    document.getElementById(None).innerText = None 
    socket.emit('clicked', {'username': username, 'id': cellid, 'mark': mark})

