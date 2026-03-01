# Dynamic Pathfinding Agent

A grid-based pathfinding visualiser built with Python and Tkinter that implements **Greedy Best-First Search (GBFS)** and **A\* Search** with real-time dynamic obstacle support and automatic re-planning.

## Features

- **Two search algorithms** — GBFS and A* selectable at runtime
- **Two heuristics** — Manhattan Distance and Euclidean Distance
- **Animated visualisation** — frontier (yellow), visited (blue), path (green), agent (purple)
- **Interactive map editor** — draw/erase walls, reposition start and goal by clicking
- **Random map generator** — adjustable obstacle density
- **Dynamic mode** — obstacles spawn randomly while the agent moves; if one blocks the current path the agent immediately re-plans from its current position without resetting the whole search
- **Metrics dashboard** — nodes visited, path cost, execution time, and status updated live

---

## Requirements

| Requirement | Version |
|-------------|---------|
| Python | 3.8 or higher |
| Tkinter | Included with Python |

> **No external libraries are needed.** Tkinter ships with the standard Python installer on Windows and macOS. On Linux you may need to install it separately (see below).

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/dynamic-pathfinding-agent.git
cd dynamic-pathfinding-agent
```

### 2. Check your Python version

```bash
python --version
# or
python3 --version
```

Python 3.8 or higher is required.

### 3. Install Tkinter (Linux only)

Tkinter is pre-installed on Windows and macOS. On Linux:

```bash
# Ubuntu / Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

---

## How to Run

```bash
python pathfinding_agent.py
# or
python3 pathfinding_agent.py
```

The GUI window will open immediately — no configuration needed.

---

## Controls

### Toolbar (top bar)

| Control | Options | Description |
|---------|---------|-------------|
| ALGORITHM | A* / GBFS | Choose the search strategy |
| HEURISTIC | Manhattan / Euclidean | Choose the distance heuristic |
| DRAW | Wall / Start / Goal / Erase | Sets what left-click places on the grid |
| DYNAMIC | ON checkbox | Enables random obstacle spawning during agent movement |

<img width="1412" height="61" alt="image" src="https://github.com/user-attachments/assets/17eee0ca-1321-449c-9f72-df85b1e45e90" />


### Buttons

| Button | Action |
|--------|--------|
| ▶ RUN | Runs the selected algorithm, animates exploration, then moves the agent |
| ■ STOP | Halts all animation and agent movement |
| ⟳ RANDOM MAP | Generates a new random maze at ~28% wall density |
| ✕ CLEAR | Removes all walls and resets the grid |

<img width="648" height="68" alt="image" src="https://github.com/user-attachments/assets/9576774c-88ea-43ff-b9f4-f3963d95f9ab" />

### Mouse

| Action | Effect |
|--------|--------|
| Left-click (Wall mode) | Place a wall; if it lands on the current path the agent re-plans instantly |
| Left-click drag | Paint walls continuously |
| Left-click (Start/Goal mode) | Move the start or goal marker |
| Left-click (Erase mode) | Remove a wall |
| Right-click | Erase a wall |

---

## Usage Walkthrough

1. **Run the program** — the grid appears with start (S) at top-left area and goal (G) at bottom-right area.
2. **Draw obstacles** — select *Wall* in the DRAW radio buttons and click/drag on the grid, or click **RANDOM MAP** for an instant maze.
3. **Choose algorithm and heuristic** — select from the top bar.
4. **Click RUN** — watch the search animate (yellow = frontier, blue = visited), then the green path appears and the agent (●) begins moving.
5. **Try Dynamic Mode** — tick the *DYNAMIC ON* checkbox before clicking RUN. While the agent moves, new walls spawn randomly. If one blocks the path, the agent detects it and re-plans immediately from its current position.
6. **Draw a wall mid-run** — even without dynamic mode enabled, drawing a wall on the green path while the agent is moving or after the path is shown will trigger an instant re-plan.

---

## Project Structure

```
dynamic-pathfinding-agent/
│
├── pathfinding_agent.py   # Complete source — all logic and UI in one file
└── README.md              # This file
```

---

## Algorithm Overview

### Greedy Best-First Search (GBFS)

Selects the next node purely by estimated distance to the goal:

```
f(n) = h(n)
```

Fast but not guaranteed to find the shortest path. Best for dynamic mode where re-planning speed matters.

<img width="1411" height="792" alt="image" src="https://github.com/user-attachments/assets/b167c236-979c-4452-8181-715f15ba9cb0" />


### A* Search

Balances actual cost from start with estimated cost to goal:

```
f(n) = g(n) + h(n)
```

Always finds the optimal (shortest) path when using an admissible heuristic. Explores more nodes than GBFS but guarantees correctness.

<img width="1417" height="832" alt="image" src="https://github.com/user-attachments/assets/e30f3d33-2c56-43f7-9a53-4ef1a038b669" />

### Heuristics

| Heuristic | Formula | Best for |
|-----------|---------|----------|
| Manhattan | `\|r1−r2\| + \|c1−c2\|` | 4-directional grids (this project) |
| Euclidean | `√((r1−r2)² + (c1−c2)²)` | Any grid / diagonal movement |

---

## Re-planning Logic

When a wall appears on the agent's remaining path (either placed manually or spawned dynamically):

1. The agent's movement is paused immediately.
2. The old path is cleared from the canvas.
3. The selected algorithm runs from the **agent's current cell** to the goal (no animation — result only).
4. The new path is drawn and the agent resumes.
5. If the wall does **not** fall on the remaining path, nothing happens — no wasted computation.

---
