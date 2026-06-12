# Django Day 01

## Getting Started

### Prerequisites

Ensure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed on your machine.

### Option 1: Run using Docker Compose

1. Clone or navigate to the directory:
   ```bash
   cd Django-Lab-01
   ```
2. Build and start the container:
   ```bash
   docker compose up --build
   ```
3. Open your browser and navigate to [http://localhost:8000/](http://localhost:8000/).

*Note: Database migrations will automatically run inside the container when it starts.*

### Option 2: Run in VS Code Dev Container

1. Open the `Django-Lab-01` directory in VS Code.
2. If you have the **Dev Containers** extension installed, VS Code will prompt you to *Reopen in Container*.
3. Alternatively, press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac), type `Dev Containers: Rebuild and Reopen in Container`, and select it.
4. VS Code will spin up the environment and perform migrations automatically.