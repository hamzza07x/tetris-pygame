# 🎮 Tetris — Python & Pygame

A modular **Tetris clone built from scratch with Python and Pygame**.

This project uses an object-oriented structure to separate the game logic, tetrominoes, blocks, timers, score interface, preview interface, and configuration. The core loop is now complete end-to-end: falling pieces, movement, rotation, soft/hard drop, a ghost piece, collision detection, piece locking, line clearing, scoring, leveling, pause, and game over with restart.

---

## ✨ Features

### Gameplay

* ✅ 10 × 20 Tetris playfield
* ✅ All 7 standard tetromino shapes
* ✅ 7-bag randomizer — every shape appears exactly once every 7 pieces (no droughts or streaks)
* ✅ Automatic vertical piece movement, speeding up every level
* ✅ Left / right movement
* ✅ Rotation, pivot-based (no wall kicks yet — see Roadmap)
* ✅ Soft drop (hold `↓`) and hard drop (`Space`)
* ✅ Ghost piece — shows where the piece will land
* ✅ Horizontal and vertical collision detection
* ✅ Piece locking, correctly handling pieces that lock while still partially above row 0
* ✅ Internal field/grid data tracking
* ✅ Completed row detection and clearing; blocks above shift down
* ✅ Game over detection, with restart
* ✅ Pause / resume

### Scoring

* ✅ Score, level, and lines-cleared display
* ✅ Line-clear scoring (single / double / triple / tetris, scaled by level)
* ✅ Soft-drop and hard-drop point bonuses
* ✅ Level-based fall-speed increase every 10 lines

### Architecture

* ✅ Object-oriented game structure
* ✅ Separate `Game`, `Tetromino`, and `Block` classes
* ✅ Custom reusable timer system, pause-aware
* ✅ Sprite-based block rendering
* ✅ Centralized game configuration
* ✅ Separate preview and score UI components

### UI

* ✅ 10 × 20 game grid
* ✅ Sidebar layout
* ✅ Preview panel (next 3 pieces)
* ✅ Score panel
* ✅ Pause overlay
* ✅ Game-over overlay
* ✅ Configurable colors and dimensions

---

## 🩹 Recent Fixes

* **Collision check indexed the field with a negative number.** Every piece spawns above row 0 (`pos.y` starts negative). `horizontalCollide` didn't guard against that, so Python's negative-index wraparound made it check the *bottom* row of the field instead of skipping the check — pieces near the top could get silently blocked by whatever was filled near the bottom.
* **Same bug on write, not just read.** A piece locking while still partially above row 0 used to write into `fieldData` with that same negative index, corrupting the bottom row instead of ending the game. This is also why there was no working game-over state — the condition that should have ended the game was silently corrupting data instead.
* **Line-clear scoring gave the same points for a triple as a double** (`scoreData[2] == scoreData[3] == 300`). Now strictly increasing: 100 / 300 / 500 / 1200.
* **L and Z pieces were the same color** (both `red`), hard to tell apart at a glance. L now has its own orange.

---

## 🛠️ Built With

* **Python 3**
* **Pygame**

---

## 📂 Project Structure

```text
tetris-pygame/
│
├── main.py        # Application entry point and main game loop
├── game.py        # Core gameplay loop, field state, pause/game-over, scoring
├── tetromino.py    # Falling piece: movement, rotation, hard drop, locking
├── block.py        # A single tetromino square: image, position, collision
├── settings.py     # Game dimensions, colors, shapes, and configuration
├── timer.py        # Custom timer implementation, pause-aware
├── preview.py      # Next-piece preview panel
├── score.py        # Score panel
│
└── README.md       # Project documentation
```

---

## 🧩 Code Architecture

### `main.py`

The entry point of the application. Initializes Pygame, creates the display, runs the 7-bag shape queue, and coordinates the main loop.

The main loop handles:

* Window and keyboard events — movement is polled every frame; hard drop, pause, and restart are handled as discrete key-press events
* Game, score, and preview updates
* Rendering and display updates
* Game timing
* Restarting after game over

---

### `game.py`

Contains the core Tetris gameplay. The `Game` class manages:

* The playfield and sprite group
* Field data (`fieldData`)
* Tetromino spawning, via a callback passed into `Tetromino`
* Timers, including pausing them without losing their progress
* Player input
* Row clearing and scoring
* The ghost piece and the pause / game-over overlays

The game maintains a 2D `fieldData` array to track occupied cells. Completed rows are detected, their blocks removed, the field data updated, and remaining blocks shifted downward.

---

### `tetromino.py`

Represents the currently falling piece. Each tetromino consists of four `Block` sprites and supports:

* Horizontal and vertical movement
* Rotation, with pivot-based collision checking
* Locking into the field — including detecting when a piece locks while still above row 0 (game over)
* Hard drop and ghost-piece drop-distance calculation

---

### `block.py`

Represents a single square of a tetromino. Each block is a Pygame sprite with its own:

* Position
* Image
* Horizontal and vertical collision logic
* Rendering rectangle

---

### `settings.py`

Centralizes configuration: grid dimensions, window layout, colors, the 7 tetromino shapes and their spawn offsets, scoring values, and gameplay timings.

---

### `timer.py`

A reusable timer class used for automatic vertical movement and the horizontal-move / rotation input delay. `Game` shifts a timer's internal clock forward when resuming from pause, so nothing "catches up" instantly.

---

### `preview.py`

Displays the next 3 upcoming pieces in the sidebar.

---

### `score.py`

Displays score, level, and lines cleared in the sidebar.

---

## 🎮 Controls

| Key             | Action                     |
| --------------- | -------------------------- |
| `←`             | Move piece left             |
| `→`             | Move piece right             |
| `↑`             | Rotate                        |
| `↓` (hold)      | Soft drop (+1 pt per row)      |
| `Space`         | Hard drop (+2 pts per row)      |
| `P` / `Esc`     | Pause / resume                   |
| `Enter` / `R`   | Restart (after game over)         |

> Hold piece and wall-kick rotation aren't implemented yet — see Roadmap.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/tetris-pygame.git
```

### 2. Enter the project directory

```bash
cd tetris-pygame
```

### 3. Install Pygame

```bash
pip install pygame
```

### 4. Run the game

```bash
python main.py
```

---

## 🖥️ Requirements

* Python **3.x**
* Pygame
* Windows, Linux, or macOS

---

## 🚧 Roadmap

The project is still under development.

### Gameplay

* [x] Tetromino generation (7-bag)
* [x] Automatic piece falling
* [x] Horizontal movement
* [x] Rotation
* [x] Rotation collision handling
* [x] Hard drop
* [x] Soft drop
* [x] Ghost piece
* [x] Collision detection
* [x] Piece locking
* [x] Field tracking
* [x] Line detection
* [x] Line clearing
* [x] Game over detection
* [x] Pause functionality
* [x] Functional next-piece preview
* [ ] Hold piece
* [ ] Wall kicks (SRS-style rotation nudging near walls/stacks)

### Scoring

* [x] Score display
* [x] Line-clear scoring
* [x] Level system
* [x] Increasing fall speed
* [x] Soft-drop / hard-drop bonuses
* [ ] Combo / back-to-back bonus system
* [ ] High-score persistence

### UI & Audio

* [x] Pause overlay
* [x] Game-over screen
* [ ] Start menu
* [ ] Sound effects
* [ ] Background music
* [ ] Visual effects (animations, particles)

---

## 📸 Screenshots

Add screenshots of the game here.

For example:

## 📸 Screenshots

<p align="center">
  <img src="ss/ss%201.png" width="30%" alt="Tetris Gameplay 1">
  <img src="ss/ss%202.png" width="30%" alt="Tetris Gameplay 2">
  <img src="ss/ss%203.png" width="30%" alt="Tetris Gameplay 3">
</p>

---

## 🎯 Project Goals

This project was created to practice and demonstrate:

* Object-oriented programming with Python
* Game development fundamentals
* Pygame
* Sprite-based rendering
* Collision detection
* Game state management
* Timers and event-driven systems
* 2D grid-based game logic
* Modular software architecture

---

## 📚 Reference & Learning Resource

This project was developed while following and learning from the following YouTube playlist:

### Tetris Tutorial — Clear Code

🔗 [YouTube Playlist](https://youtube.com/playlist?list=PL4cUxeGkcC9iurLoO9Mu7GqsKlxEXcf8m&si=NnT9XQc5QlNz_760&utm_source=chatgpt.com)

The playlist was used as a reference for understanding the architecture and implementation of a Tetris game using Python and Pygame.

The project is being developed as a learning exercise, with the codebase being extended and adapted as development continues.

**Credit:** Clear Code

---

## 📌 Current Status

**In Development 🚧**

The core game loop is complete and playable end-to-end:

* Tetromino generation (7-bag), falling, movement, and rotation
* Soft drop, hard drop, and ghost piece
* Collision detection and piece locking, including correct handling at the top of the field
* Line detection, clearing, and scoring with levels and increasing speed
* Pause / resume
* Game over detection and restart

Still missing: hold piece, wall-kick rotation, a combo scoring system, high-score persistence, menus, and audio.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Muhammad Hamza**

Built with 🐍 **Python** and 🎮 **Pygame**

---

⭐ If you find this project useful or interesting, consider giving the repository a star!
