# Lesson 3: GPU Setup & Cloud

## What a GPU is

A **GPU** (graphics processing unit) is a processor designed to do many similar calculations at the same time. It was built for graphics, but the same ability to process large batches of numbers in parallel makes it useful for AI. Neural networks repeatedly perform matrix and tensor operations, which GPUs can handle much faster than a CPU for many workloads.

A **CPU** (central processing unit) is a general-purpose processor. It handles a wide range of tasks well, including running the operating system and ordinary program logic. A GPU has many smaller processing units suited to parallel calculations. The two processors work together; using a GPU does not replace the CPU.

## Why I need a GPU for AI

Small lessons and experiments can run on a CPU. As models and datasets grow, training involves many more calculations. A GPU can reduce the time for those calculations, making larger experiments and faster iteration practical. GPU memory, called **VRAM**, also limits how much model data can fit on the GPU at once.

I do not need a GPU for every lesson. My computer has Intel UHD Graphics 620, so it does not provide the NVIDIA CUDA GPU used by this lesson. I used Google Colab instead. Colab assigned a remote NVIDIA Tesla T4; the T4 is in Google's runtime, not inside my computer.

## Verifying the Colab GPU

In a Colab cell, `!nvidia-smi` showed:

- GPU: Tesla T4
- GPU memory: 15,360 MiB (about 15 GiB)
- CUDA driver support was available

PyTorch also confirmed that CUDA was available and identified the device as `Tesla T4`:

```python
import torch

print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
```

## CPU versus GPU benchmark

I multiplied two 5,000 × 5,000 matrices with PyTorch. The second run is the more useful comparison because the first GPU run can include startup overhead.

| Run | CPU | Tesla T4 | Speedup |
| --- | ---: | ---: | ---: |
| First | 1.988 s | 0.188 s | 11× |
| Second | 2.014 s | 0.088 s | 23× |

For this operation in this Colab session, the T4 completed the second run about 23 times faster than the CPU. This is one benchmark, not a guarantee that every program or model will be 23 times faster.

## Rough VRAM estimate

At 2 bytes per parameter, 15 GiB of VRAM corresponds to roughly 8 billion fp16 parameters **for model weights alone**. This is only a theoretical upper bound: training also needs memory for gradients, activations, optimizer state, and other data, so a model's practical training limit is much lower.

## Takeaway

GPUs speed up many of the parallel matrix and tensor calculations used in AI. My local computer has no NVIDIA GPU available to WSL, but Colab provided a T4 that I verified with both `nvidia-smi` and PyTorch. In my matrix multiplication benchmark, the T4 was 23× faster on the second run. CPU remains sufficient for many introductory lessons; I can use a cloud GPU when a lesson benefits from acceleration.
