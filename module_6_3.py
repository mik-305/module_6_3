x_distance = 0
y_distance = 0
global dx
dx = 0
class Horse:
    sound = 'Frrr'
    def run(self, dx):
        self.dx = dx
        global x_distance
        x_distance = x_distance + dx
        return x_distance
class Eagle:
    dy = 0
    sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.dy = dy
        global y_distance
        y_distance = y_distance + dy
        return y_distance

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        x_distance = Horse.run
        y_distance = Eagle.fly
    def get_pos(self):

        return x_distance, y_distance

    def voice(self, sound):
        self.sound = sound
        return print(sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.voice()
