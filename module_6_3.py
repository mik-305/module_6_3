class Horse:
    x_distance = 0          # Пройденный путь
    sound = 'Frrr'          # Звук, издаваемый лошадью
    def run(self, dx):
        self.dx = x_distance + dx

class Eagle:
    y_distance = 0          # высота полёта орла
    sound = 'I train, eat, sleep, and repeat' # Звук, издаваемый орлом
    def fly(self, dy):
        self.dy = y_distance + dy

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):

    def get_pos(self):

    def voice(self):
