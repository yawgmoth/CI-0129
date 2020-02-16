import random

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
    def start_round(self):
        pass
    def deal(self, card):
        pass 
    def inform(self, community):
        pass 
    def get_action(self, actions):
        return random.choice(actions)
    def blind(self, amount):
        pass


def generate_deck():
    result = []
    for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
        for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
            result.append((suit,rank))
    return result


BIG_BLIND = 10
SMALL_BLIND = 5

class Game:
    def __init__(self, players):
        self.cards = generate_deck()
        self.players = players
        self.dealer = 0
        
    def draw(self):
        result = self.deck[0]
        self.deck = self.deck[1:]
        return result
        
    def enough_players(self):
        cnt = 0
        for p in self.active_players:
            if p: cnt += 1
        return cnt >= 2
        
    def round(self):
        self.deck = self.cards[:]
        self.community = []
        self.active_players = [p.money > BIG_BLIND for p in players]
        if not self.enough_players(): return
        self.pot = 0
        
        random.shuffle(self.deck)
        for p in self.players:
            p.start_round()        
        for i in range(2):
            for p in self.players:
                p.deal(self.draw())
        if not self.betting():
            return
        for i in range(3):
            self.community.append(self.draw())
        for p in self.players:
            p.inform(self.community)
        if not self.betting():
            return
        self.community.append(self.draw())
        for p in self.players:
            p.inform(self.community)
        if not self.betting():
            return
        for p in self.players:
            p.inform(self.community)
        if not self.betting():
            return
        self.determine_winner()
        
    def betting(self):
        for (p,a) in zip(self.players, self.active_players):
            if a:
                


def main():
    g = Game([])
    g.round()


if __name__ == "__main__":
    main()
        
        
        