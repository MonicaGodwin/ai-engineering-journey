# Phase 0, Lesson 12: Debugging & Profiling

## What makes AI bugs tricky

AI code can run without an exception and still give misleading results. A suspiciously high test score may come from **data leakage**, such as examples or target information appearing in both the training and test data. A useful first check is whether the test set remains independent of training and model tuning.

Debugging has several layers:

1. Check ordinary Python behavior and program flow.
2. Inspect tensor shapes, dtypes, devices, and values such as NaN or infinity.
3. Review training behavior over time, including losses and gradients.

Profiling measures resource use—such as execution time or memory—so the slow or memory-heavy part can be found before optimizing.

## PyTorch environment

In my VS Code notebook, PyTorch reported:

```text
PyTorch: 2.14.1+cpu
CUDA available: False
```

The notebook uses CPU-only PyTorch, so CUDA memory profiling is not available in this environment.

## Inspecting tensor values

I used this helper to print a tensor's shape, dtype, device, value range, mean, and whether it contains NaNs:

```python
def debug_print(name, tensor):
    print(
        f"{name}: shape={tuple(tensor.shape)}, "
        f"dtype={tensor.dtype}, device={tensor.device}"
    )
    print(
        f"  min={tensor.min().item():.1f}, "
        f"max={tensor.max().item():.1f}, "
        f"mean={tensor.mean().item():.1f}, "
        f"has_nan={tensor.isnan().any().item()}"
    )
```

On a `2 × 3` tensor containing values 1 through 6, it printed:

```text
batch: shape=(2, 3), dtype=torch.float32, device=cpu
  min=1.0, max=6.0, mean=3.5, has_nan=False
```

I cloned the tensor, inserted a NaN, and ran the helper again:

```text
bad_batch: shape=(2, 3), dtype=torch.float32, device=cpu
  min=nan, max=nan, mean=nan, has_nan=True
```

The `has_nan=True` flag exposes invalid values before they silently contaminate later calculations. The range and mean becoming NaN are additional signs that the tensor needs investigation.

## Finding and fixing a shape mismatch

Matrix multiplication requires the inner dimensions to match. An input tensor of shape `(4, 3)` cannot multiply weights of shape `(5, 2)` because 3 does not equal 5. I corrected the weight shape to `(3, 2)`:

```python
inputs = torch.randn(4, 3)
weights = torch.randn(3, 2)
outputs = inputs @ weights
print(inputs.shape, weights.shape, outputs.shape)
```

The output was:

```text
torch.Size([4, 3]) torch.Size([3, 2]) torch.Size([4, 2])
```

I first got a `NameError` because I had not run the cell that defined `inputs`. Running the complete cell with all definitions fixed the hidden-state issue.

## Conditional breakpoints and training logs

In a Python training script, a conditional breakpoint can stop at the failure instead of interrupting every step:

```python
if torch.isnan(loss):
    breakpoint()
```

At the debugger prompt, inspect values such as `loss.item()`, `outputs.shape`, and gradients; use `c` to continue or `q` to quit.

For longer runs, Python's `logging` module can add timestamps and severity levels and write messages to a file. TensorBoard can record loss, learning rate, weights, and gradients over training steps. These records help distinguish patterns such as a loss that does not improve, unstable loss, or training loss improving while validation loss gets worse.

## Profiling execution time

I used the standard-library `cProfile` to profile a function that sums 100,000 integers:

```python
import cProfile

def count_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

profiler = cProfile.Profile()
profiler.enable()
count_sum(100_000)
profiler.disable()
profiler.print_stats(sort="cumtime")
```

My run reported **43 function calls in 0.029 seconds**. The `count_sum` row used about **0.027 seconds**. Jupyter execution overhead is also present, and timing varies by run and machine. In a real training loop, time data loading, the forward pass, and the backward pass separately; optimize the stage the measurements identify.

For memory, `tracemalloc` can inspect Python CPU allocations. PyTorch exposes CUDA memory statistics only when CUDA is available. Data loading can also be a training bottleneck, so measure it before assuming the GPU needs to be faster.

## Practice record

- Verified the notebook has PyTorch 2.14.1 CPU and no CUDA.
- Printed tensor metadata and detected an inserted NaN.
- Diagnosed matrix dimensions and corrected the weights from `(5, 2)` to `(3, 2)`.
- Used `cProfile` to find the time spent in a Python function.
- Learned to check test/train overlap, use a conditional breakpoint for NaN loss, and log or plot training behavior.
- Lesson quiz score: **3/3**.
