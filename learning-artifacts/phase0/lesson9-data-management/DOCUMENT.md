# Phase 0, Lesson 9: Data Management

## Loading and caching a dataset

I installed Hugging Face's `datasets` and `huggingface_hub` packages in the Python environment used by my VS Code notebook. The terminal environment initially had no `pip`, so I bootstrapped it with `python -m ensurepip --upgrade`. The notebook first reported `ModuleNotFoundError`; running `%pip install datasets huggingface_hub` in a notebook cell installed the packages for that kernel. I restarted the kernel and reran the import.

I loaded the IMDB movie-review dataset:

```python
from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb")
print(dataset)
print(dataset["train"][0])
```

The first load downloaded and cached the data. The output showed:

| Split | Rows |
|---|---:|
| train | 25,000 |
| test | 25,000 |
| unsupervised | 50,000 |

Each example has `text` and `label` fields. The unauthenticated Hugging Face warning was informational: the public dataset loaded successfully, though unauthenticated requests can have lower rate limits. The local cache avoids downloading the same data again; Python still loads the cached data into the session.

## Reproducible train, validation, and test splits

I held the supplied test split aside and used a fixed seed to take 10% of the original training split for validation:

```python
splits = dataset["train"].train_test_split(test_size=0.1, seed=42)

train_ds = splits["train"]
val_ds = splits["test"]
test_ds = dataset["test"]

print(len(train_ds), len(val_ds), len(test_ds))
```

The counts were:

```text
22500 2500 25000
```

I split the same source again with `seed=42` and compared its first validation example with the first split. The comparison printed `True`, confirming that this split was repeatable.

- **Train** data is used to fit the model.
- **Validation** data is used to check progress and tune choices during development.
- **Test** data is kept for final evaluation on examples not used to fit or tune the model.

## Comparing storage formats

I converted 100 IMDB training examples to CSV, JSON, and Parquet in a temporary directory, so the files did not remain in the repository. Their measured sizes were:

| Format | Size for this 100-example sample | Notes |
|---|---:|---|
| CSV | 136,031 bytes | Human-readable and widely supported; can be larger and slower to scan. |
| JSON | 138,291 bytes | Useful for APIs and nested records; can be verbose. |
| Parquet | 90,441 bytes | Columnar format; often compact and efficient for analytics. |

These measurements are for this sample and do not guarantee the same size relationship for every dataset. Hugging Face `datasets` uses Apache Arrow internally for efficient in-memory data.

## Streaming a large dataset

I requested Wikipedia with streaming enabled and printed the first five article titles:

```python
wiki = load_dataset(
    "wikimedia/wikipedia",
    "20231101.en",
    split="train",
    streaming=True,
)

for i, row in enumerate(wiki):
    print(row["title"])
    if i == 4:
        break
```

The titles printed were `Anarchism`, `Albedo`, `A`, `Alabama`, and `Achilles`.

`streaming=True` returns rows on demand without downloading the entire dataset first. It is useful when a dataset is too large to fit on local disk or when I only need to inspect or process a portion. **Review reminder:** streaming yields examples as needed; it does not download the whole dataset before iteration.

## Keep large files out of Git

Downloaded datasets and model weights should generally not be committed as ordinary Git files. Choose a method based on the goal:

- **`.gitignore`**: keep local, re-downloadable files out of Git. The repository already ignores common PyTorch weight extensions such as `.pt`, `.pth`, and `.safetensors`.
- **Git LFS**: version and share large files using Git LFS pointers.
- **DVC**: version datasets and model artifacts through small pointer files in Git and store the data in a remote backend, supporting repeatable experiments across machines.

Avoid broad patterns such as ignoring every CSV or Parquet file unless that is intended for the repository; small sample data may be useful to commit.

## Practice record

- Loaded IMDB with Hugging Face `datasets`, inspected its splits and first example, and used its local cache.
- Made a repeatable train/validation split with `seed=42`, kept the supplied test set, and verified the repeated split matched.
- Compared CSV, JSON, and Parquet file sizes for 100 examples.
- Streamed five Wikipedia article titles.
- Lesson quiz score: **2/3**. Review the exact behavior of `streaming=True`.
