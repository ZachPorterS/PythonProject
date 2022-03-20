import numpy as np
import time

class Pokemon:
  def __init__(self, name, type, moves, EVs, health='100' ):
    self.name = name
    self.type = type
    self.moves = moves
    self.attack = EVs['ATK']
    self.defense = EVs['DFS']
    self.health = 20

  def Fighter(self):
    '''Tracks two pokemon during a battle'''
    print("---POKEMON BATTLE---")
    print(f"\n{self.name}")
    print("TYPE:: ", self.type)
    print("ATK:: ", self.attack)
    print("LVL:: ", 3 * (1 + np.mean([self.attack, self.defense])))
    print("\nVS")
    time.sleep(2)

  def FighterTwo(self, Pokemon_Two):
    print("---POKEMON BATTLE---")
    print(f"\n{Pokemon_Two.name}")
    print("TYPE:: ", Pokemon_Two.type)
    print("ATK:: ", Pokemon_Two.attack)
    print("LVL:: ", 3 * (1 + np.mean([Pokemon_Two.attack, Pokemon_Two.defense])))
    print("\nVS")
    time.sleep(2)

  def Weaknesses (self, Pokemon_Two):
    type_check = ['Fire', 'Water', 'Grass']
    for i, k in enumerate(type_check):
      if self.type == k:
        # Both Pokemon are of the same type
        if Pokemon_Two.type == k:
          string_attack = "It's not very effective..."
          string_attack_two = "It's not very effective..."
          
        # Attack is super effective against the opposing Pokemon
        # Check by grabbing the index of the type + 1 and getting the remainder
        # avoid getting out of bounds of the list
        if Pokemon_Two.type == type_check[(i + 1) % 3]:
          Pokemon_Two.attack *= 2
          Pokemon_Two.defense *= 2
          self.attack /= 2
          self.defense /= 2
          string_attack = "It's not very effective..."
          string_attack_two = "It's super effective!"
