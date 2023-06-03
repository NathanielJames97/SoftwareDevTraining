import random

class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_turn = "X"
    
    def display_instructions(self):
        print(
            """
            Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
            This will be a showdown between your human brain and my silicon processor.
            You will make your move known by entering a number, 0 - 8. The number
            will correspond to the board position as illustrated:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

            Prepare yourself, human. The ultimate battle is about to begin. \n
            """
        )

    def ask_yes_no(self, question):
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response

    def ask_number(self, question, low, high):
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

    def pieces(self):
        go_first = self.ask_yes_no("Do you require the first move? (y/n): ")
        if go_first == "y":
            print("\nThen take the first move. You will need it.")
            self.human = "X"
            self.computer = "O"
        else:
            print("\nYour bravery will be your undoing... I will go first.")
            self.computer = "X"
            self.human = "O"

    def display_board(self):
        print("\n\t", self.board[0], "|", self.board[1], "|", self.board[2])
        print("\t", "---------")
        print("\t", self.board[3], "|", self.board[4], "|", self.board[5])
        print("\t", "---------")
        print("\t", self.board[6], "|", self.board[7], "|", self.board[8], "\n")

    def legal_moves(self):
        moves = []
        for i in range(9):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def winner(self):
        WAYS_TO_WIN = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))

        for row in WAYS_TO_WIN:
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] != " ":
                return self.board[row[0]]

        if " " not in self.board:
            return "TIE"

        return None

    def human_move(self):
        move = None
        legal_moves = self.legal_moves()
        while move not in legal_moves:
            move = self.ask_number("Where will you move? (0 - 8): ", 0, 9)
            if move not in legal_moves:
                print("\nThat square is already occupied, foolish human. Choose another.\n")
        return move

    def computer_move(self):
        best_moves = [4, 0, 2, 6, 8, 1, 3, 5, 7]
        
        # Check if computer can win in the next move
        for move in self.legal_moves():
            self.board[move] = self.computer
            if self.winner() == self.computer:
                return move
            self.board[move] = " "
        
        # Check if human can win in the next move, and block it
        for move in self.legal_moves():
            self.board[move] = self.human
            if self.winner() == self.human:
                return move
            self.board[move] = " "
        
        # Choose the best open square
        for move in best_moves:
            if move in self.legal_moves():
                return move

    def next_turn(self):
        if self.current_turn == "X":
            self.current_turn = "O"
        else:
            self.current_turn = "X"

    def play(self):
        self.display_instructions()
        self.pieces()
        while self.winner() is None:
            if self.current_turn == self.human:
                move = self.human_move()
                self.board[move] = self.human
            else:
                move = self.computer_move()
                self.board[move] = self.computer
            self.display_board()
            self.next_turn()

        winner = self.winner()
        if winner == self.human:
            print("You win!")
        elif winner == self.computer:
            print("I win!")
        else:
            print("It's a tie!")

# Example usage:
game = TicTacToe()
game.play()
