# Phase 0, Lesson 11: Linux for AI

## Linux paths and navigation

Linux uses one filesystem rooted at `/`. The tilde `~` is a shortcut for the current user's home directory. I ran `echo ~` and got `/home/recoding`; `pwd` showed my working directory:

```text
/home/recoding/ai-engineering-journey
```

The repository is inside my home directory, so its path can be written as `~/ai-engineering-journey`.

## File permissions

I created a small shell script in `/tmp` and checked it with `ls -l`:

```bash
printf '#!/bin/sh\necho "Hello from Linux"\n' > /tmp/hello.sh
ls -l /tmp/hello.sh
```

The mode was:

```text
-rw-rw-r--
```

The file had read and write permissions but no execute (`x`) permission. I added execute permission for its owner and ran it:

```bash
chmod u+x /tmp/hello.sh
/tmp/hello.sh
```

It printed `Hello from Linux`. `chmod` changes permission bits. `chown` changes file ownership and usually requires administrator access. A Docker socket permission error is a separate access-control issue; making a script executable does not grant access to `/var/run/docker.sock`.

## System packages and Python packages

Ubuntu uses `apt` for system-level packages such as `tmux` and `htop`. Installing or changing system packages requires administrator access, normally through `sudo apt install ...`. My account is not in the sudoers file, so I cannot install those packages myself.

Python libraries belong in a project virtual environment, installed with that environment's Python and `pip`. System package installation and project package installation are separate tasks.

## Check disk space and directory sizes

`df -h` reports filesystem capacity and free space. My root filesystem showed:

| Total | Used | Available | Used percent |
|---:|---:|---:|---:|
| 233 GB | 39 GB | 183 GB | 18% |

`du` reports the amount of space used by directories. I checked the Hugging Face cache:

```bash
du -sh ~/.cache/huggingface
```

It reported **208 MB**. A size listing of my home directory showed about **3.5 GB** in `.cache` overall; the Hugging Face cache is one part of that total. Other large directories included `ai` (2.0 GB), `.vscode` (1.7 GB), and `.config` (1.4 GB).

## Linux and macOS command differences

Linux commonly uses GNU `sed`; macOS uses BSD `sed`. For in-place substitution, the forms differ:

```bash
# Linux
sed -i 's/old/new/' file.txt

# macOS
sed -i '' 's/old/new/' file.txt
```

This matters when shell scripts move between operating systems.

## Practice record

- Resolved `~` to `/home/recoding` and used `pwd` to identify the current directory.
- Read the permission string from `ls -l`, added the owner execute bit with `chmod u+x`, and ran the temporary script.
- Distinguished disk capacity (`df`) from directory size (`du`).
- Learned why `apt` requires administrator access and how Linux `sed -i` syntax differs from macOS.
- Lesson quiz score: **3/3**.
