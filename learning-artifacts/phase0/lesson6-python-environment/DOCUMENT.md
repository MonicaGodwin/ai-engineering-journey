# Phase 0, Lesson 6: Python Environments

## Why projects need separate environments

Different projects can require different versions of the same package. A virtual environment gives each project its own Python interpreter and installed packages, so changing one project does not have to change another project's dependencies.

The environment directory is local to the machine and should not be pushed to GitHub. Keep it ignored in `.gitignore`. Share the project's dependency configuration and lockfile instead.

## Activating the project environment in VS Code

My notebook uses the repository's `.venv`. At first, the VS Code terminal used the parent environment:

```text
/home/recoding/ai/.venv/bin/python
```

From the repository root, I activated the repository environment and checked the interpreter:

```bash
source .venv/bin/activate
python -c "import sys; print(sys.executable)"
```

It printed:

```text
/home/recoding/ai/ai-engineering-journey/.venv/bin/python
```

This confirms that the terminal is using the repository's Python environment. On Linux and macOS, `which python` is another way to check. On Windows, use `where python`. In VS Code, the notebook kernel and integrated terminal interpreter are separate selections, so check each one when their package behavior differs.

## Dependency files and repeatable installs

`pyproject.toml` describes a project's direct dependencies and configuration. A lockfile records exact versions for the full dependency set, including transitive dependencies. Committing the lockfile helps another machine install the same package versions.

I learned the purpose of these files but did not create a `pyproject.toml` or lockfile during this lesson.

## Package manager choices

- Python's built-in `venv` creates a lightweight virtual environment.
- `uv` can create environments and manage packages and lockfiles.
- Conda is useful when an environment needs non-Python dependencies such as a particular CUDA toolkit or C library.

When using conda, prefer conda for packages in that environment. Installing with pip can bypass conda's dependency tracking and make conflicts harder to resolve. My current repository environment is a Python `venv`; I did not use conda.

## CUDA troubleshooting note

An NVIDIA GPU being present does not guarantee that PyTorch can use it. Check the driver with `nvidia-smi` and check the CUDA version PyTorch was built with using `torch.version.cuda`. An incompatible PyTorch CUDA build and GPU driver can make CUDA unavailable. Virtual environments can access the GPU; they only isolate Python packages.

## Practice record

- Confirmed the terminal initially pointed at `/home/recoding/ai/.venv/bin/python`.
- Activated the repository `.venv` and confirmed the interpreter path changed to `/home/recoding/ai/ai-engineering-journey/.venv/bin/python`.
- Learned that environments isolate packages, lockfiles pin exact versions, and mixing pip and conda can cause dependency conflicts.
- Lesson quiz: **1/3**. Review checking the active interpreter and diagnosing PyTorch CUDA/driver compatibility.
