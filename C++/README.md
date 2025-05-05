<!--- README file --->

# Project Title
battleShip.cpp

Battleship Game in C++.
This is a simple console-based Battleship game implemented in C++. 
The game randomly places ships on a 4x4 grid for both the player and the bot. 
The player and the bot take turns to guess the locations of the opponent's ships.

## Table of Contents
- [Features]
- [HowToCompileAndRun]
- [HowToPlay]
- [ProjectStructure]
- [Notes]
- [License]

## Features
- Random placement of ships on a 4x4 grid.
- Player inputs coordinates to attack the bot's ships.
- Bot randomly selects coordinates to attack player's ships.
- Tracks hits, misses, and number of turns.
- Maximum allowed misses before game over.
- Input validation to avoid repeated and invalid attacks.
- Clear feedback on hits and misses.
- Victory or defeat messages based on game outcome.

## How to Compile and Run
1. Make sure you have a C++ compiler installed (e.g., `g++`).

2. Compile the `battleship.cpp` file:
    g++ -o battleship battleship.cpp

3. Run the executable:
    ./battleship

## How to Play
- When prompted, enter a row and column number between 0 and 3 to attack that position on the bot's board.
- The game will notify you if you hit or miss a ship.
- The bot will then make its move.
- The game continues until all ships of one side are sunk or either player exceeds the maximum allowed misses.

## Project Structure
- `battleship.cpp`: The main source code file containing the game logic.

## Notes
- The bot's moves are random and may repeat previously attacked positions.
- You can uncomment the displayBoard calls in the code for debugging purposes to view ship placements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.
---
Enjoy playing Battleship!