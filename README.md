# 🎮 Tetris (Python + Pygame)

A modular implementation of the classic **Tetris** game built with **Python** and **Pygame**.

This project focuses on clean architecture, object-oriented programming, and maintainable game development practices rather than simply recreating the game.

---

## Features

- ✅ Modular project structure
- ✅ Object-oriented architecture
- ✅ Sprite-based rendering
- ✅ Timer-driven game loop
- ✅ Random tetromino generation
- ✅ Grid rendering
- ✅ Preview panel (UI)
- ✅ Score panel (UI)
- 🚧 Collision detection (In Progress)
- 🚧 Line clearing
- 🚧 Rotation system
- 🚧 Scoring
- 🚧 Hold piece
- 🚧 Game over detection

---

## Project Structure

```
.
├── main.py          # Main game loop
├── game.py          # Core gameplay logic
├── settings.py      # Constants and configuration
├── timer.py         # Custom timer system
├── preview.py       # Next piece preview UI
├── score.py         # Score UI
```

---

## Requirements

- Python 3.10+
- Pygame

Install dependencies:

```bash
pip install pygame
```

---

## Running the Game

```bash
python main.py
```

---

## Architecture

The project is separated into multiple components:

- **Main** → Handles initialization and game loop.
- **Game** → Core gameplay mechanics.
- **Tetromino** → Piece management.
- **Block** → Individual block sprites.
- **Timer** → Handles timed events like automatic falling.
- **Preview** → Sidebar preview panel.
- **Score** → Score display panel.

This modular design makes the project easier to extend with new gameplay mechanics.

---

## Roadmap

- [ ] Collision detection
- [ ] Piece locking
- [ ] Line clearing
- [ ] Score system
- [ ] Level progression
- [ ] Rotation (SRS)
- [ ] Hard drop
- [ ] Soft drop
- [ ] Ghost piece
- [ ] Hold piece
- [ ] Pause menu
- [ ] Sound effects
- [ ] High score saving

---

## Built With

- Python
- Pygame

---

## Screenshots

_Add gameplay screenshots here._

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

Inspired by the classic **Tetris** game and built as a learning project to explore game development with Python and Pygame.
