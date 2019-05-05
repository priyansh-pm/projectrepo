import os
import random
from copy import deepcopy
from tkinter import *
playerWins = 0
artificialIntelligenceWins = 0
drawGames = 0

class TicTacToe(object):

    def __init__(self):
        self.list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.playerName = ""
        self.playerSymbol = ""
        self.artificialIntelligenceSymbol = ""
        self.choosed_boxes = []

    def set_player_name(self):
        self.playerName = input("Enter player name here : ")

    def set_player_symbol(self):
        self.playerSymbol = ""
        while self.playerSymbol != 'o' and self.playerSymbol != 'x':
            self.playerSymbol = input("Enter o or x : ")
        if self.playerSymbol == 'o':
            self.artificialIntelligenceSymbol = 'x'
        else:
            self.artificialIntelligenceSymbol = 'o'

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def check_for_winner(self, list, symbol, i, j):
        col = list[i][0] == symbol and list[i][
            1] == symbol and list[i][2] == symbol
        row = list[0][j] == symbol and list[1][
            j] == symbol and list[2][j] == symbol
        diagonals = list[1][1] == symbol and ((list[0][0] == symbol and list[2][
            2] == symbol) or (list[0][2] == symbol and list[2][0] == symbol))
        if col or row or diagonals:
            return True
        else:
            return False

    def table(self):
        print("                        ", "        |        |        ")
        print("                      ", "    ", self.list[0][
              0], "   |  ", self.list[0][1], "   |  ", self.list[0][2], "   ")
        print("                        ", "        |        |        ")
        print("                        ", "--------|--------|--------")
        print("                        ", "        |        |        ")
        print("                      ", "    ", self.list[1][
              0], "   |  ", self.list[1][1], "   |  ", self.list[1][2], "   ")
        print("                        ", "        |        |        ")
        print("                        ", "--------|--------|--------")
        print("                        ", "        |        |        ")
        print("                      ", "    ", self.list[2][
              0], "   |  ", self.list[2][1], "   |  ", self.list[2][2], "   ")
        print("                        ", "        |        |        ")

    def get_turn(self, turn):
        if turn:
            return self.playerName
        return "artificialIntelligence"

    def imput_symbol(self, list, number, symbol):
        tempi = 0
        tempj = 0
        number = int(number)
        if number >= 1 and number <= 3:
            list[0][number - 1] = symbol
            tempi = 0
            tempj = number - 1
        elif number >= 4 and number <= 6:
            list[1][number - 4] = symbol
            tempi = 1
            tempj = number - 4
        elif number >= 7 and number <= 9:
            list[2][number - 7] = symbol
            tempi = 2
            tempj = number - 7

        winner = self.check_for_winner(
            list, symbol, tempi, tempj)
        return winner

    def play(self):
        self.set_player_symbol()
        winner = False
        turn = False

        for i in range(0, 9):
            if (turn):
                if winner:
                    break
                self.clear_screen()
                self.table()
                if self.simulatorAIWin():
                    winner = True
                if self.simulatorAIBlock():
                    pass
                else:
                    number = random.randint(1, 9)
                    while number in self.choosed_boxes:
                        number = random.randint(1, 9)
                    self.choosed_boxes.append(number)
                    winner = self.imput_symbol(self.list,
                                               number, self.artificialIntelligenceSymbol)
                turn = False

            else:
                if winner:
                    break
                self.clear_screen()
                self.table()
                isGoodNumber = False
                while not isGoodNumber:
                    number = input(
                        self.playerName + " enter number you are with " + self.playerSymbol + ": ")
                    number = int(number)
                    if(number > 0 and number < 10 and number not in self.choosed_boxes):
                        isGoodNumber = True
                self.choosed_boxes.append(number)
                winner = self.imput_symbol(
                    self.list,  number, self.playerSymbol)
                turn = True
            if winner:
                self.clear_screen()
                self.table()
                print("Winner is ", self.get_turn(turn), "!!!")
                if self.get_turn(turn) == self.playerName:
                    global playerWins
                    playerWins += 1
                else:
                    global artificialIntelligenceWins
                    artificialIntelligenceWins += 1

        if not winner:
            self.clear_screen()
            self.table()
            print("Draw game !!!")
            global drawGames
            drawGames += 1

        print(self.playerName, " wins: ", playerWins)
        print("artificialIntelligence wins: ", artificialIntelligenceWins)
        print("Draw Games: ", drawGames)
        self.list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.choosed_boxes = []

    def simulatorAIWin(self):
        simulateTable = deepcopy(self.list)
        for i in range(1, 10):
            if i not in self.choosed_boxes:
                if self.imput_symbol(simulateTable, i, self.artificialIntelligenceSymbol):
                    self.imput_symbol(
                        self.list, i, self.artificialIntelligenceSymbol)
                    self.choosed_boxes.append(i)
                    return True
            print(simulateTable)
            print(self.list)
            simulateTable = deepcopy(self.list)
        return False

    def simulatorAIBlock(self):
        simulateTable = deepcopy(self.list)
        for i in range(1, 10):
            if i not in self.choosed_boxes:
                if self.imput_symbol(simulateTable, i, self.playerSymbol):
                    self.imput_symbol(
                        self.list, i, self.artificialIntelligenceSymbol)
                    self.choosed_boxes.append(i)
                    return True
            print(simulateTable)
            print(self.list)
            simulateTable = deepcopy(self.list)
        return False


def main():

    root = Tk()
    button1 = Button(text="X this out")

    button1.pack()
    root.mainloop()
    
    game = TicTacToe()
    game.set_player_name()
    game.play()
    retry = input("Do you want to play again y/n: ")
    while retry == 'y':
        game.play()
        retry = input("Do you want to play again y/n: ")
    print("Thanks for playing !!!")

if __name__ == '__main__':
    main()
