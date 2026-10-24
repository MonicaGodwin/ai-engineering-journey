# Phase 0, Lesson 5: Jupyter Notebooks

## What a notebook is

A Jupyter notebook (`.ipynb`) is an interactive document made of cells. Code cells run Python and show results inline. Markdown cells hold formatted notes and explanations.

The **kernel** is the Python process that runs the code cells and keeps variables in memory. Cells share that kernel, so a variable created in one cell can be used by another. Restarting the kernel clears that state.

## Creating and running a notebook in VS Code

1. Open the Command Palette with **Ctrl+Shift+P**.
2. Choose **Jupyter: Create New Jupyter Notebook**.
3. Create a Python environment when prompted and select it as the kernel.
4. Enter `2 + 2` in a code cell and press **Shift+Enter** to run it.
5. Use **+ Markdown** to add a text cell. For example:

   ```markdown
   # My first notebook
   Testing a Python expression.
   ```

The notebook toolbar showed the selected `.venv` Python 3.12.3 environment. I ran the code and Markdown cells successfully.

## Timing code with Jupyter magics

Magic commands belong to Jupyter; they are not ordinary Python syntax. `%` starts a line magic, while `%%` starts a cell magic.

`%timeit` repeats a short expression and reports an average. I ran:

```python
%timeit sum(range(100))
```

My notebook reported about `1.51 µs ± 13.8 ns per loop` (the exact timing depends on the machine and current load).

`%%time` runs the whole cell once and reports CPU and wall time. I ran:

```python
%%time
sum(range(1_000_000))
```

The successful run reported about `34.6 ms` CPU time and `57.6 ms` wall time. I initially typed an extra `sum(`, saw the cell error, corrected the expression, and ran it successfully.

## Check that the notebook runs from a clean start

Notebook cells can be run in any order. This is convenient for exploration, but it can leave hidden dependencies: a later cell might use a variable created by an earlier run even if that cell was deleted or is below it.

I used **Restart** and **Run All** in VS Code. All cells ran successfully from a fresh kernel in top-to-bottom order. This is a useful check before sharing a notebook.

## When to use a notebook or a script

Use a notebook to explore data, prototype a model, visualize results, and explain an experiment. Move reusable utilities, training pipelines, and production code into `.py` scripts. The workflow is: **explore in notebooks, ship in scripts**.

## Practice record

- Created a Python notebook in VS Code using a local Python 3.12.3 virtual environment.
- Ran code and Markdown cells, including `2 + 2`.
- Used `%timeit` for a repeated microbenchmark and `%%time` for a one-time cell timing.
- Fixed a syntax mistake and verified the notebook with **Restart and Run All**.
- Scored 3/3 on the lesson quiz.
