#!/usr/bin/env python3
"""Simple Tkinter GUI for the Rock Paper Scissors game.
Reuses get_computer_choice and determine_winner from
`rock_paper_scissors_game.py` to keep logic in one place.
"""
import tkinter as tk
from functools import partial
from rock_paper_scissors_game import get_computer_choice, determine_winner


class RPSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0

        self._create_widgets()

    def _create_widgets(self):
        header = tk.Label(self, text="Rock - Paper - Scissors", font=("Arial", 14, "bold"))
        header.pack(padx=12, pady=(12, 6))

        self.status_label = tk.Label(self, text="Make your move:", font=("Arial", 11))
        self.status_label.pack(padx=8, pady=(0, 8))

        btn_frame = tk.Frame(self)
        btn_frame.pack(padx=8, pady=6)

        rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=partial(self.play, 'rock'))
        paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=partial(self.play, 'paper'))
        scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=partial(self.play, 'scissors'))

        rock_btn.pack(side="left", padx=6)
        paper_btn.pack(side="left", padx=6)
        scissors_btn.pack(side="left", padx=6)

        self.result_label = tk.Label(self, text="", font=("Arial", 11))
        self.result_label.pack(padx=8, pady=(8, 4))

        self.computer_label = tk.Label(self, text="", font=("Arial", 10))
        self.computer_label.pack(padx=8, pady=(0, 8))
        score_frame = tk.Frame(self)
        score_frame.pack(padx=8, pady=(0, 12))

        self.player_score_label = tk.Label(score_frame, text="You: 0", font=("Arial", 10, "italic"), width=10, anchor="w")
        self.player_score_label.grid(row=0, column=0, sticky="w")

        self.computer_score_label = tk.Label(score_frame, text="Computer: 0", font=("Arial", 10, "italic"), width=14, anchor="e")
        self.computer_score_label.grid(row=0, column=1, sticky="e")
        self.score_label.pack(padx=8, pady=(0, 12))

        quit_btn = tk.Button(self, text="Quit", command=self.destroy)
        quit_btn.pack(pady=(0, 12))

    def play(self, player_choice: str):
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)

        if winner == 'player':
            self.player_score += 1
            result_text = "You win!"
        elif winner == 'computer':
            self.computer_score += 1
            result_text = "Computer wins!"
        else:
            result_text = "It's a tie!"

        self.result_label.config(text=result_text)
        self.player_score_label.config(text=f"You: {self.player_score:2d}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score:2d}")
        self.score_label.config(text=f"You: {self.player_score}    Computer: {self.computer_score}")


def main():
    app = RPSApp()
    app.mainloop()


if __name__ == '__main__':
    main()
