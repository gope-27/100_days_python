class animal:
    def __init__(self):
        self.num_eyes = 2
    def can_move(self):
        print("can breath in the water")


class fish(animal):
    def __init__(self):
        super().__init__()

    def cannot_move(self):
        print("cannot walk in the water")


df = fish()
df.can_move()
df.cannot_move()
print(df.num_eyes)
