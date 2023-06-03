import tkinter as tk
import tkinter.messagebox
import random

class TicTacToeUI:
    def __init__(self):
        self.board = [" "] * 9
        self.current_turn = "X"
        
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text=" ", width=10, height=5,
                               command=lambda idx=i: self.make_move(idx))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
        
        self.display_instructions()
        self.pieces()
        
        self.window.mainloop()
    
    def display_instructions(self):
        instructions = tk.Label(self.window, text="Welcome to Tic-Tac-Toe!\n\n"
                                                  "Make your move by clicking on a square.")
        instructions.grid(row=3, columnspan=3)
        
    def pieces(self):
        go_first = tk.messagebox.askyesno("Tic-Tac-Toe", "Do you require the first move?")
        if go_first:
            self.human = "X"
            self.computer = "O"
            self.current_turn = "X"
        else:
            self.human = "O"
            self.computer = "X"
            self.current_turn = "X"
            self.make_computer_move()
        
    def make_move(self, idx):
        if self.board[idx] == " " and self.current_turn == self.human:
            self.board[idx] = self.human
            self.buttons[idx].config(text=self.human, state=tk.DISABLED)
            if self.check_winner(self.human):
                self.end_game(self.human)
            elif " " not in self.board:
                self.end_game("TIE")
            else:
                self.current_turn = self.computer
                self.make_computer_move()
    
    def make_computer_move(self):
        if self.current_turn == self.computer:
            available_moves = [idx for idx, val in enumerate(self.board) if val == " "]
            if available_moves:
                random_move = random.choice(available_moves)
                self.board[random_move] = self.computer
                self.buttons[random_move].config(text=self.computer, state=tk.DISABLED)
                if self.check_winner(self.computer):
                    self.end_game(self.computer)
                elif " " not in self.board:
                    self.end_game("TIE")
                else:
                    self.current_turn = self.human
    
    def check_winner(self, player):
        winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                                (0, 4, 8), (2, 4, 6))            # Diagonals
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False
    
    def end_game(self, result):
        if result == self.human:
            message = "Congratulations! You won!"
        elif result == self.computer:
            message = "You lost! Better luck next time."
        else:
            message = "It's a tie!"
            tk.messagebox.showinfo("Game Over", message)
        self.window.quit()

# Start the Tic-Tac-Toe game
game = TicTacToeUI()

''' TODO:
Implement a more attractive user interface:

Choose a GUI library such as Tkinter, Pygame, or PyQt.
Design the game board and buttons using the library's tools for creating graphical elements.
Map the button clicks to the corresponding game logic to handle player moves and update the game state.
Display the game board and relevant information (e.g., current player, score) using the GUI library's text and drawing functions.
Implement different difficulty levels for the computer player:

Define different levels of difficulty, such as easy, medium, and hard.
For each difficulty level, create a corresponding algorithm or strategy for the computer player to make moves.
Update the computer player's logic to use the appropriate strategy based on the selected difficulty level.
Add a score tracker:

Create variables to keep track of the scores for the human player and computer player.
Update the game logic to increment the scores after each game.
Display the scores on the screen after each game and provide an option to reset the scores.
Implement a multiplayer mode:

Add a player selection screen or a mode switch button to allow the user to choose between single-player and two-player modes.
Modify the game logic to handle two human players taking turns.
Update the user interface to display the current player and handle input from both players.
Implement additional features:

Choose the specific additional features you want to implement, such as undo/redo, hint system, save/load functionality, or an AI opponent.
Design the user interface elements and integrate them into the game logic.
Implement the necessary functions and algorithms to support the desired features.
Improve error handling and input validation:

Add appropriate error handling mechanisms to handle invalid user input, such as displaying error messages and prompting the user to enter valid input.
Validate user input to ensure it falls within the expected range or format.
Implement safeguards to prevent crashes or unexpected behavior due to incorrect input.





'''