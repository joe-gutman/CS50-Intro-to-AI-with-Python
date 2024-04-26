# Minesweeper

Write an AI to play Minesweeper.

## Background

Minesweeper is a puzzle game that consists of a grid of cells, where some of the cells contain hidden “mines.” Clicking on a cell that contains a mine detonates the mine, and causes the user to lose the game. Clicking on a “safe” cell (i.e., a cell that does not contain a mine) reveals a number that indicates how many neighboring cells – where a neighbor is a cell that is one square to the left, right, up, down, or diagonal from the given cell – contain a mine.

### Propositional Logic

Your goal in this project will be to build an AI that can play Minesweeper. Recall that knowledge-based agents make decisions by considering their knowledge base, and making inferences based on that knowledge.

One way we could represent an AI’s knowledge about a Minesweeper game is by making each cell a propositional variable that is true if the cell contains a mine, and false otherwise.

Instead, we’ll represent each sentence of our AI’s knowledge like the below.

{A, B, C, D, E, F, G, H} = 1

Every logical sentence in this representation has two parts: a set of cells on the board that are involved in the sentence, and a number count, representing the count of how many of those cells are mines. The above logical sentence says that out of cells A, B, C, D, E, F, G, and H, exactly 1 of them is a mine.

Why is this a useful representation? In part, it lends itself well to certain types of inference.

### Knowledge Representation

Instead, we’ll represent each sentence of our AI’s knowledge like the below.

{A, B, C, D, E, F, G, H} = 1

Every logical sentence in this representation has two parts: a set of cells on the board that are involved in the sentence, and a number count, representing the count of how many of those cells are mines. The above logical sentence says that out of cells A, B, C, D, E, F, G, and H, exactly 1 of them is a mine.

Why is this a useful representation? In part, it lends itself well to certain types of inference. 

### Getting Started

1. Download the distribution code from [this link](https://cdn.cs50.net/ai/2020/x/projects/1/minesweeper.zip) and unzip it.
2. Once in the directory for the project, run `pip3 install -r requirements.txt` to install the required Python package (pygame) for this project if you don’t already have it installed.

### Understanding

There are two main files in this project: `runner.py` and `minesweeper.py`. `minesweeper.py` contains all of the logic the game itself and for the AI to play the game. `runner.py` has been implemented for you, and contains all of the code to run the graphical interface for the game. Once you’ve completed all the required functions in `minesweeper.py`, you should be able to run `python runner.py` to play Minesweeper (or let your AI play for you)!

Let’s open up `minesweeper.py` to understand what’s provided. There are three classes defined in this file, `Minesweeper`, which handles the gameplay; `Sentence`, which represents a logical sentence that contains both a set of cells and a count; and `MinesweeperAI`, which handles inferring which moves to make based on knowledge.

The `Minesweeper` class has been entirely implemented for you. Notice that each cell is a pair `(i, j)` where `i` is the row number (ranging from 0 to `height - 1`) and `j` is the column number (ranging from 0 to `width - 1`).

The `Sentence` class will be used to represent logical sentences of the form described in the Background. Each sentence has a set of cells within it and a count of how many of those cells are mines. The class also contains functions `known_mines` and `known_safes` for determining if any of the cells in the sentence are known to be mines or known to be safe. It also contains functions `mark_mine` and `mark_safe` to update a sentence in response to new information about a cell.

Finally, the `MinesweeperAI` class will implement an AI that can play Minesweeper. The AI class keeps track of a number of values. `self.moves_made` contains a set of all cells already clicked on, so the AI knows not to pick those again. `self.mines` contains a set of all cells known to be mines. `self.safes` contains a set of all cells known to be safe. And `self.knowledge` contains a list of all of the Sentences that the AI knows to be true.

The `mark_mine` function adds a cell to `self.mines`, so the AI knows that it is a mine. It also loops over all sentences in the AI’s knowledge and informs each sentence that the cell is a mine, so that the sentence can update itself accordingly if it contains information about that mine. The `mark_safe` function does the same thing, but for safe cells instead.

The remaining functions, `add_knowledge`, `make_safe_move`, and `make_random_move`, are left up to you!

## Specification

Complete the implementations of the `Sentence` class and the `MinesweeperAI` class in `minesweeper.py`.

In the `Sentence` class, complete the implementations of `known_mines`, `known_safes`, `mark_mine`, and `mark_safe`.

- The `known_mines` function should return a set of all of the cells in `self.cells` that are known to be mines.
- The `known_safes` function should return a set of all the cells in `self.cells` that are known to be safe.
- The `mark_mine` function should first check to see if `cell` is one of the cells included in the sentence.
    - If `cell` is in the sentence, the function should update the sentence so that `cell` is no longer in the sentence, but still represents a logically correct sentence given that `cell` is known to be a mine.
    - If `cell` is not in the sentence, then no action is necessary.
- The `mark_safe` function should first check to see if `cell` is one of the cells included in the sentence.
    - If `cell` is in the sentence, the function should update the sentence so that `cell` is no longer in the sentence, but still represents a logically correct sentence given that `cell` is known to be safe.
    - If `cell` is not in the sentence, then no action is necessary.

In the `MinesweeperAI` class, complete the implementations of `add_knowledge`, `make_safe_move`, and `make_random_move`.

- `add_knowledge` should accept a cell (represented as a tuple `(i, j)`)) and its corresponding count, and update `self.mines`, `self.safes`, `self.moves_made`, and `self.knowledge` with any new information that the AI can infer, given that `cell` is known to be a safe cell with `count` mines neighboring it.
    - The function should mark the cell as one of the moves made in the game.
    - The function should mark the cell as a safe cell, updating any sentences that contain the cell as well.
    - The function should add a new sentence to the AI’s knowledge base, based on the value of `cell` and `count`, to indicate that `count` of the cell’s neighbors are mines. Be sure to only include cells whose state is still undetermined in the sentence.
    - If, based on any of the sentences in `self.knowledge`, new cells can be marked as safe or as mines, then the function should do so.
    - If, based on any of the sentences in `self.knowledge`, new sentences can be inferred (using the subset method described in the Background), then those sentences should be added to the knowledge base as well.
    - Note that any time that you make any change to your AI’s knowledge, it may be possible to draw new inferences that weren’t possible before. Be sure that those new inferences are added to the knowledge base if it is possible to do so.
- `make_safe_move` should return a move `(i, j)` that is known to be safe.
    - The move returned must be known to be safe, and not a move already made.
    - If no safe move can be guaranteed, the function should return None.
    - The function should not modify `self.moves_made`, `self.mines`, `self.safes`, or `self.knowledge`.
- `make_random_move` should return a random move `(i, j)`.
    - This function will be called if a safe move is not possible: if the AI doesn’t know where to move, it will choose to move randomly instead.
    - The move must not be a move that has already been made.
    - The move must not be a move that is known to be a mine.
    - If no such moves are possible, the function should return None.
