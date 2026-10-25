# Phase 0, Lesson 7: Docker for AI

## What Docker is

Docker packages an application's code, runtime, system libraries, and Python packages into an **image**. Starting that image creates a **container**: an isolated running process with its own filesystem and network settings. A container shares the host operating system's kernel, unlike a virtual machine, which runs a full guest operating system.

| Term | Meaning |
|---|---|
| Dockerfile | Build instructions for an image. |
| Image | A reusable, mostly read-only template built from a Dockerfile. |
| Container | A running instance of an image, with a small writable layer. |
| Volume mount | A host folder or Docker-managed volume made available inside a container. |
| Docker Compose | A way to define and run a group of related containers from YAML. |

Docker helps AI projects run with a consistent Python version and package set across development machines and servers. It is useful when an AI stack has packages, CUDA libraries, or system dependencies that are difficult to keep aligned by hand.

## Build a basic Python image

For a CPU-only example, create a `Dockerfile` in a Python project. If the project has a `requirements.txt`, it could contain:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

- `FROM` selects the starting image. `slim` is a smaller base with fewer system tools preinstalled.
- `WORKDIR` sets the working directory inside the image.
- `COPY` places project files in the image.
- `RUN` executes a command while building the image.
- `CMD` sets the default command when a container starts.

Copying and installing `requirements.txt` before copying the rest of the code lets Docker reuse the dependency layer when only application code changes. Docker caches unchanged layers to speed up rebuilds.

Build and run it from the directory containing the Dockerfile:

```bash
docker build -t my-ai-app .
docker run --rm my-ai-app
```

`--rm` removes the stopped container. The image remains available for another run.

## Keep local files out of the image

A `.dockerignore` file prevents local environments, secrets, and other unnecessary files from being sent to the build context. For example:

```text
.git
.venv
__pycache__
*.py[cod]
.env
.ipynb_checkpoints
```

Do not put API keys into the Dockerfile or image. Pass secrets at runtime using an appropriate secret manager or environment configuration, and keep secret files out of the build context.

## Persist code, models, and data with volumes

Files written only inside a container's writable layer disappear when that container is removed. Mount host folders or named volumes for files that should persist.

```bash
docker run --rm \
  -v "$PWD:/workspace" \
  -v "$HOME/models:/models" \
  -w /workspace \
  my-ai-app python app.py
```

This maps the current host folder to `/workspace` and the host `models` folder to `/models` inside the container. The model files remain on the host when the container is removed or rebuilt.

## GPU access for AI containers

A CUDA image can include the CUDA toolkit and AI libraries, but the host provides the NVIDIA driver. On supported Linux hosts, the NVIDIA Container Toolkit allows Docker to expose the host GPU to a container:

```bash
docker run --rm --gpus all my-ai-gpu-app
```

The host needs a compatible NVIDIA GPU, driver, Docker setup, and NVIDIA Container Toolkit. A CUDA-enabled image by itself does not create GPU access. CPU containers remain useful without an NVIDIA GPU. My local machine has Intel UHD 620 graphics, so it cannot provide an NVIDIA CUDA GPU; I previously used a Tesla T4 through Colab.

## Run related services with Docker Compose

An AI application may need an app container and a vector database. Compose defines both services and creates a shared network. Services can reach each other by service name.

```yaml
services:
  ai-dev:
    build: .
    working_dir: /workspace
    volumes:
      - .:/workspace
      - ${HOME}/models:/models
  qdrant:
    image: qdrant/qdrant:v1.12.5
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

volumes:
  qdrant_data:
```

From the directory containing `compose.yaml`, use:

```bash
docker compose up -d
docker compose ps
docker compose down
```

The `ai-dev` service can connect to Qdrant at `http://qdrant:6333` because Compose provides service-name DNS on its shared network. The named `qdrant_data` volume preserves the database data. `docker compose down -v` also removes named volumes, so use it only when you intend to delete that persisted data.

## Useful commands

```bash
docker --version        # show the Docker CLI version
docker ps               # list running containers
docker images           # list local images
docker logs <container> # view a container's logs
docker exec -it <container> sh  # open a shell in a running container
```

## Practice record and current limitation

- `docker --version` succeeded and reported Docker `28.2.2`.
- `docker run --rm hello-world` did not run: account `recoding` was denied access to `/var/run/docker.sock`.
- `sudo` is unavailable to this account because it is not in the sudoers file. Therefore, I did not build or run a container during this lesson.
- An administrator must configure Docker access before the hands-on build and run commands can be verified. Docker group membership grants powerful control over the host, so access should follow the machine administrator's policy.
- Lesson quiz score: **3/3**.
