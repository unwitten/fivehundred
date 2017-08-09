import sys
from time import sleep

from automat import MethodicalMachine


class Game(object):
    _machine = MethodicalMachine()

    def __init__(self):
        self.go_to_main_menu()

    # Game States
    @_machine.state(initial=True)
    def initial(self):
        """Initial state for the game. Allows calling `_show_main_menu` at start of game."""

    @_machine.state()
    def main_menu(self):
        """The game is on the main menu, waiting for the player to press start."""

    @_machine.state()
    def running_game(self):
        """The game is in progress."""

    @_machine.state()
    def game_over(self):
        """The game has finished."""

    @_machine.state()
    def quit(self):
        """State when quitting the game."""

    # Inputs
    @_machine.input()
    def start_game(self):
        """Start playing the game."""

    @_machine.input()
    def finish_game(self):
        """Finish playing the game."""

    @_machine.input()
    def go_to_main_menu(self):
        """Quit out of the game and return to the main menu."""

    @_machine.input()
    def quit_game(self):
        """Quit out of the game from the main menu."""

    # Outputs
    @_machine.output()
    def _show_main_menu(self):
        """Show the menu menu to the player."""
        answer = input("Do you want to play the game? [y/n] ")
        if answer == 'y':
            self.start_game()
        elif answer == 'n':
            self.quit_game()

    @_machine.output()
    def _play_game(self):
        """Main game loop."""
        answer = None
        while answer != 'y':
            answer = input("Is this a great game? [y/n] ")

        self.finish_game()

    @_machine.output()
    def _show_end_screen(self):
        """Display end game message."""
        print("Nice work!")
        self.go_to_main_menu()

    @_machine.output()
    def _quit_game(self):
        """Display message and close the game."""
        print("Goodbye.")
        sleep(1.5)
        print("Loser.")
        sys.exit(0)

    # Connections
    initial.upon(go_to_main_menu, enter=main_menu, outputs=[_show_main_menu])
    main_menu.upon(start_game, enter=running_game, outputs=[_play_game])
    main_menu.upon(quit_game, enter=quit, outputs=[_quit_game])
    running_game.upon(finish_game, enter=game_over, outputs=[_show_end_screen])
    game_over.upon(go_to_main_menu, enter=main_menu, outputs=[_show_main_menu])


if __name__ == '__main__':
    game = Game()
