from itertools import combinations
from random import choice
from player import Player
from player import AI

STARTING_BOARD = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
TOKENS = ['O', 'X']

class TicTacToe:
    def __init__(self, player_count=1):
        self.running = False
        self.board = STARTING_BOARD
        player_1 = Player(token=choice(TOKENS))
        player_2_token = TOKENS[1] if player_1.token == TOKENS[0] else TOKENS[0]
        player_2 = AI(token=player_2_token) if player_count == 1 else Player(token=player_2_token)
        self.players = [player_1, player_2]
        first_to_play = choice(self.players)
        first_to_play.is_current_player = True

    def run(self):
        self.running = True
        self.draw_grid()
        while self.running:
            for player in self.players:
                print(f"Player {player.token}'s turn...")
                player.make_move(self.board)
                self.draw_grid()
                if self.is_game_over():
                    self.running = False
                    break


    def is_game_over(self):
        magic_square = [
            [8, 1 ,6],
            [3, 5, 7],
            [4, 9, 2],
        ]
        for player in self.players:
            current_player_token = player.token
            values = []
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == current_player_token:
                        values.append(magic_square[i][j])

            for p in combinations(values, r=3):
                if sum(p) == 15:
                    print(f"Game over, {current_player_token} wins!")
                    return True

        return False

    def draw_grid(self):
        grid = [
            [' ', '|', ' ', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', ' ', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', ' ', '|', ' '],
        ]
        # map board to visual grid
        for x in range(3):
            for y in range(3):
                square = self.board[y][x]
                if square != '':
                    grid[y*2][x*2] = square
        # output grid to console
        for row in grid.__reversed__():
            print(*row)
        print('\n')
