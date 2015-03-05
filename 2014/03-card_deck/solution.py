<<<<<<< HEAD
class Base:
    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __str__(self):
        return self.__class__.__name__


class Rank(Base):
    symbol = None   # wtf is this shit

class Suit(Base):
    color = None

class King(Rank):
    symbol = 'K'

class Queen(Rank):
    symbol = 'Q'

class Jack(Rank):
    symbol = 'J'

class Ten(Rank):
    symbol = '10'

class Nine(Rank):
    symbol = '9'

class Eight(Rank):
    symbol = '8'

class Seven(Rank):
    symbol = '7'

class Six(Rank):
    symbol = '6'

class Five(Rank):
    symbol = '5'

class Four(Rank):
    symbol = '4'

class Three(Rank):
    symbol = '3'

class Two(Rank):
    symbol = '2'

class Ace(Rank):
    symbol = 'A'


class Diamonds(Suit):
    color = 'red'

class Hearts(Suit):
    color = 'red'

class Spades(Suit):
    color = 'black'

class Clubs(Suit):
    color = 'black'


RANK_CLASSES = [
    King, Queen, Jack, Ten, Nine, Eight, Seven,
    Six, Five, Four, Three, Two, Ace
]
SUIT_CLASSES = [Diamonds, Hearts, Spades, Clubs]

RANKS = {cls.__name__: cls for cls in RANK_CLASSES}
SUITS = {cls.__name__: cls for cls in SUIT_CLASSES}


class Card:
    def __init__(self, rank, suit):
        self.rank = rank()
        self.suit = suit()

    def __str__(self):
        return str(self.rank) + ' of ' + str(self.suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit


class CardCollection:
    def __init__(self, collection=[]):
        self.__cards = list(collection)

    def draw(self, index):
        return self.__cards.pop(index)

    def draw_from_top(self):
        return self.__cards.pop()

    def draw_from_bottom(self):
        return self.__cards.pop(0)

    def top_card(self):
        return self.__cards[-1]

    def bottom_card(self):
        return self.__cards[0]

    def add(self, card):
        self.__cards.append(card)

    def index(self, card):
        return self.__cards.index(card)

    def __getitem__(self, index):
        return self.__cards[index]

    def __setitem__(self, index, card):
        self.__cards[index] = card

    def __iter__(self):
        for card in self.__cards:
            yield card

    def __len__(self):
        return len(self.__cards)


def AllSuitsDeck(ranks):
    deck = CardCollection()
    for suit in SUIT_CLASSES:
        for rank in ranks:
            deck.add(Card(rank, suit))
    return deck


def StandardDeck():
    return AllSuitsDeck(RANK_CLASSES)


def BeloteDeck():
    unused = [Two, Three, Four, Five, Six]
    return AllSuitsDeck([rank for rank in RANK_CLASSES if rank not in unused])


def SixtySixDeck():
    unused = [Two, Three, Four, Five, Six, Seven, Eight]
    return AllSuitsDeck([rank for rank in RANK_CLASSES if rank not in unused])
=======
from collections import OrderedDict


class Card:
    def __init__(self, rank, suit):
        self._rank = rank()
        self._suit = suit()

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):
        return "<Card " + self.__str__() + ">"

    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)


class Suit:
    color = "blank"

    def __str__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        return self.__class__ == other.__class__


class Rank:
    symbol = ""

    def __str__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        return self.__class__ == other.__class__


ORDERED_RANKS = OrderedDict([("Ace", "A"), ("Two", "2"), ("Three", "3"),
                             ("Four", "4"), ("Five", "5"), ("Six", "6"),
                             ("Seven", "7"), ("Eight", "8"), ("Nine", "9"),
                             ("Ten", "10"), ("Jack", "J"), ("Queen", "Q"),
                             ("King", "K")])
ORDERED_SUITS = OrderedDict([("Spades", "black"), ("Hearts", "red"),
                             ("Clubs", "black"), ("Diamonds", "red")])

RANKS = {rank: type(rank, (Rank,), {"symbol": symbol})
         for rank, symbol in ORDERED_RANKS.items()}

SUITS = {suit: type(suit, (Suit,), {"color": color})
         for suit, color in ORDERED_SUITS.items()}


class CardCollection(list):

    def draw(self, index):
        return self.pop(index)

    def draw_from_top(self):
        return self.draw(len(self) - 1)

    def draw_from_bottom(self):
        return self.draw(0)

    def top_card(self):
        return self[len(self) - 1]

    def bottom_card(self):
        return self[0]

    def add(self, card):
        self.append(card)


def StandardDeck():
    cards = [Card(RANKS[rank], SUITS[suit])
             for suit in ORDERED_SUITS.keys() for rank in ORDERED_RANKS.keys()]
    cards.reverse()
    return CardCollection(cards)


def BeloteDeck():
    return CardCollection(filter(lambda x: x.rank.symbol >= '7'
                                 or x.rank.symbol == '10', StandardDeck()))


def SixtySixDeck():
    return CardCollection(filter(lambda x: x.rank.symbol >= '9'
                                 or x.rank.symbol == '10', BeloteDeck()))
>>>>>>> 27b8bc94a0affac85b2780f057b389ff39faf9ac
