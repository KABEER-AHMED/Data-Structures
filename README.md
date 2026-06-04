# Data Structures

This folder is a Python learning collection for core data structures, algorithms, and recursion exercises. Most examples are stored as Jupyter notebooks, with a few standalone Python scripts for quick execution.

## Why This Is Useful

The project is useful for practicing how common data structures work internally instead of only using built-in Python containers. It covers beginner-friendly implementations and demonstrations of:

- Deques and queues.
- Linked lists.
- Searching algorithms.
- Recursion.
- Stack-style number conversion.
- Turtle graphics recursion.
- Basic card/deck classes used in game simulations.

## Project Contents

- `Dequeue.ipynb` - Deque class and palindrome-checker exercise.
- `Hash.ipynb` - Hashing/hash-table practice notebook.
- `LinkedList.ipynb` - Node and linked-list implementation with add, search, remove, and print behavior.
- `List.ipynb` - List practice notebook.
- `Recursion.ipynb` - Recursive thinking notes, base conversion, and turtle recursion examples.
- `Searching_Algorithms.py` - Binary search, first/last occurrence search, and occurrence-counting examples.
- `Test.py` - Turtle recursion script that draws a branching tree.
- `main.ipynb` - Card/deck/player practice code.
- `README.md` - Project documentation.

## Requirements

Most files use standard Python only. For notebooks, install Jupyter:

```bash
pip install jupyter
```

The turtle examples use Python's standard `turtle` module and require a desktop environment where a graphics window can open.

## How To Use

To explore the notebooks:

```bash
jupyter notebook
```

Open the notebook for the topic you want to study and run the cells in order.

To run the standalone searching examples:

```bash
python Searching_Algorithms.py
```

To run the turtle recursion demo:

```bash
python Test.py
```

## Important Notes

- `binary_search`, `First_occurrence_bin`, and `last_Occurrence_bin` expect the input list to be sorted.
- Some notebooks are practice scratchpads and may contain partial examples rather than polished modules.
- Running turtle scripts will open a GUI window and wait for a click before closing.
- Function and method names use mixed capitalization because these are learning exercises. If you turn this into a package, standardize naming before expanding it.

## Good Next Improvements

- Add unit tests for each data structure and algorithm.
- Convert reusable notebook code into `.py` modules.
- Add complexity notes such as time and space complexity.
- Add small input/output examples for every algorithm.
