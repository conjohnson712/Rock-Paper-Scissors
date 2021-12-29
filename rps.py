#!/usr/bin/env python3
import random
import enum
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
"""The Player class is the parent class for all of the Players
in this game"""

class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Rock, Paper, Scissors? > ").lower()
            if choice in self.moves:
                return choice
            print("Invalid Choice. Try Again :)")


class ReflectPlayer(Player):
    def move(self):
        if round == [0]:
            return random.choice(self.moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        self.their_move = random.choice(self.moves)
        if self.their_move == "rock".lower():
            return "paper"
        elif self.their_move == "paper".lower():
            return "scissors"
        elif self.their_move == "scissors".lower():
            return "rock"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player_score = 0
        self.CPU_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player: {move1}  CPU: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if (move1 == move2):
            print("It's a tie! No Winner This Round!")
        elif beats(move1, move2) is True:
            print("The Player Wins This Round!")
            self.player_score += 1
        elif beats(move2, move1) is True:
            print("The CPU Wins This Round!")
            self.CPU_score += 1

        print("Player: " + str(self.player_score) + " " +
              " CPU: " + str(self.CPU_score))

    def play_game(self):
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        if self.player_score > self.CPU_score:
            print("The Player Wins!")
        elif self.player_score < self.CPU_score:
            print("The CPU Wins!")
        elif self.player_score == self.CPU_score:
            print("Tie Game!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice([Player(), RandomPlayer(),
                                             ReflectPlayer(), CyclePlayer()]))
    game.play_game()
