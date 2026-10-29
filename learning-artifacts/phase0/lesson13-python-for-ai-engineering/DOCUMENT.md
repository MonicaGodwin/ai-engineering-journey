# Phase 0, Lesson 13: Python for AI Engineering

> Session notes: this document records the concepts and examples covered with the tutor. The course lesson and its official quiz were not available in this checkout, so these notes are not a transcript of the full course material.

## Organize reusable code into modules

As an AI project grows, putting every operation in one script makes it harder to read and debug. Put related reusable functions in modules such as `metrics.py`, `data.py`, and `model.py`, then import them where needed.

For example, a small accuracy function can live in `metrics.py`:

```python
def accuracy(correct: int, total: int) -> float:
    if total == 0:
        return 0.0
    return correct / total
```

The type hints say that `correct` and `total` are integers and the result is a float. The `total == 0` guard prevents division by zero. In the session, I identified that the guard makes `accuracy(0, 0)` return `0.0` instead of raising a division-by-zero error.

Another script can reuse the function:

```python
from metrics import accuracy

score = accuracy(correct=8, total=10)
print(f"Accuracy: {score:.0%}")
```

`8 / 10` is `0.8`, or 80%. The `:.0%` format displays the fraction as a percentage with no decimal places. Keeping the function in one module means that training and evaluation scripts can share the same implementation. A fix in `metrics.py` then applies to every importer, instead of maintaining separate copies that could drift apart.

## Use a library for standard metrics

For common metrics, scikit-learn provides a tested implementation:

```python
from sklearn.metrics import accuracy_score

true_labels = [1, 0, 1]
predictions = [1, 1, 1]
score = accuracy_score(true_labels, predictions)
print(score)  # 0.666...
```

Accuracy is the fraction of predictions that match the true labels. Here, two of the three pairs match, so the result is `2 / 3`, approximately `0.67`. A library handles the comparison and tallying; understanding the small implementation first makes the library result easier to interpret.

## What I learned

- Separate reusable Python code into modules and import it into scripts that need it.
- Type hints document expected inputs and outputs; they do not replace runtime validation.
- Guard against a zero denominator before dividing.
- `8 / 10` is `0.8`, which can be formatted as `80%` with `:.0%`.
- Shared modules make fixes easier to maintain and prevent duplicated implementations from drifting.
- Accuracy compares each prediction with its true label and returns the fraction that match; scikit-learn can calculate this standard metric.

## Practice record

- Answered the zero-total check: it prevents a division-by-zero error.
- Identified easier debugging and less bulky code as benefits of separating a metric into its own module.
- Worked through a three-example accuracy calculation together: two predictions matched, giving `2 / 3` (about `0.67`).
- Did not run a local script or the official course quiz during this session.
