class PlayerCharacter:
  def __init__(self, name):
    self.name = name
    self.age = 30

  def run(self):
    print('run')

  def stampa(self):
    print(f'my name is {self.name}')

player1 = PlayerCharacter('antonio abc')

print(player1.name, player1.age)

player1.run()

player1.stampa()