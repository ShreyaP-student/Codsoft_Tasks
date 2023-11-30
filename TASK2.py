import tkinter as tk
from tkinter import messagebox
import copy

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.board = [""] * 9
        self.current_player = "X"
        self.buttons = []
        self.create_gui()

    def create_gui(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.root, text="", font=('normal', 20), width=5, height=2,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_button_click(self, row, col):
        index = 3 * row + col
        if self.board[index] == "" and not self.is_game_over():
            self.board[index] = self.current_player
            self.buttons[index]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()
                self.make_move()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def make_move(self):
        if self.current_player == "O":
            best_move = self.minimax(self.board, "O")[1]
            self.board[best_move] = "O"
            self.buttons[best_move]["text"] = "O"
            if self.check_winner():
                messagebox.showinfo("Game Over", "AI wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def minimax(self, current_board, current_player):
        if self.check_winner():
            return 1, None
        elif self.is_board_full():
            return 0, None

        available_moves = [i for i, val in enumerate(current_board) if val == ""]
        best_score, best_move = (float('-inf'), None) if current_player == "O" else (float('inf'), None)

        for move in available_moves:
            new_board = copy.deepcopy(current_board)
            new_board[move] = current_player
            score, _ = self.minimax(new_board, "X" if current_player == "O" else "O")

            if (current_player == "O" and score > best_score) or (current_player == "X" and score < best_score):
                best_score, best_move = score, move

        return best_score, best_move

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return True
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "":
                return True
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        return False

    def is_board_full(self):
        return all(cell != "" for cell in self.board)

    def is_game_over(self):
        return self.check_winner() or self.is_board_full()

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button["text"] = ""
        self.current_player = "X"

    def run(self):
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.root.mainloop()
if __name__ == "__main__":
    game = TicTacToe()
    game.run()