# Phase 0, Lesson 10: Terminal & Shell

## Terminal and shell

The terminal is the interface where I type commands. The **shell** interprets and runs them. In my VS Code terminal, `echo $SHELL` printed:

```text
/bin/zsh
```

## Pipes and filtering command output

The pipe character `|` sends one command's standard output to the next command as input. I ran:

```bash
ls learning-artifacts/phase0 | sort
```

This listed the Phase 0 artifact folders in alphabetical text order. `lesson10-terminal-and-shell` appeared before `lesson1-Dev_env` because `sort` compares the names as text, not as lesson numbers.

I also created a small temporary log and extracted its loss values:

```bash
printf 'epoch 1 loss: 0.9\nepoch 2 loss: 0.5\n' > /tmp/train.log
cat /tmp/train.log | grep loss | awk '{print $NF}'
```

The output was `0.9 0.5`. `grep` kept lines containing `loss`; `awk` printed the last whitespace-separated field (`$NF`) from each matching line.

## Redirects and logs

These shell operators route command output:

| Operator | Meaning |
|---|---|
| `>` | Write standard output to a file, replacing its previous contents. |
| `>>` | Append standard output to a file. |
| `2>` | Write standard error to a file. |
| `2>&1` | Send standard error to the same destination as standard output. |

I tested combining output and errors with:

```bash
python -c 'import sys; print("normal"); print("problem", file=sys.stderr)' > /tmp/both.log 2>&1
cat /tmp/both.log
```

Both lines were captured. `problem` appeared before `normal` because redirected standard output was buffered while standard error appeared immediately; combined redirection does not always preserve the order in which the program issued writes.

## Background work and tmux

`nohup command > run.log 2>&1 &` can keep a command running after the terminal closes and send its output to a log file. You cannot reattach to its live terminal output.

`tmux` supports persistent sessions you can detach from and reattach to, and it can show several panes at once. Typical commands and shortcuts are:

```bash
tmux new -s training
# Ctrl+B, then " to split horizontally
# Ctrl+B, then % to split vertically
# Ctrl+B, then d to detach
tmux ls
tmux attach -t training
```

I checked `tmux -V`; the command was not found. This account does not have sudo access, so I could not install tmux or practice the live detach/reattach workflow.

## Checking disk space

I ran `df -h`. The root filesystem (`/`) had 233 GB total, 39 GB used, and **183 GB available** (18% used). Entries such as `/run` and `/dev/shm` were `tmpfs`, which is temporary memory-backed storage rather than additional persistent disk space.

## Remote commands and SSH port forwarding

These are common patterns for a remote GPU machine:

```bash
ssh user@gpu-box
scp results.csv user@gpu-box:~/results/
rsync -avz ./data/ user@gpu-box:~/data/
```

`ssh` opens a remote shell, `scp` copies files, and `rsync` synchronizes directories. I learned the syntax but did not connect to a remote host.

For a Jupyter server listening on remote port 8888, local port forwarding uses:

```bash
ssh -L 8888:localhost:8888 user@gpu-box
```

Then open `http://localhost:8888` in the local browser. The first port is local; the forwarded destination is port 8888 on the remote host.

## Practice record

- Identified Zsh and used `sort`, `grep`, and `awk` in a pipeline.
- Practiced output and error redirection and learned why combined streams may appear out of order due to buffering.
- Checked available disk space with `df -h`.
- Learned the difference between `nohup` and tmux, and the SSH commands for remote work and port forwarding.
- Lesson quiz score: **3/3**.
