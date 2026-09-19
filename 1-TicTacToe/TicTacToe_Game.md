# Approach for Tic-Tac-Toe in Python

## 1. Represent the Board
Use a simple data structure — most commonly a list of 9 elements (indices 0–8) representing a 3x3 grid, or a list of lists (3x3 nested). Each cell holds `' '`, `'X'`, or `'O'`.

## 2. Display the Board
Write a function that prints the current state in a readable 3x3 grid format, usually with row/column separators like `|` and `-`.

## 3. Track Game State
Keep variables for:
- Current player (alternate between X and O each turn)
- The board itself
- Game status (ongoing, won, draw)

## 4. Handle Player Input
Ask the player to enter a position (e.g., 1–9, or row/column). Validate that:
- The input is a valid number/format
- The chosen cell isn't already occupied

## 5. Update the Board
Place the current player's mark in the chosen cell after validation passes.

## 6. Check for a Win
After every move, check all 8 possible winning combinations (3 rows, 3 columns, 2 diagonals) to see if the current player has 3 in a row.

## 7. Check for a Draw
If all 9 cells are filled and no one has won, declare a draw.

## 8. Game Loop
Wrap everything in a loop:
1. Print board
2. Get input
3. Validate
4. Update board
5. Check win/draw
6. Switch player
7. Repeat until game ends

## Suggested Build Order
1. Get the board printing correctly
2. Get two humans able to alternate placing marks
3. Add win/draw detection
4. Add input validation and error handling

