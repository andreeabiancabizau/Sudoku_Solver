import itertools
import pycosat

def print_menu():
    print("""
=== Sudoku via SAT Solver ===
1. See Sudoku Rules
2. Enter Your Own Puzzle
3. Exit
    """)

def show_rules():
    print("""
Rules of Sudoku:
- The board is a 9x9 grid.
- Each row must contain the digits from 1 to 9 exactly once.
- Each column must contain the digits from 1 to 9 exactly once.
- Each of the nine 3x3 squares must contain the digits from 1 to 9 exactly once.
To enter a board:
- You will input 9 rows of digits (use 0 for empty cells).
  Example row: 530070000
-And do not forget to have fun! :) 
    """)

def read_board():
    board = []
    print("Enter your Sudoku puzzle row by row:")
    for i in range(9):
        while True:
            row = input(f"Row {i + 1}: ").strip()
            if len(row) == 9 and all(c.isdigit() and 0 <= int(c) <= 9 for c in row):
                board.append([int(c) for c in row])
                break
            else:
                print("Invalid row. Please enter exactly 9 digits (0-9).")
    return board

def varnum(i, j, d):
    return 81 * (i - 1) + 9 * (j - 1) + d

def sudoku_to_cnf(board):
    cnf = []

    for i, j in itertools.product(range(1, 10), repeat=2):
        cnf.append([varnum(i, j, d) for d in range(1, 10)])

    for i, j in itertools.product(range(1, 10), repeat=2):
        for d1 in range(1, 10):
            for d2 in range(d1 + 1, 10):
                cnf.append([-varnum(i, j, d1), -varnum(i, j, d2)])

    for i, d in itertools.product(range(1, 10), repeat=2):
        cnf.append([varnum(i, j, d) for j in range(1, 10)])
        for j1 in range(1, 10):
            for j2 in range(j1 + 1, 10):
                cnf.append([-varnum(i, j1, d), -varnum(i, j2, d)])

    for j, d in itertools.product(range(1, 10), repeat=2):
        cnf.append([varnum(i, j, d) for i in range(1, 10)])
        for i1 in range(1, 10):
            for i2 in range(i1 + 1, 10):
                cnf.append([-varnum(i1, j, d), -varnum(i2, j, d)])

    for d in range(1, 10):
        for block_i in range(0, 3):
            for block_j in range(0, 3):
                cells = [
                    (i, j)
                    for i in range(block_i * 3 + 1, block_i * 3 + 4)
                    for j in range(block_j * 3 + 1, block_j * 3 + 4)
                ]
                cnf.append([varnum(i, j, d) for i, j in cells])
                for (i1, j1), (i2, j2) in itertools.combinations(cells, 2):
                    cnf.append([-varnum(i1, j1, d), -varnum(i2, j2, d)])

    for i in range(9):
        for j in range(9):
            d = board[i][j]
            if d != 0:
                cnf.append([varnum(i + 1, j + 1, d)])

    return cnf

def decode_solution(solution):
    board = [[0 for _ in range(9)] for _ in range(9)]
    for v in solution:
        if v > 0:
            v -= 1
            i, j, d = v // 81, (v % 81) // 9, (v % 9) + 1
            board[i][j] = d
    return board

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "| "
            row += f"{board[i][j] or '.'} "
        print(row.strip())

def main():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_rules()
        elif choice == "2":
            board = read_board()
            print("\nInput board:")
            print_board(board)
            cnf = sudoku_to_cnf(board)
            print("\nSolving...")
            solution = pycosat.solve(cnf)
            if solution == "UNSAT":
                print("No solution exists.")
            else:
                solved = decode_solution(solution)
                print("\nSolved board:")
                print_board(solved)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select 1, 2 or 3.")

if __name__ == "__main__":
    main()
