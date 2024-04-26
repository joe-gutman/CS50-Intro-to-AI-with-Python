# Crossword

Due to interaction with several of the course’s projects, and given that this course material was originally from 2020, the latest version of Python you should use in this course is Python 3.10.

Write an AI to generate crossword puzzles.

```bash
python generate.py data/structure1.txt data/words1.txt output.png

██████████████
███████M████R█
█INTELLIGENCE█
█N█████N████S█
█F██LOGIC███O█
█E█████M████L█
█R███SEARCH█V█
███████X████E█
██████████████
```
![crossword example](https://cs50.harvard.edu/ai/2020/projects/3/crossword/images/crossword.png)

**When to Do It**

By Sunday, December 31, 2023 at 8:59 PM PST.

**How to Get Help**

- Ask questions via Ed!
- Ask questions via any of CS50’s communities!

## Background

How might you go about generating a crossword puzzle? Given the structure of a crossword puzzle (i.e., which squares of the grid are meant to be filled in with a letter), and a list of words to use, the problem becomes one of choosing which words should go in each vertical or horizontal sequence of squares. We can model this sort of problem as a constraint satisfaction problem. Each sequence of squares is one variable, for which we need to decide on its value (which word in the domain of possible words will fill in that sequence). Consider the following crossword puzzle structure.

![crossword structure](https://cs50.harvard.edu/ai/2020/projects/3/crossword/images/structure.png)

In this structure, we have four variables, representing the four words we need to fill into this crossword puzzle (each indicated by a number in the above image). Each variable is defined by four values: the row it begins on (its i value), the column it begins on (its j value), the direction of the word (either down or across), and the length of the word. Variable 1, for example, would be a variable represented by a row of 1 (assuming 0 indexed counting from the top), a column of 1 (also assuming 0 indexed counting from the left), a direction of across, and a length of 4.

As with many constraint satisfaction problems, these variables have both unary and binary constraints. The unary constraint on a variable is given by its length. For Variable 1, for instance, the value BYTE would satisfy the unary constraint, but the value BIT would not (it has the wrong number of letters). Any values that don’t satisfy a variable’s unary constraints can therefore be removed from the variable’s domain immediately.

The binary constraints on a variable are given by its overlap with neighboring variables. Variable 1 has a single neighbor: Variable 2. Variable 2 has two neighbors: Variable 1 and Variable 3. For each pair of neighboring variables, those variables share an overlap: a single square that is common to them both. We can represent that overlap as the character index in each variable’s word that must be the same character. For example, the overlap between Variable 1 and Variable 2 might be represented as the pair (1, 0), meaning that Variable 1’s character at index 1 necessarily must be the same as Variable 2’s character at index 0 (assuming 0-indexing, again). The overlap between Variable 2 and Variable 3 would therefore be represented as the pair (3, 1): character 3 of Variable 2’s value must be the same as character 1 of Variable 3’s value.

For this problem, we’ll add the additional constraint that all words must be different: the same word should not be repeated multiple times in the puzzle.

The challenge ahead, then, is write a program to find a satisfying assignment: a different word (from a given vocabulary list) for each variable such that all of the unary and binary constraints are met.

### Getting Started

- Download the distribution code from [here](https://cdn.cs50.net/ai/2020/x/projects/3/crossword.zip) and unzip it.

### Understanding

There are two Python files in this project: crossword.py and generate.py. The first has been entirely written for you, the second has some functions that are left for you to implement.

First, let’s take a look at crossword.py. This file defines two classes, Variable (to represent a variable in a crossword puzzle) and Crossword (to represent the puzzle itself).

Notice that to create a Variable, we must specify four values: its row i, its column j, its direction (either the constant Variable.ACROSS or the constant Variable.DOWN), and its length.

The Crossword class requires two values to create a new crossword puzzle: a structure_file that defines the structure of the puzzle (the _ is used to represent blank cells, any other character represents cells that won’t be filled in) and a words_file that defines a list of words (one on each line) to use for the vocabulary of the puzzle. Three examples of each of these files can be found in the data directory of the project, and you’re welcome to create your own as well.

Note in particular, that for any crossword object crossword, we store the following values:

- `crossword.height`: integer representing the height of the crossword puzzle.
- `crossword.width`: integer representing the width of the crossword puzzle.
- `crossword.structure`: 2D list representing the structure of the puzzle. `crossword.structure[i][j]` will be `True` if the cell is blank and `False` otherwise.
- `crossword.words`: set of all the words to draw from when constructing the crossword puzzle.
- `crossword.variables`: set of all the variables in the puzzle (each is a `Variable` object).
- `crossword.overlaps`: dictionary mapping a pair of variables to their overlap. For any two distinct variables `v1` and `v2`, `crossword.overlaps[v1, v2]` will be `None` if the two variables have no overlap, and will be a pair of integers `(i, j)` if the variables do overlap.


Crossword objects also support a method neighbors that returns all of the variables that overlap with a given variable. That is to say, crossword.neighbors(v1) will return a set of all of the variables that are neighbors to the variable v1.

Next, take a look at generate.py. Here, we define a class CrosswordCreator that we’ll use to solve the crossword puzzle. When a CrosswordCreator object is created, it gets a crossword property that should be a Crossword object (and therefore has all of the properties described above). Each CrosswordCreator object also gets a domains property: a dictionary that maps variables to a set of possible words the variable might take on as a value. Initially, this set of words is all of the words in our vocabulary, but we’ll soon write functions to restrict these domains.

We’ve also defined some functions for you to help with testing your code: print will print to the terminal a representation of your crossword puzzle for a given assignment (every assignment, in this function and elsewhere, is a dictionary mapping variables to their corresponding words). save, meanwhile, will generate an image file corresponding to a given assignment (you’ll need to pip3 install Pillow if you haven’t already to use this function). letter_grid is a helper function used by both print and save that generates a 2D list of all characters in their appropriate positions for a given assignment: you likely won’t need to call this function yourself, but you’re welcome to if you’d like to.

Finally, notice the solve function. This function does three things: first, it calls enforce_node_consistency to enforce node consistency on the crossword puzzle, ensuring that every value in a variable’s domain satisfy the unary constraints. Next, the function calls ac3 to enforce arc consistency, ensuring that binary constraints are satisfied. Finally, the function calls backtrack on

## How to Submit
- You may not have your code in your `ai50/projects/2020/x/crossword` branch nested within any further subdirectories (such as a subdirectory called `crossword` or `project4a`). That is to say, if the staff attempts to access `https://github.com/me50/USERNAME/blob/ai50/projects/2020/x/crossword/crossword.py`, where `USERNAME` is your GitHub username, that is exactly where your file should live. If your file is not at that location when the staff attempts

1. Visit [this link](https://submit.cs50.io/invites/3f39c5c0747a4890a0a0df58f1023d5b), log in with your GitHub account, and click Authorize cs50. Then, check the box indicating that you’d like to grant course staff access to your submissions, and click Join course.
2. Install Git and, optionally, install submit50.
3. If you’ve installed submit50, execute

    ```bash
    submit50 ai50/projects/2020/x/crossword
    ```

    Otherwise, using Git, push your work to `https://github.com/me50/USERNAME.git`, where `USERNAME` is your GitHub username, on a branch called `ai50/projects/2020/x/crossword`.
4. Submit this form.

You can then go to [this link](https://cs50.me/cs50ai) to view your current progress!