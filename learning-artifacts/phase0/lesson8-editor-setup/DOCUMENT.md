# Phase 0, Lesson 8: Editor Setup

## VS Code setup I practiced

I already had the **Python** and **Jupyter** extensions and used VS Code to open Python files and notebooks. I configured these settings in User `settings.json`:

```json
{
  "files.autoSave": "afterDelay",
  "python.analysis.typeCheckingMode": "basic",
  "notebook.output.scrolling": true,
  "editor.formatOnSave": true,
  "editor.rulers": [88, 120]
}
```

- **Basic type checking** asks Pylance to report likely type and argument mistakes while I edit.
- **Notebook output scrolling** keeps long training output from taking over the page.
- **Format on save** runs the selected formatter whenever I save a file.
- **Rulers** mark useful line-width guides in the editor.
- **Auto-save after a delay** saves edits automatically.

## Activate Black Formatter in VS Code

1. Open the **Extensions** panel and install **Black Formatter** by Microsoft (`ms-python.black-formatter`) if it is not installed.
2. Open a Python `.py` file.
3. Press **Ctrl+Shift+P** and select **Format Document With…**.
4. Select **Configure Default Formatter…**.
5. Choose **Black Formatter**.
6. Make sure `"editor.formatOnSave": true` is set in VS Code settings.

I verified the formatter with this code:

```python
def add(a,b):
    return a+b
```

After selecting Black, I saved it and confirmed the code became:

```python
def add(a, b):
    return a + b
```

I also tested **Format Document** directly, then undid the formatting and saved again. The save reformatted the code, confirming that both Black and format-on-save were active.

## Type checking practice

In `me.py`, I tested a function with an integer type annotation:

```python
def double(value: int) -> int:
    return value * 2

double("hello")
```

Pylance underlined the string argument because the function expects an integer. If the function should work on numbers, use `double(5)`. If it should accept strings, update the annotations to `str`; multiplying a string by 2 repeats it.

I also have a simple `python_greet` example in `hello.py`.

## Other editor tools

- **Pylance** provides autocomplete, type information, and diagnostics. The red underline in my type-mismatch example confirmed it was active.
- **GitLens** helps inspect Git history and line changes.
- **Debugpy** supports step-through debugging in Python.
- **Remote SSH** connects VS Code to files and terminals on a remote machine, such as a GPU server. I learned its role but did not connect to a remote host in this lesson.

## Practice record

- Used the Python and Jupyter extensions already available in VS Code.
- Enabled Pylance basic type checking and verified a type mismatch warning.
- Installed and selected Black Formatter as the default Python formatter.
- Confirmed that format-on-save reformats code.
- Enabled notebook output scrolling and configured editor rulers and auto-save.
- Lesson quiz score: **3/3**.
