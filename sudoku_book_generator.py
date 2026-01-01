"""
Sudoku book generator for KDP (6"x9" pages).

Requirements:
    pip install fpdf2

This script creates:
    - A folder "sudoku_book" (in the script's directory)
    - A PDF "sudoku_book.pdf" inside that folder
    - NUM_PUZZLES pages with playable Sudoku grids
    - Optionally, solution pages right after each puzzle
"""

from fpdf import FPDF
import os
import random
import copy

# ---------- Config ----------
NUM_PUZZLES = 30          # how many puzzles in the book
ADD_SOLUTIONS = True      # whether to add solution page after each puzzle

# KDP 6"x9" in points (1 point = 1/72 inch)
PAGE_WIDTH = 6 * 72        # 432
PAGE_HEIGHT = 9 * 72       # 648
MARGIN = 36                # 0.5 inch margin

# Folder for output
OUTPUT_FOLDER = "sudoku_book"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "sudoku_book.pdf")


# ---------- Sudoku generator ----------
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def valid(grid, num, pos):
    row, col = pos
    # Check row
    if num in grid[row]:
        return False
    # Check column
    if num in [grid[r][col] for r in range(9)]:
        return False
    # Check box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num:
                return False
    return True


def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    row, col = find
    nums = list(range(1, 10))
    random.shuffle(nums)
    for num in nums:
        if valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0
    return False


def generate_complete_grid():
    grid = [[0]*9 for _ in range(9)]
    solve(grid)
    return grid


def remove_numbers(grid, removal_count=40):
    # Create a puzzle by removing a number of cells
    # (simple, not guaranteed minimal or unique but works for casual puzzle book)
    puzzle = copy.deepcopy(grid)
    attempts = removal_count
    while attempts > 0:
        row = random.randrange(9)
        col = random.randrange(9)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            attempts -= 1
    return puzzle


# ---------- PDF drawing ----------
class SudokuPDF(FPDF):
    def __init__(self):
        super().__init__(format=(PAGE_WIDTH, PAGE_HEIGHT))
        self.set_auto_page_break(auto=True, margin=MARGIN)

    def draw_grid(self, grid, title=""):
        """
        Draw a Sudoku grid on a new page. `grid` is 9x9 list (0 = empty).
        """
        self.add_page()
        # Title
        self.set_font("Arial", "B", 16)
        self.cell(0, 12, title, ln=True, align="C")
        self.ln(4)

        # Compute cell size: keep square grid centered
        usable_width = PAGE_WIDTH - 2*MARGIN
        usable_height = PAGE_HEIGHT - 2*MARGIN - 40  # leave some space at top for title
        cell_size = min(usable_width, usable_height) / 9.0

        x_start = (PAGE_WIDTH - 9*cell_size) / 2.0
        y_start = MARGIN + 20

        # Draw cells
        self.set_font("Arial", "", 12)
        for i in range(10):
            line_width = 0.8
            if i % 3 == 0:
                line_width = 1.5
            # Horizontal
            self.set_line_width(line_width)
            self.line(x_start, y_start + i*cell_size, x_start + 9*cell_size, y_start + i*cell_size)
            # Vertical
            self.line(x_start + i*cell_size, y_start, x_start + i*cell_size, y_start + 9*cell_size)

        # Fill numbers
        self.set_font("Arial", "", 14)
        for r in range(9):
            for c in range(9):
                num = grid[r][c]
                if num != 0:
                    # Position number at center of cell
                    x = x_start + c*cell_size
                    y = y_start + r*cell_size
                    self.text(x + cell_size*0.35, y + cell_size*0.7, str(num))


# ---------- Build book ----------
def build_sudoku_book():
    pdf = SudokuPDF()

    for idx in range(1, NUM_PUZZLES + 1):
        # Generate puzzle
        full = generate_complete_grid()
        puzzle = remove_numbers(full, removal_count=40)  # adjust difficulty by removing count

        # Title for puzzle page
        pdf.draw_grid(puzzle, title=f"Sudoku Puzzle {idx}")

        # Optionally add solution page
        if ADD_SOLUTIONS:
            pdf.draw_grid(full, title=f"Solution {idx}")

    # Save PDF
    pdf.output(OUTPUT_FILE)
    print(f"Sudoku book generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    build_sudoku_book()
