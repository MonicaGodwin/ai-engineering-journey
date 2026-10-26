# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission
I am learning AI to understand AI. By the end, I am not sure yet what I want to build.

## Placement
- Date: 2026-10-23
- Score: 3/10 (Math & Statistics: 1/2; Classical ML: 0/2; Deep Learning: 0/2; NLP & Transformers: 0/2; Applied AI: 2/2)
- Entry point: Phase 0: Setup & Tooling
- Pace: As fast as possible

## Path
| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Do | -- |
| 1 | Math Foundations | Review | 23 |
| 2 | ML Fundamentals | Do | 26 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP — Foundations to Advanced | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 19 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 76 |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 34 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-10-23 | 00/01 | 1/3 | Completed the environment check (2/2 required), installed and verified CPU-only PyTorch (2.14.1+cpu; CUDA unavailable as expected), and ran hello-world examples in Python, TypeScript, Rust, and Julia. Recalled the four-layer order; review the PyTorch GPU availability check. |
| 2026-10-23 | 00/02 | 3/3 | Verified checkpoint ignore patterns with `git check-ignore` and inspected Phase 0 commit history. Explain the branch workflow; still practice creating a branch, committing, and pushing. |
| 2026-10-24 | 00/02 follow-up | — | Pulled remote updates on the personal system and resolved the `LEARNING.md` stash conflict. `main` now matches `origin/main`; branch, commit, and push practice remains. |
| 2026-10-24 | 00/03 | — | Verified a Colab Tesla T4 with `nvidia-smi` and PyTorch (`torch.cuda.is_available()` is True). For a 5,000 × 5,000 matrix multiplication, the second run was CPU 2.014 s vs T4 0.088 s (23×). Local Intel UHD 620 has no NVIDIA CUDA GPU. Notes: `learning-artifacts/phase0/lesson3-GPU-Setup-and-cloud/DOCUMENT.md`. |
| 2026-10-24 | 00/04 (in progress) | — | Learned that API keys authenticate requests and must stay out of source control. Added `.env` to `.gitignore`. No API key or request yet; Anthropic API use requires prepaid credits. |
| 2026-10-24 | 00/04 | 2/3 | Wrote the SDK and raw HTTP exercise and verified syntax and dry-run mode. Explain key and request body; review the Anthropic raw HTTP key header. Live API calls remain pending until credits are available. |
| 2026-10-24 | 00/05 | 3/3 | Created a VS Code notebook with Python venv; used Markdown, `%timeit`, and `%%time`, corrected a cell error, and verified Restart and Run All. |
| 2026-10-24 | 00/06 | 1/3 | Activated the repo `.venv` in VS Code and learned why environments and lockfiles matter; review how to check the active interpreter and diagnose PyTorch CUDA/driver mismatches. |
| 2026-10-25 | 00/07 | 3/3 | Learned Docker images, containers, build layers, volume mounts, GPU exposure, and Compose service networking. `docker --version` works, but running containers is blocked because account `recoding` lacks Docker socket and sudo access. |
| 2026-10-25 | 00/08 | 3/3 | Configured VS Code type checking, notebook output scrolling, and Black format-on-save; verified formatting and a Pylance type warning. Remote SSH was explained but not connected to a host. |
| 2026-10-25 | 00/09 | 2/3 | Loaded and cached IMDB with Hugging Face `datasets`, made reproducible train/validation/test splits (22,500/2,500/25,000), compared CSV/JSON/Parquet, and streamed five Wikipedia titles. Review what `streaming=True` does. |
| 2026-10-26 | 00/10 | 3/3 | Identified Zsh, practiced pipelines, log filtering and redirection, checked disk space (183 GB available), and learned SSH port forwarding. tmux is not installed, so its detach/reattach workflow was discussed but not run. |
| 2026-10-26 | 00/11 | 3/3 | Practiced Linux home/path navigation, added execute permission to a temporary script, checked disk usage (`~/.cache` 3.5 GB; Hugging Face cache 208 MB), and reviewed apt/sudo and macOS/Linux `sed` differences. |

## Review queue
- Phase 0, Lesson 4: Review that Anthropic sends the API key in the `x-api-key` header.
- Phase 0, Lesson 6: Review checking the active Python interpreter (`which python`/`where python`) and that CUDA availability can fail when the installed PyTorch CUDA build is incompatible with the GPU driver.
- Phase 0, Lesson 9: Review that `streaming=True` yields dataset rows on demand without downloading the entire dataset first.
