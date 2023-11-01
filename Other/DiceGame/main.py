import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def _roll(self):
        self._value = random.randint(1, 6)
        return self.value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def _increment_counter(self):
        self._counter += 1

    def _decrement_counter(self):
        self._counter -= 1

    def _roll_die(self):
        return self._die._roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("============================")
        print("🎲 Welcome to Roll the Dice!")
        print("============================")
        while True:
            self._play_round()
            game_over = self._check_game_over()
            if game_over:
                break
        self._play_again()

    def _play_round(self):
        # Welcome the user
        self._print_round_welcome()

        # Roll the dice
        player_value = self._player._roll_die()
        computer_value = self._computer._roll_die()

        # Show the values
        self._show_dice(player_value, computer_value)

        # Determine winner and loser
        if player_value > computer_value:
            print("You won the round!")
            self._update_counters(winner=self._player, loser=self._computer)
        elif computer_value > player_value:
            print("The computer won this round. Try again.")
            self._update_counters(winner=self._computer, loser=self._player)
        else:
            print("It's a tie.")

        # Show counter
        self._show_counters()

    def _print_round_welcome(self):
        print("\n-------- New Round --------")
        input("🎲 Press any key to roll the dice. 🎲")

    def _show_dice(self, player_value, computer_value):
        print(f"\nYour die: {player_value}")
        print(f"Computer die: {computer_value}\n")

    def _update_counters(self, winner, loser):
        winner._decrement_counter()
        loser._increment_counter()

    def _show_counters(self):
        print(f"Your counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")

    def _check_game_over(self):
        if self._player.counter == 0:
            self._show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self._show_game_over(self._computer)
            return True
        else:
            return False

    def _show_game_over(self, winner):
        if winner.is_computer:
            print("\n===========")
            print("You lose.")
            print("GAME OVER!")
            print("===========")
        else:
            print("\n===========")
            print("You win! Congratulations!")
            print("GAME OVER.")
            print("===========")

    def _play_again(self):
        print("\nWould you like to play again?\n")
        response = input("Type 'y' for 'yes' and 'n' for 'no': ")
        response = response.lower()
        if response == "y":
            self._player._counter = 10
            self._computer._counter = 10
            game.play()
        elif response == "n":
            print("\n😊 Thanks for playing! Have a nice day! 😊")
        else:
            print("\nPlease input either 'y' or 'n'.")
            self._play_again()


# Create instances
player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

# Start Game
game.play()
