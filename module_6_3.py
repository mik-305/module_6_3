class Horse:                            # Создаем класс Лошадь
    def __init__(self):
        self.x_distance = 0             # Начальные координаты
        self.sound = 'Frrr'             # Издаваемый звук

    def run(self, dx):
        self.x_distance += dx           # Движение по горизонтали
        return self.x_distance

class Eagle:                            # Создаем класс Орёл
    def __init__(self):
        self.y_distance = 0             # Начальные координаты
        self.sound = 'I train, eat, sleep, and repeat'   # Издаваемый звук

    def fly(self, dy):
        self.y_distance += dy           # Движение по вертикали
        return self.y_distance

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        x_distance = self.run(dx)
        y_distance = self.fly(dy)
        return x_distance, y_distance

    def get_pos(self):
        return self.x_distance, self.y_distance  # Координаты

    def voice(self):
        print(self.sound)                       # Издаваемый звук

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
