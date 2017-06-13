from __future__ import print_function
from IPYTHON.display import clear_output

def display_board(board):
	clear_output()
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')


def player_input():
	marker=''
	while not (marker == 'X' or marker == 'O'):
		marker=input('Player 1:Do you want to be X or O').upper()
	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')


def place_marker(board,marker,position):
	board[position]=marker

def win_check(board,mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or
		(board[4] == mark and board[5] == mark and board[6] == mark) or
		(board[1] == mark and board[2] == mark and board[3] == mark) or
		(board[7] == mark and board[4] == mark and board[1] ==mark) or
		(board[8] == mark and board[5] == mark and board[2] == mark) or
		(board[9] == mark and board[6] == mark and board[3] == mark) or
		(board[7] == mark and board[5] == mark and board[3] == mark) or
		(board[9] == mark and board[5] == mark and board[1] == mark))

import random
def choose_first():
	if random.randint(0,1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'


def space_check(board,position):
	return board[position] == ' '

def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True


def player_choice(board):
	position=' '
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
		position=input('choose your next position:(1-9)')
	return int(position)

def replay():
	return input('do you want to play again? Enter Yes or No:').lower().startswitch('y')


print('Welcome to Tic Tac Toe!')
while True:
	theBoard=[' ']*10
	player1_marker,player2_marker = player_input()
	turn=choose_first()
	print(turn + 'will go first.')
	game_on=True

	while game_on:
		if turn == 'Player 1':


			display_board(theBoard)
			position=player_choice(theBoard)
			place_marker(theBoard,player1_marker,position)

			if win_check(theBoard,player1_marker):
				display_board(theBoard)
				print('congratulations you have win the game')
				game_on=False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('the game is a draw')
					break
				else:
					turn='Player 2'
			
		else:
			display_board(theBoard)
			position=player_choice(theBoard)
			player1_marker(theBoard,player2_marker,position)

			if win_check(theBoard,player2_marker):
				display_board(theBoard)
				print('Player 2 has won')
				game_on=False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('the game is a tie')
					break
				else:
					turn='Player 1'
	if not replay():
		break


	