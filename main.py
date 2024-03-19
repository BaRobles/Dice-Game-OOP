import random


class Dice:
  # def __init__(self, value=None):
  #   self._value = value
  # or:
  def __init__(self):
    self._value = None

# we're only writing the getter, and not the setter also, because we don't want 
# to change the value of the dice, we just want to present it to the user.
  @property
  def value(self):
    return self._value

  def roll(self):
    new_value = random.randint(1, 6)
    self._value = new_value
    return new_value


class Player:
  def __init__(self, dice, is_computer=False):
    self._dice = dice
    self._is_computer = is_computer
    self._counter = 10

  @property
  def dice(self):
    return self._dice

  @property
  def is_computer(self):
    return self._is_computer

  @property
  def counter(self):
    return self._counter

  def increment_counter(self):
    self._counter += 1

  def decrement_counter(self):
    self._counter -=1

  # aggregation
  def roll_dice(self):
    return self._dice.roll()
# The reason for returning the value from self._dice.roll() 
#in the roll_dice method is to allow the Player class to access the result of the dice 
# roll. This design keeps the dice-rolling logic within the Dice class while still 
# allowing the Player class to initiate a dice roll and know the outcome.


class DiceGame:
  def __init__(self, player, computer):
    self._player = player
    self._computer = computer

  def play(self):
    print("============================")
    print("🎲 Welcome to Roll the Dice!")
    print("============================")
    while True:
      self.play_round()
      game_over = self.check_game_over()
      if game_over:
        break

  def play_round(self):
    # Welcome the user
    self.print_round_welcome()
    # roll the dice
    player_value = self._player.roll_dice()
    computer_value = self._computer.roll_dice()
    # show the values
    self.show_dice(player_value, computer_value)

    # determine winner and loser
    if player_value > computer_value:
      print("You won the round! 🎉")
      # self.update_counters(self._player, self._computer) BEST TO READ:
      self.update_counters(winner=self._player, loser=self._computer)
    elif computer_value > player_value:
      print("The computer won this round. 😢 Try again.")
      self.update_counters(winner=self._computer, loser=self._player)
    else:
      print("It's a tie! 🤝")

    # show counters
    self.show_counters()

  def print_round_welcome(self):
    print("\n------ New Round ------")
    input("🎲 Press any key to roll the dice. 🎲")

  def show_dice(self, player_value, computer_value):
    print(f"Your dice: {player_value}  ")
    print(f"Computer dice: {computer_value}\n")

  def update_counters(self, winner, loser):
    winner.decrement_counter()
    loser.increment_counter()

  def show_counters(self):
    print(f"\nYour counter: {self._player.counter}")
    print(f"Computer counter: { self._computer.counter}")

  def check_game_over(self):
    if self._player.counter == 0:
      self.show_game_over(self._player)
      return True
    elif self._computer.counter == 0:
      self.show_game_over(self._computer)
      return True
    else:
      return False

  def show_game_over(self, winner):
    if winner.is_computer:
      self.game_over_message()
      print("The computer won the game. Sorry...")
      print("===================")
    else:
      self.game_over_message()
      print("You won the game! Congratulations! 🎉✌🏼😎")
      print("===================")

  def game_over_message(self):
    print("\n==================")
    print("✨ G A M E   O V E R ✨")
    print("===================")

player_dice = Dice()
computer_dice = Dice()

# composition
my_player = Player(player_dice, is_computer=False)
computer_player = Player(computer_dice, is_computer=True)

game = DiceGame(my_player, computer_player)

# start the game
game.play()





      








    
# testing the Player class
# my_dice = Dice()

# my_player = Player(my_dice, True)
# # my_player = Player(my_dice, is_computer=True)
# print(my_player.dice)
# print(my_player.is_computer)

# print(my_player.counter)
# my_player.increment_counter()
# print(my_player.counter)
# # wrong way to see if the increment is working:
# # print(my_player.increment_counter())

# print("======")
# print(my_dice.value)
# my_player.roll_dice()
# print(my_dice.value)

# print(my_player.dice.value)
# my_player.roll_dice()
# print(my_player.dice.value)