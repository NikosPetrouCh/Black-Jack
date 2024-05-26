import random


class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"
    # return self.rank["rank"] + " of " + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "hearts", "diamonds", "clubs"]
        # ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

        ranks = [{"rank": "A", "value": 11},
                 {"rank": "2", "value": 2},
                 {"rank": "3", "value": 3},
                 {"rank": "4", "value": 4},
                 {"rank": "5", "value": 5},
                 {"rank": "6", "value": 6},
                 {"rank": "7", "value": 7},
                 {"rank": "8", "value": 8},
                 {"rank": "9", "value": 9},
                 {"rank": "10", "value": 10},
                 {"rank": "J", "value": 10},
                 {"rank": "Q", "value": 10},
                 {"rank": "K", "value": 10},
                 ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit, rank))

    def My_Shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


class Hand:
    def __init__(self, dealer=False):
        self.cards_on_hand = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards_on_hand.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards_on_hand:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealers_card=False):
        print(f"""{"Dealer's" if self.dealer else "Your"} hand: """)
        for index, card in enumerate(self.cards_on_hand):
            if index == 0 and self.dealer \
                    and not show_all_dealers_card and not self.is_blackjack():
                print("hidden")
            else:
                print(card)

        # for card in self.cards_on_hand:
        #   print(card)
        if not self.dealer:
            print("Value: ", self.get_value())
        print()


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        games_to_play = int(input("How many games do you want to play? "))

        while games_to_play <= 0:
            try:
                print("How many games do you want to play? ")
            except:
                print("You have to enter a number")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.My_Shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 10)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 10)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""

            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S): ").lower()
                    print()
                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealers_card=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("your hand", player_hand_value)
            print("dealer's hand", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("Dealer wins!")
                return True
            elif dealer_hand.get_value() > 21:
                print("You win!")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Tie!")
                return True
            elif player_hand.is_blackjack():
                print("You win!")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer wins!")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            elif player_hand.get_value() < dealer_hand.get_value():
                print("Dealer wins!")
            else:  # player_hand.hand_value() == dealer_hand.hand_value():
                print("Tie!")
            return True
        return False


first_try = Game()
first_try.play()

# Deck1 = Deck()
# Deck1.My_Shuffle()

# hand1 = Hand()
# hand1.add_card(Deck1.deal(3))
# print (hand1.cards[1], hand1.cards[0])
# hand1.display()


# hand1.get_value()
# Card = card("hearts", {"rank":"A", "value": 11})
# print(Card)
# deck1 = Deck()
# deck2 = Deck()
# deck1.My_Shuffle()
# print (deck2.cards)
# print (deck1.cards)

# My_Shuffle()
# card = deal(1)[0]
# print (card[1]["value"])

# cards_dealt = deal(1)
# card = deal(4)
# rank = card[1]
# print (card)

# if rank == "A":
#   value = 11
# elif rank == "J" or rank == "Q" or rank == "K":
#   value = 10
# else:
#   value = rank
# rank_dict = {"rank": rank, "value": value}

# print(rank_dict["rank"], rank_dict["value"])

# print("Your card is:" + rank + " of " + suit)