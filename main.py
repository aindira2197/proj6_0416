class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, s):
        self.score += s

p = Player("Indira")
p.add_score(10)
print(p.score)
