import random
import chess
import time
import random

def set_board(board: chess.Board, board_position:str):
    board.set_fen(board_position)

def main():

    board = chess.Board()

    while True:
        opponent_move = input()
        time.sleep(random.randrange(1,10)/100)
        if opponent_move.startswith("BOARD: "):
            set_board(board, opponent_move.removeprefix("BOARD: "))
        elif opponent_move.startswith("MOVE: "):
            board.push_uci(opponent_move.removeprefix("MOVE: "))
            legal_moves = [move.uci() for move in list(board.legal_moves)]
            choice = random.choice(legal_moves)
            board.push_uci(choice)
            # example about logs
            print(f"I moved {choice}\n")
            # example about posting a move
            print(f"MOVE: {choice}\n")   

if __name__ == "__main__":
    main()
