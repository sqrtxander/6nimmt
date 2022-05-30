import random
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap
import sys
from functools import partial

from PyQt6.QtWidgets import QApplication

from mainWin import Ui_MainWindow
from rules import Rules
from outcome import Outcome
from settings import Settings


class Player:
    def __init__(self, name, link, pick, win):
        self.score = 0
        self.hand = []
        self.pickups = []
        self.name = name
        self.link = link
        self.pick = pick
        self.win = win


class Game:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.main_window.setFixedSize(self.main_window.width(), self.main_window.height())

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

        self.ui.table = [[self.ui.table00, self.ui.table01, self.ui.table02, self.ui.table03, self.ui.table04, self.ui.table05],
                         [self.ui.table10, self.ui.table11, self.ui.table12, self.ui.table13, self.ui.table14, self.ui.table15],
                         [self.ui.table20, self.ui.table21, self.ui.table22, self.ui.table23, self.ui.table24, self.ui.table25],
                         [self.ui.table30, self.ui.table31, self.ui.table32, self.ui.table33, self.ui.table34, self.ui.table35]]

        self.ui.scores = [self.ui.p1_score, self.ui.p2_score, self.ui.p3_score, self.ui.p4_score]
        self.ui.played = [self.ui.p1_played, self.ui.p2_played, self.ui.p3_played, self.ui.p4_played]
        self.ui.pickups = [self.ui.p1_pickup, self.ui.p2_pickup, self.ui.p3_pickup, self.ui.pr_pickup]
        
        # creating the players array
        self.players = [Player('You', 'are', 'pick', 'win'), Player('Player 2', 'is', 'picks', 'wins'),
                        Player('Player 3', 'is', 'picks', 'wins'), Player('Player 4', 'is', 'picks', 'wins')]

        for i, widget in enumerate(self.ui.hand):
            widget.clicked.connect(partial(self.place_cards, i))

        for played in self.ui.played:
            played.setPixmap(QPixmap('cards/blank.png'))

        # self.ui.hand[-1].clicked.connect(self.display_win)

        for i, row in enumerate(self.ui.table):
            for widget in row:
                widget.clicked.connect(partial(self.choose_row, i, 0, None))

        # self.ui.setWindowIcon(QIcon('background/icon.png'))

        self.ui.play_btn.clicked.connect(self.hide_menu)
        self.ui.exit_btn.clicked.connect(self.close)

        self.ui.menu_image.setPixmap(QPixmap('background/icon.png'))

        self.ui.current_lbl.setText('Pick a card')

        self.delay_time = 2000
        self.points_required = 66

        self.outcome = Outcome(self)
        self.rules = Rules()
        self.settings = Settings(self)
        
        self.ui.rules_button.clicked.connect(self.rules.window.show)
        self.ui.settings_button.clicked.connect(self.settings.window.show)

        self.reset()

    def hide_menu(self):
        self.ui.play_btn.hide()
        self.ui.exit_btn.hide()
        self.ui.menu_cover.hide()
        self.ui.menu_image.hide()
        self.ui.menu_text.hide()

        self.app.setStyleSheet('''
    QMainWindow {
        background-image: url(background/felt.png); 
        background-position: center;
        }
        ''')

    def close(self):
        self.main_window.close()
        self.app.quit()


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
        self.enable_hand()

        self.set_table_state(False)
        self.ui.current_lbl.setText('Pick a card')
        self.update_display()

    def is_game_over(self):
        # true if any player has a score >= the required points to end the game
        return any(player.score >= self.points_required for player in self.players)

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
            self.cards.append([self.cpu_turn(i), i])

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

        self.call_next_place()

    def enable_hand(self):
        for i in range(len(self.players[0].hand)):
            self.ui.hand[i].setEnabled(True)
    
    def set_table_state(self, state):
        for row in self.ui.table:
            for widget in row:
                widget.setEnabled(state)

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

    def do_place1(self, card, player_turn):
        # get the player
        player = self.players[player_turn]

        # update the helpful label
        self.ui.current_lbl.setText(f'{player.name} {player.link} placing {card}')

        # remove the card from the player's hand
        if player_turn != 0:
            player.hand.remove(card)


        # find the row that the card goes on
        min_score = float('inf')
        row = None
        for i, r in enumerate(self.table):
            score = card - r[-1]
            if 0 < score < min_score:
                min_score = score
                row = i

        if player_turn == 0 and row == None:
            self.ui.current_lbl.setText(f'You need to choose a row')
            self.set_table_state(True)
            return

        QtCore.QTimer.singleShot(self.delay_time, lambda: self.do_place2(min_score, row, card, player_turn))

    def do_place2(self, min_score, row, card, player_turn):
        
        # get the player
        player = self.players[player_turn]

        # if there is no row the card goes on
        if min_score == float('inf'):
            if player_turn != 0:
                row = self.cpu_choose_row()
                self.ui.current_lbl.setText(f'{player.name} {player.link} choosing a row')
                QtCore.QTimer.singleShot(self.delay_time, lambda: self.choose_row(row, player_turn, card))
            return 

        # remove the card from the played section
        self.ui.played[player_turn].setPixmap(QPixmap('cards/blank.png'))

        # add the card to the end of the row
        self.table[row].append(card)

        # update the display
        self.update_display()

        #if the row is about to overflow
        if len(self.table[row]) == 6:
            QtCore.QTimer.singleShot(self.delay_time, lambda: self.row_overflow(row, player_turn))
            return

        # place next card with delay
        self.call_next_place()

    def choose_row(self, row, player_turn, placed_card=None):
        # get the player
        player = self.players[player_turn]

        if placed_card == None:
            placed_card = self.placed_card

        self.ui.current_lbl.setText(f'{player.name} chose row {row + 1}')

        # add the cards in the row to the player's pickups
        for card in self.table[row]:
            player.pickups.append(card)
        
        #clear the row
        self.table[row] = []

        # remove the card from the played section
        self.ui.played[player_turn].setPixmap(QPixmap('cards/blank.png'))

        # add the card to the end of the row
        self.table[row].append(placed_card)

        # update the display
        self.update_display()

        # disable the table
        self.set_table_state(False)

        # place next card with delay
        QtCore.QTimer.singleShot(self.delay_time, self.call_next_place)

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

    def call_next_place(self):
        # if turn is over
        if len(self.cards) == 0:
            self.enable_hand()
            # if round is over
            if len(self.players[0].hand) == 0:
                self.ui.current_lbl.setText('Round over')
                QtCore.QTimer.singleShot(self.delay_time, self.end_round)
            else:
                self.ui.current_lbl.setText('Pick a card')
            return

        self.placed_card, turn = self.cards.pop(0)
        self.update_display()
        self.do_place1(self.placed_card, turn)

    def row_overflow(self, row, player_turn):
        # get the player
        player = self.players[player_turn]
        
        # update helpful label
        self.ui.current_lbl.setText(f'{player.name} {player.pick} up row {row + 1}')
 
        # add the cards in the row to the player's pickups
        for card in self.table[row][:-1]:
            player.pickups.append(card)
            
        # clear the row except for the placed card
        self.table[row] = [self.table[row][-1]]

        # update the display
        self.update_display()

        # place the next card with delay
        QtCore.QTimer.singleShot(self.delay_time, self.call_next_place)

    def end_round(self):
        # end of round
        self.score_pickups()
        if self.is_game_over():
            self.display_win()
        else:
            self.reset()

    def score_pickups(self):
        # sum the pickups into the player's score
        for player in self.players:
            for pickup in player.pickups:
                player.score += self.get_bullheads(pickup)
        
    def display_win(self):
        min_score = float('inf')
        winners = []

        for player in self.players:
            if player.score < min_score:
                min_score = player.score
                winners = [player]
            elif player.score == min_score:
                winners.append(player)
        

        self.outcome.window.show()
        self.outcome.show_win(winners)     
        self.update_display()

if __name__ == "__main__":
    game = Game()
    game.main_window.show()
    sys.exit(game.app.exec())