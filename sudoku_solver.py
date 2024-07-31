import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row, column, and 3x3 subgrid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try all numbers from 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Make a tentative assignment
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[tk.Entry(root, width=3, font=("Arial", 18), justify="center") for _ in range(9)] for _ in range(9)]
        self.setup_grid()
        self.setup_buttons()

    def setup_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i, column=j, padx=5, pady=5)

    def setup_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=10, column=0, columnspan=5)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear)
        clear_button.grid(row=10, column=5, columnspan=4)

    def solve(self):
        board = self.get_board()
        if solve_sudoku(board):
            self.display_board(board)
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists")

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.cells[i][j].get()
                if val == '':
                    row.append(0)
                else:
                    row.append(int(val))
            board.append(row)
        return board

    def display_board(self, board):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    self.cells[i][j].insert(0, str(board[i][j]))

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
