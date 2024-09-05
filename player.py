import random

class Player:
    def __init__(self, token, is_current_player=False):
        self.token = token
        self.is_current_player = is_current_player

    def make_move(self, board):
        while True:
            print("Enter move in format x,y")
            player_input = input()
            try:
                x, y = map(int, player_input.split(','))
                square = board[y][x]
                if square == '':
                    board[y][x] = self.token
                    break
                else:
                    raise ValueError


            except (ValueError, IndexError):
                print("Invalid input. Please enter two integers separated by a comma.")



class AI(Player):
    def make_move(self, board):
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            square = board[y][x]
            if square == '':
                board[y][x] = self.token
                break
