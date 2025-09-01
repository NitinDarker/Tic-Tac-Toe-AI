# Tic Tac Toe AI

![Python](https://img.shields.io/badge/python-3.12-blue)
![Pygame](https://img.shields.io/badge/pygame-2.6-green)

This is a **Tic Tac Toe game with AI** built in Python using the **Minimax algorithm**. Play against the computer and see if you can beat it — spoiler: it’s really good! 😎

>  The game uses **Pygame** for the GUI.

## Features

- Play as **X** or **O** against the AI.
- AI uses **Minimax** to always make the optimal move.
- Interactive **GUI with Pygame**.
- Replayable game with “Play Again” option.

## Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/NitinDarker/Tic-Tac-Toe-AI.git

cd Tic-Tac-Toe-AI
```

### 2️⃣ Install dependencies
Make sure you have Python installed. Then install all dependencies:

```bash
pip install -r requirements.txt
```

**⚠️ Note:** If you don’t have pip, install it first → [pip installation guide](https://pip.pypa.io/en/stable/installation/)

## Running the Game

You can run the game directly with **Python** or create a standalone Executable file:

```bash
python runner.py
```

## Creating a Standalone Executable

Want a .exe (Windows) so you don’t need Python installed? Use PyInstaller:

![pygame](https://img.shields.io/badge/pyinstaller-6.15-violet)

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Build the executable

```bash
# Windows
pyinstaller --onefile --windowed --add-data "OpenSans-Regular.ttf;." runner.py


# Linux / WSL / Mac
pyinstaller --onefile --windowed --add-data "OpenSans-Regular.ttf:." runner.py
```

- --onefile → Creates a single executable.
- --windowed → Runs without opening a console window.
- --add-data → Includes the font file for the game.

### Step 3: Run the executable

- On Windows: dist/runner.exe
- On Linux/WSL: dist/runner

## How to Play

1. Launch the game.

2. Choose your player: X or O.

3. Click on the grid to place your move.

4. The AI will play its turn automatically.

5. Game ends when there’s a winner or a tie.

6. Click Play Again to restart.

## Screenshots

![Tic Tac Toe](assets/landing.png)

![Tic Tac Toe](assets/game.png)