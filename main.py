import random
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap
import sys

from PyQt6.QtWidgets import QDialog, QApplication

from mainWin import Ui_MainWindow

from functools import partial


class Player:
    def __init__(self):
        self.score = 0
        self.hand = []
        self.pickups = []


class Game:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
    
        self.ui.hand = [self.ui.hand00,
                         self.ui.hand01,
                         self.ui.hand02,
                         self.ui.hand03,
                         self.ui.hand04,
                         self.ui.hand05,
                         self.ui.hand06,
                         self.ui.hand07,
                         self.ui.hand08,
                         self.ui.hand09,]

        # timers for adding delay to placing the cards
        timer1 = QtCore.QTimer()
        timer1.setSingleShot(True)
        timer1.timeout.connect(lambda: self.do_place(self.cards[0][0], self.cards[0][1]))
        timer2 = QtCore.QTimer()
        timer2.setSingleShot(True)
        timer2.timeout.connect(lambda: self.do_place(self.cards[1][0], self.cards[1][1]))
        timer3 = QtCore.QTimer()
        timer3.setSingleShot(True)
        timer3.timeout.connect(lambda: self.do_place(self.cards[2][0], self.cards[2][1]))
        timer4 = QtCore.QTimer()
        timer4.setSingleShot(True)
        timer4.timeout.connect(lambda: self.do_place(self.cards[3][0], self.cards[3][1]))
        timer5 = QtCore.QTimer()
        timer5.setSingleShot(True)
        timer5.timeout.connect(self.reenable_hand)
        timer6 = QtCore.QTimer()
        timer6.setSingleShot(True)
        timer6.timeout.connect(self.end_round)
        self.timers = [timer1, timer2, timer3, timer4, timer5, timer6]


        self.ui.table = [[self.ui.table00, self.ui.table01, self.ui.table02, self.ui.table03, self.ui.table04, self.ui.table05],
                         [self.ui.table10, self.ui.table11, self.ui.table12, self.ui.table13, self.ui.table14, self.ui.table15],
                         [self.ui.table20, self.ui.table21, self.ui.table22, self.ui.table23, self.ui.table24, self.ui.table25],
                         [self.ui.table30, self.ui.table31, self.ui.table32, self.ui.table33, self.ui.table34, self.ui.table35]]

        self.ui.scores = [self.ui.p1_score, self.ui.p2_score, self.ui.p3_score, self.ui.p4_score]
        self.ui.played = [self.ui.p1_played, self.ui.p2_played, self.ui.p3_played, self.ui.p4_played]
        self.ui.pickups = [self.ui.p1_pickup, self.ui.p2_pickup, self.ui.p3_pickup, self.ui.pr_pickup]
        
        # creating the players array
        self.players = [Player(), Player(), Player(), Player()]

        for i, widget in enumerate(self.ui.hand):
            widget.clicked.connect(partial(self.place_cards, i))

        for played in self.ui.played:
            played.setPixmap(QPixmap('cards/blank.png'))


        self.reset()

    def reset(self):
        # creating the deck
        deck = list(range(1, 105))
        random.shuffle(deck)

        
        # creating the initial state of the table
        self.table = []
        for _ in range(4):
            self.table.append([deck.pop()])


        # dealing the cards
        for _ in range(10):
            for player in self.players:
                player.hand.append(deck.pop())

        # clearing the pickups
        for player in self.players:
            player.pickups = []

        # resetting the score when the game is over
        if self.is_game_over():
            for player in self.players:
                player.score = 0

        # reenable hand
        self.reenable_hand()

        self.update_display()

    def is_game_over(self):
        # true if any player has a score >= 66
        return any(player.score >= 66 for player in self.players)

    def get_bullheads(self, card):
        if card == 55:
            return 7
        elif card % 11 == 0:
            return 5
        elif card % 10 == 0:
            return 3
        elif card % 5 == 0:
            return 2
        else:
            return 1

    def update_display(self):
        # clear everything
        for widget in self.ui.hand:
            widget.setStyleSheet('background-image: url(cards/blank.png)')
        for row in self.ui.table:
            for i, widget in enumerate(row):
                if i == 5:
                    widget.setStyleSheet('background-image: url(cards/blank_red.png)')
                else:
                    widget.setStyleSheet('background-image: url(cards/blank.png)')
                    

        # update player hand
        for card, widget in zip(self.players[0].hand, self.ui.hand):
            widget.setStyleSheet(f'background-image: url(cards/{card}.png)')

        # update table
        for table_row, row  in zip(self.table, self.ui.table):
            for card, widget in zip(table_row, row):
                widget.setStyleSheet(f'background-image: url(cards/{card}.png)')

        # update scores
        for player, widget in zip(self.players, self.ui.scores):
            widget.setText(str(player.score))

        # update pickups
        for player, widget in zip(self.players, self.ui.pickups):
            if len(player.pickups) > 0:
                widget.setPixmap(QPixmap(f'cards/{player.pickups[-1]}.png'))
            else:
                widget.setPixmap(QPixmap('cards/blank.png'))

    def place_cards(self, player_card_i):

        # add the player's card
        self.cards = [[self.players[0].hand[player_card_i], 0]]

        # remove the card from the player's hand
        self.players[0].hand.pop(player_card_i)

        # add the computer's cards
        for i in range(1, 4):
            # cards.append([self.cpu_turn(i), i])
            self.cards.append([self.players[i].hand[-1], i])

        # move the cards to the played section
        for (card, _), widget in zip(self.cards, self.ui.played):
            widget.setPixmap(QPixmap(f'cards/{card}.png'))

        # sort the cards by value
        self.cards.sort(key=lambda x: x[0])

        # disable the hand
        for widget in self.ui.hand:
            widget.setEnabled(False)


        # update the display
        self.update_display()

        # place the cards with delay
        self.timers[0].start(1500)
        self.timers[1].start(3000)
        self.timers[2].start(4500)
        self.timers[3].start(6000)

        # reenable the hand after the cards have been placed
        self.timers[4].start(6000)

        if len(self.players[0].hand) == 0:
            self.timers[5].start(7000)

    def reenable_hand(self):
        for i in range(len(self.players[0].hand)):
            self.ui.hand[i].setEnabled(True)

    def cpu_turn(self, player_turn):
        # get the player
        player = self.players[player_turn]
        
        # find the card with the lowest difference between itself and the table
        min_score = float('inf')
        card = player.hand[0]
        for c in player.hand:
            min_delta = float('inf')
            for row in self.table:
                
                if len(row) == 5:
                    continue

                delta = c - row[-1]
                if 0 < delta < min_delta:
                    min_delta = delta

            if min_score < min_delta:
                min_score = min_delta
                card = c

        return card

    def do_place(self, card, player_turn):
        # get the player
        player = self.players[player_turn]

        # remove the card from the played section
        self.ui.played[player_turn].setPixmap(QPixmap('cards/blank.png'))

        # remove the card from the player's hand
        if player_turn != 0:
            player.hand.remove(card)


        # find the row that the card goes on
        min_score = float('inf')
        for i, r in enumerate(self.table):
            score = card - r[-1]
            if 0 < score < min_score:
                min_score = score
                row = i

        # if there is no row the card goes on
        if min_score == float('inf'):
            if player_turn == 0:
                row = 0
            else:
                row = self.cpu_choose_row()
            
            self.choose_row(row, player_turn)
  
        # add the card to the end of the row
        self.table[row].append(card)

        #if the row is about to overflow
        if len(self.table[row]) == 6:
            self.row_overflow(row, player_turn)

        # update the display
        self.update_display()

    def choose_row(self, row, player_turn):
        # get the player
        player = self.players[player_turn]
        
        # add the cards in the row to the player's pickups
        for card in self.table[row]:
            player.pickups.append(card)
        
        #clear the row
        self.table[row] = []

    def cpu_choose_row(self):
        # find the row with the lowest bullheads
        min_score = float('inf')
        row = 0
        for i, r in enumerate(self.table):
            score = sum([self.get_bullheads(c) for c in r])
            if score < min_score:
                min_score = score
                row = i
        return row

    def row_overflow(self, row, player_turn):
        # get the player
        player = self.players[player_turn]
        
        # add the cards in the row to the player's pickups
        for card in self.table[row][:-1]:
            player.pickups.append(card)
            
        # clear the row
        self.table[row] = [self.table[row][-1]]

    def end_round(self):
        # end of round
        self.score_pickups()
        if self.is_game_over():
            self.display_win()
        else:
            self.reset()

    def score_pickups(self):
        # sum the pickusp into the player's score
        for player in self.players:
            for pickup in player.pickups:
                player.score += self.get_bullheads(pickup)
        
    def display_win(self):
        min_score = float('inf')
        winner = 0
        for i, player in enumerate(self.players):
            if player.score < min_score:
                min_score = player.score
                winner = i
        print('player ' + str(winner) + ' wins')
        
        
        self.update_display()

if __name__ == "__main__":
    game = Game()
    game.main_window.show()
    sys.exit(game.app.exec())