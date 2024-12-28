import customtkinter as ctk
import os
from tkinter import Image
from PIL import Image, ImageTk


class GameGUI:
    def __init__(self, master, game_state, whiskers_choices):
        self.master = master
        self.master.title("Whiskers Toy Quest")
        self.master.geometry("800x600")

        # Save game state and choices
        self.game_state = game_state
        self.whiskers_choices = whiskers_choices

        # Configure grid layout
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        # Title label
        self.title_label = ctk.CTkLabel(self.master, text="Whiskers Toy Quest", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Left frame for button and image
        self.left_frame = ctk.CTkFrame(self.master)
        self.left_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        # Story label
        self.story_label = ctk.CTkLabel(self.left_frame, text="", wraplength=300, justify="left",
                                        font=ctk.CTkFont(size=14))
        self.story_label.pack()

        self.image_label = ctk.CTkLabel(self.left_frame, text="Image not found", width=400, height=300)
        self.image_label.pack(pady=20, padx=20)

        # Right frame for story and input
        self.right_frame = ctk.CTkScrollableFrame(self.master, width=400, height=500)
        self.right_frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        # Question label
        self.question_label = ctk.CTkLabel(self.right_frame, text="", wraplength=300, font=ctk.CTkFont(size=14))
        self.question_label.pack()

        # Message label
        self.message_label = ctk.CTkLabel(self.right_frame, text="", wraplength=300, justify="left",
                                            font=ctk.CTkFont(size=14))
        self.message_label.pack()

        # Input field
        self.user_input = ctk.CTkEntry(self.right_frame, placeholder_text="Type your choice here", width=350)
        self.user_input.pack(pady=20)
        self.user_input.bind("<Return>", self.handle_input)
        self.user_input.configure(state="disabled")

        # Start the game
        self.start_game()

    def start_game(self):
        """Start the game by displaying the intro story."""
        self.display_next_char()


    def display_next_char(self):
        """Display the next character in the intro story."""
        char = self.game_state.get_next_line()
        if char:
            # Add the character to the story text (label)
            current_text = self.story_label.cget("text")
            current_text += char
            self.story_label.configure(text=current_text)
            # Call this method again after 50 milliseconds to display the next character
            self.master.after(50, self.display_next_char) # Delay of 50 milliseconds
        else:
            # Enable the user input after the scene description is fully displayed
            self.user_input.configure(state="normal")
            self.update_stage_description()

    def update_stage_description(self):
        """Update the stage description and question."""
        stage_info = self.game_state.get_current_stage_info()
        if stage_info:
            self.story_label.configure(text=stage_info['scene_desc'])
            self.question_label.configure(text=stage_info['question'])


    def handle_input(self, event):
        """Handle the user input."""
        user_input = self.user_input.get().strip()
        if user_input:
            self.user_input.delete(0, "end")
            if self.game_state.transition_to_next_state(user_input):
                self.display_next_char()

