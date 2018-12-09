from blist import blist


class MarbleGame:
    def __init__(self):
        self.ring = blist([0])
        self.current = 0

    def place(self, marble):
        if marble % 23 == 0:
            self.current = (self.current - 7) % len(self.ring)
            score = self.ring[self.current]
            del self.ring[self.current]
            return score + marble
        else:
            self.current = (self.current + 2) % len(self.ring)
            self.ring.insert(self.current, marble)
            return 0


def play(players, rounds):
    game = MarbleGame()
    scores = dict()
    current_player = 0
    for marble in range(1, rounds + 1):
        scores[current_player] = scores.get(current_player, 0) + game.place(marble)
        current_player = (current_player + 1) % players
    return scores
