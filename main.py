import os, time


def rollDice(size):
  import random
  return random.randint(1, size)


def calculateHp():
  return rollDice(6) * rollDice(12) / 2 + 10


def calculateStrength():
  return rollDice(6) * rollDice(12) / 2 + 10


def generateCharacter():
  print("\n\033[0mName your Legend: \033[32m")
  name = input("")
  print("\033[0mCharacter Type (Human, Elf, Wizard, Orc): \033[32m")
  type = input("")
  return name, type


def printCharacter(name, type, hp, strength):
  print("\033[0m")
  print(name)
  time.sleep(1)
  print("HEALTH: ", hp)
  time.sleep(1)
  print("STRENGTH: ", strength)
  time.sleep(1)

def printResults(name,hp):
  time.sleep(1)
  print(name)
  time.sleep(1)
  print("HEALTH: ", hp)
  print()

def printFinalDestroy(name1, name2, round):
  time.sleep(1)
  print("\nOh no, ", name1, "has died")
  time.sleep(2)
  os.system("clear")
  print("\U0001F6E1 \033[1;32mBATTLE TIME\033[0m \U00002694\n")
  print(name2,"destroyed", name1,"in", round, "rounds!")
  
  
def battle():
  print("\U0001F6E1 \033[1;32mBATTLE TIME\033[0m \U00002694\n")
  #creates 1 character
  name1, type1 = generateCharacter()
  hp1 = calculateHp()
  strength1 = calculateStrength()
  printCharacter(name1, type1, hp1, strength1)
  print("\nWho are they battling? \n")
  #creates 2 character
  name2, type2 = generateCharacter()
  hp2 = calculateHp()
  strength2 = calculateStrength()
  printCharacter(name2, type2, hp2, strength2)
  time.sleep(2)

  os.system("clear")
  print("\U0001F6E1 \033[1;32mBATTLE TIME\033[0m \U00002694\n")
  print("\nThe battle Begins!\n")
  #counter for rounds
  round = 0

  #rolling dice
  while True:
    roll1 = rollDice(6)
    roll2 = rollDice(6)
    damage = abs(strength1 - strength2) + 1

    if roll1 == roll2:
      continue
    elif roll1 > roll2:
      round += 1
      time.sleep(1)
      if round == 1:
        print(name1, "wins the first blow.")
        print(name2, "takes a hit , with",damage, "damage\n")
      else:
        print(name1, "wins round", round)
        print(name2, "takes a hit , with",damage, "damage\n")
      hp2 -= damage
      
    else:
      round += 1
      time.sleep(1)
      if round == 1:
        print(name2, "wins the first blow.")
        print(name1, "takes a hit , with",damage, "damage\n")
      else:
        print(name2, "wins round", round, ".")
        print(name1, "takes a hit , with",damage, "damage\n")
      hp1 -= damage
      
    #print the results
    printResults(name1, hp1)
    printResults(name2, hp2)

    #resulting line for current battle
    if hp1 > 0 and hp2 > 0:
      time.sleep(1)
      print("And they're both standing for the next round!")
      time.sleep(2)
      os.system("clear")
      time.sleep(1)
      print("\U0001F6E1 \033[1;32mBATTLE TIME\033[0m \U00002694\n")
      time.sleep(1)
      print("\nThe battle continues!\n")
    else:
      break

  #after leaves the while when one of hp is less or equels to 0
  if hp1 <= 0:
    printFinalDestroy(name1, name2, round)
  else:
    printFinalDestroy(name2, name1, round)

#run the battle
battle()
