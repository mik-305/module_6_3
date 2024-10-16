class Horse:
    global sound
    sound = 'Frrr'
    x_distance = 0
    def run(self, dx):
        self.dx = dx
        global x_distance
        x_distance = x_distance + dx
        print('x_distance + dx ', x_distance + dx)
        return x_distance
class Eagle:
    dy = 0
    global sound
    sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy): #, y_distance):
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
        return x_distance, y_distance
    def get_pos(self):

        return x_distance, y_distance

    def voice(self):
        print(sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
