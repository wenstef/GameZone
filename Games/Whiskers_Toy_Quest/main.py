import customtkinter as ctk

from game import GameGUI
from game_state import WhiskersGameState
from whiskers_choices import WhiskersChoices

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Whiskers Toy Quest")
    root.geometry("800x600")

    whiskers_choices = WhiskersChoices()
    game_state = WhiskersGameState(whiskers_choices)
    gui = GameGUI(root, game_state, whiskers_choices)

    root.mainloop()