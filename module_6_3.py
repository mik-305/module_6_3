class Horse:
    x_distance = 0          # Пройденный путь
    dx = 0
    sound = 'Frrr'          # Звук, издаваемый лошадью
    def run(self, dx):
        self.dx = x_distance + dx

class Eagle:
    y_distance = 0          # высота полёта орла
    dy = 0
    sound = 'I train, eat, sleep, and repeat' # Звук, издаваемый орлом
    def fly(self, dy):
        self.dy = y_distance + dy

class Pegasus(Horse, Eagle):
    #def __init__(self):

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy

    #def get_pos(self):

    def voice(self, sound):
        self.sound = sound

horse = Horse()
eagle = Eagle()
print(horse.sound)
print(eagle.sound)
