class Character:

    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter


class Enemy(Character):

    def __init__(self, x, y, img_file, speed):
        Character.__init__(self, x, y, img_file, speed, 5)
        self.message = "I'm here to protect my master"


class Player(Character):

    def __init__(self, x, y, img_file, speed):
        Character.__init__(self, x, y, img_file, speed, 6)
        self.speed = 56


class DifficultEnemy(Enemy):

    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 80)


class EasyEnemy(Enemy):

    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 40)
        Enemy.life_counter = 1


easy_enemy = EasyEnemy(15, 15, "img")
hard_enemy = DifficultEnemy(30, 30, "img2")
player = Player(0, 0, "img3", 30)

print(easy_enemy.speed)
print(easy_enemy.x)
print(easy_enemy.life_counter)
print(hard_enemy.y)
print(hard_enemy.speed)
print(hard_enemy.img_file)
print(player.life_counter)

