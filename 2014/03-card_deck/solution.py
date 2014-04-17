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
