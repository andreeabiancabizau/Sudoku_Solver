# # Sudoku Solver using SAT and CDCL

This project is a Sudoku puzzle solver built entirely on top of a SAT solving technique using the CDCL (Conflict-Driven Clause Learning) algorithm. It encodes Sudoku rules into CNF (Conjunctive Normal Form) and uses PycoSAT to find solutions.

## 🧩 What it does

- Allows the user to input a 9x9 Sudoku puzzle
- Encodes the constraints into CNF
- Uses PycoSAT to determine satisfiability
- Displays the solved board or notifies if the board is unsatisfiable

## 📜 Menu Options

1. **View Rules** – Briefly explains the constraints of a standard Sudoku board.
2. **Input Puzzle** – Prompts the user to enter a Sudoku puzzle row-by-row (empty cells as `0`).  It translates the board into CNF, runs the SAT solver, and prints the solution (if one exists).

## ✅ Example Input
003201769, where 0 is for the empty cells 
## 🔧 Requirements

- Python 3.x
- `pycosat` library: install with `pip install pycosat`

## 📁 File Structure

- `sudoku_solver.py`: Main program with menu interface and CNF encoder

## 🧠 Why SAT?

SAT solvers are great at solving constraint satisfaction problems, and Sudoku fits naturally into this model. This project demonstrates how even a game can be solved using powerful algorithmic logic techniques.

##This minigame was use for the MPI paper. 
