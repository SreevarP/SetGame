import colorama
from colorama import Fore, Back, Style
import time
colorama.init(autoreset=True)
print(f"""{Back.BLACK}{Fore.RED}
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀ █▀▀ ▀█▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ▄█ ██▄ ░█░   █▄█ █▀█ █░▀░█ ██▄""")
ternary = ['0000', '0001',
'0002','0010','0011','0012','0020','0021','0022','0100','0101','0102','0110','0111','0112','0120','0121','0122','0200','0201','0202','0210','0211','0212','0220','0221','0222','1000','1001','1002','1010','1011','1012','1020','1021','1022','1100','1101','1102','1110','1111','1112','1120','1121','1122','1200','1201','1202','1210','1211','1212','1220','1221','1222','2000',
'2001','2002','2010','2011','2012','2020','2021','2022','2100','2101','2102', '2110', '2111','2112','2120','2121','2122','2200','2201','2202','2210','2211','2212','2220','2221', '2222']
print()
time.sleep(2)
print(f"{Back.BLACK}The deck consists of 81 unique cards that vary in four features across three possibilities for each kind of feature: number of shapes (one, two, or three), shape (diamond, rectangle, circle), shading (black, light blue, or white), and color (red, green, or purple).[1] Each possible combination of features (e.g. a card with three striped green diamonds) appears as a card precisely once in the deck.")
time.sleep(2)
print()
print(f'''{Back.BLACK}Several games can be played with these cards, all involving the concept of a set. A set consists of three cards satisfying all of these conditions: They all have the same number or have three different numbers.
They all have the same shape or have three different shapes.
They all have the same shading or have three different shadings.
They all have the same color or have three different colors.''')
print()


#creates deck
def createList(max, length):
  list = []
  for i in range(length):
    list.append(random.randint(0, max))
  return list

#shuffles cards
def shuffle(list):
  for i in range(len(list)):
    first = random.randint(0, len(list) - 1)
    random_index = random.randint(0, len(list) - 1)
    temp = list[random_index]
    list[random_index] = list[first]
    list[first] = temp
  return list


def displayCard(howMany):
  
  global cards
  cards = []

  for i in range(howMany):
    number = random.choice(ternary)
    ternary.remove(number)
    card = drawCard(number) + Back.RESET + "  "
    print(f"{i}. {card}")
    cards.append(number)


def chooseCard(cards, c1, c2, c3):
  print(drawCard(cards[c1]), drawCard(cards[c2]), drawCard(cards[c3]))
  return [cards[c1], cards[c2], cards[c3]]

#draws the cards
def drawCard(tNumber):
  d1 = int(tNumber[0])
  d2 = int(tNumber[1])
  d3 = int(tNumber[2])
  d4 = int(tNumber[3])
  color = 0
  shape = 0
  shading = 0
  amount = 0

  if d1 == 0:
    shape = '◇'
  if d1 == 1:
    shape = '▯'
  if d1 == 2:
    shape = '○'

  if d2 == 0:
    color = Fore.RED
  if d2 == 1:
    color = Fore.GREEN
  if d2 == 2:
    color = Fore.MAGENTA

  if d3 == 0:
    shading = Back.WHITE
  if d3 == 1:
    shading = Back.LIGHTBLUE_EX
  if d3 == 2:
    shading = Back.BLACK

  if d4 == 0:
    amount = 1
  if d4 == 1:
    amount = 2
  if d4 == 2:
    amount = 3

  return f"{shading}{color}{amount * shape}"



import random

displayCard(12)

card = int(input("which card? 0-11"))
card2 = int(input("which card? 0-11"))
card3 = int(input("which card? 0-11"))

chosen_cards = chooseCard(cards, card, card2, card3)


def isSet(card1, card2, card3):
  # F and F  = true or (True and True and True)
  #false and true = false
  # (card1[0] == card2[0]) and (card2[0] == card3[0]) checks if all the cards have the same attribute(in this case its shape).
  # or if they all have completely different attributes
  if not (((card1[0] == card2[0]) and (card2[0] == card3[0])) or
          (((card1[0] != card2[0]) and (card1[0] != card3[0])) and
           (card2[0] != card3[0]))):
    return False

  if not (((card1[1] == card2[1]) and (card2[1] == card3[1])) or
          (((card1[1] != card2[1]) and (card1[1] != card3[1])) and
           (card2[1] != card3[1]))):
    return False

  if not (((card1[2] == card2[2]) and (card2[2] == card3[2])) or
          (((card1[2] != card2[2]) and (card1[2] != card3[2])) and
           (card2[2] != card3[2]))):
    return False

  if not (((card1[3] == card2[3]) and (card2[3] == card3[3])) or
          (((card1[3] != card2[3]) and (card1[3] != card3[3])) and
           (card2[3] != card3[3]))):
    return False

  return True


if isSet(chosen_cards[0], chosen_cards[1], chosen_cards[2]):
  print("These cards are a set!")
else:
  print("These cards are not a set. Try again")



















'''
c1 = str(random.randint(0, 2)) + str(random.randint(0, 2)) + str(
  random.randint(0, 2)) + str(random.randint(0, 2))
c2 = str(random.randint(0, 2)) + str(random.randint(0, 2)) + str(
  random.randint(0, 2)) + str(random.randint(0, 2))
c3 = str(random.randint(0, 2)) + str(random.randint(0, 2)) + str(
  random.randint(0, 2)) + str(random.randint(0, 2))
'''
print()
'''
while not (isSet(c1, c2, c3)):
  c1 = str(random.randint(0, 2)) + str(random.randint(0, 2)) + str(
    random.randint(0, 2)) + str(random.randint(0, 2))
  c2 = str(random.randint(0, 2)) + str(random.randint(0, 2)) + str(
    random.randint(0, 2)) + str(random.randint(0, 2))
  c3 = str(random.randint(0, 2)) + str(random.randint(0, 2)) + str(
    random.randint(0, 2)) + str(random.randint(0, 2))
print(c1, c2, c3)
print(drawCard(c1), drawCard(c2), drawCard(c3))
print()
'''


