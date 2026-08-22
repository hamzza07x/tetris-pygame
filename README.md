# 🎮 Tetris — Python & Pygame

A modular **Tetris clone built from scratch with Python and Pygame**.

The project uses an object-oriented structure to separate the game logic, tetrominoes, blocks, timers, score interface, preview interface, and configuration. It currently supports falling pieces, horizontal movement, collision detection, piece locking, and completed-row removal.

---

## ✨ Features

### Gameplay

* ✅ 10 × 20 Tetris playfield
* ✅ Random tetromino generation
* ✅ All 7 standard tetromino shapes
* ✅ Automatic vertical piece movement
* ✅ Left/right player movement
* ✅ Horizontal collision detection
* ✅ Vertical collision detection
* ✅ Piece locking when reaching the bottom or another block
* ✅ Internal field/grid data tracking
* ✅ Completed row detection
* ✅ Completed row removal
* ✅ Blocks above cleared rows automatically move downward

### Architecture

* ✅ Object-oriented game structure
* ✅ Separate `Game`, `Tetromino`, and `Block` classes
* ✅ Custom reusable timer system
* ✅ Sprite-based block rendering
* ✅ Centralized game configuration
* ✅ Separate preview and score UI components

### UI

* ✅ 10 × 20 game grid
* ✅ Sidebar layout
* ✅ Preview panel
* ✅ Score panel
* ✅ Configurable colors and dimensions

---

## 🛠️ Built With

* **Python 3**
* **Pygame**

---

## 📂 Project Structure

```text
tetris-pygame/
│
├── main.py          # Application entry point and main game loop
├── game.py          # Core gameplay, tetrominoes, blocks, movement & collisions
├── settings.py      # Game dimensions, colors, shapes and configuration
├── timer.py         # Custom timer implementation
├── preview.py       # Next-piece preview panel
├── score.py         # Score panel
│
└── README.md        # Project documentation
```

---

## 🧩 Code Architecture

### `main.py`

The entry point of the application.

It initializes Pygame, creates the display, and coordinates the main game loop and UI components.

The main loop handles:

* Window events
* Game updates
* Rendering
* Display updates
* Game timing

---

### `game.py`

Contains the core Tetris gameplay.

The `Game` class manages:

* The playfield
* Sprite groups
* Field data
* Tetromino generation
* Timers
* Player input
* Row clearing

The game maintains a 2D `fieldData` array to keep track of occupied cells.

The project also checks completed rows, removes their blocks, updates the field data, and moves remaining blocks downward.

---

### `Tetromino`

Represents the currently falling Tetris piece.

Each tetromino consists of four `Block` sprites and supports:

* Horizontal movement
* Vertical movement
* Collision detection
* Piece locking

The movement system checks the next position before moving the piece.

---

### `Block`

Represents an individual square of a tetromino.

Each block is implemented as a Pygame sprite and contains its own position, image, and collision logic.

---

### `timer.py`

Provides a reusable timer class for timed gameplay events.

The timer system is currently used for automatic vertical movement and horizontal movement delay.

---

### `preview.py`

Provides the sidebar preview area for the upcoming tetromino.

---

### `score.py`

Provides the sidebar area dedicated to displaying the player's score.

---

## 🎮 Controls

| Key   | Action                                         |
| ----- | ---------------------------------------------- |
| `←`   | Move piece left                                |
| `→`   | Move piece right                               |
| `↓`   | Automatic falling is handled by the game timer |
| `ESC` | Not currently implemented                      |

> Additional controls such as rotation, hard drop, and soft drop are planned for future versions.

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

* [x] Tetromino generation
* [x] Automatic piece falling
* [x] Horizontal movement
* [x] Collision detection
* [x] Piece locking
* [x] Field tracking
* [x] Line detection
* [x] Line clearing
* [ ] Tetromino rotation
* [ ] Rotation collision handling
* [ ] Hard drop
* [ ] Soft drop
* [ ] Ghost piece
* [ ] Game over detection
* [ ] Pause functionality
* [ ] Hold piece
* [ ] Next-piece preview functionality

### Scoring

* [ ] Score display
* [ ] Line-clear scoring
* [ ] Combo system
* [ ] Level system
* [ ] Increasing fall speed
* [ ] High-score system

### UI & Audio

* [ ] Improved score panel
* [ ] Functional next-piece preview
* [ ] Start menu
* [ ] Pause menu
* [ ] Game-over screen
* [ ] Sound effects
* [ ] Background music
* [ ] Visual effects

---

## 📸 Screenshots

Add screenshots of the game here.

Example:

```markdown
![Tetris Gameplay](screenshots/gameplay.png)
```

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

## 📌 Current Status

**In Development 🚧**

The core falling-piece and grid systems are implemented, including movement, collision detection, piece locking, and line clearing.

Rotation, advanced scoring, game-over handling, and several UI/gameplay features are still being developed.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Muhammad Hamza**

Built with Python 🐍 and Pygame 🎮

---

⭐ If you find this project useful or interesting, consider giving the repository a star!
