<!--- README file --->

# Project Title
Pong game

This project is a simple implementation of the classic Pong game using Python and the Pygame library. 
The game features a player-controlled bar that must catch a bouncing ball while avoiding letting it fall off the screen. 
Players can also interact with bricks and portals that add additional gameplay elements.

## Table of Contents
- [Features]
- [Requirements]
- [Installation]
- [HowToPlay]
- [GameControls]
- [CodeStructure]
- [Customization]
- [Acknowledgments]
- [Notes]
- [License]

## Features
- **Player Input**: Players can enter their names and control the bar using the left and right arrow keys.
- **Scoring System**: Players earn points by hitting bricks and can see their scores displayed on the screen.
- **High Scores**: The game keeps track of the top scores and allows players to view them.
- **Sound Effects**: Sound effects are played when the ball hits the bar or the edges of the screen.
- **Dynamic Gameplay**: The game includes portals that randomly reposition the ball and bricks that add complexity to the gameplay.

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Clone the repository or download the source code.
2. Install Pygame if you haven't already:
    pip install pygame
3. Ensure you have the necessary image and sound files in the correct directories

## How to Play
To start the game, run the main script:
    python Pong_play.py

### Game Controls
- **Left Arrow**: Move the bar left.
- **Right Arrow**: Move the bar right.
- **Space**: Start the game after entering your name.
- **Esc**: Quit the game.
- **r**: Restart the game after a game over.
- **h**: View high scores after a game over.
- **b**: Go back to previous page.
- **s**: Start new game from the High Scores page.
- **n**: Start a new game with a new player name after a game over.

## Code Structure
- **Pong_class_V2.py**: Contains the `Pong` class that handles the game logic, rendering, and player interactions.
- **Game_class.py**: Contains the `Game` class that provides the foundational structure for the game, including methods for saving/loading game state, handling events, and managing the game loop.

## Customization
You can customize various aspects of the game by modifying the parameters in the `Pong` class constructor. This includes changing the images, sounds, and gameplay mechanics.

## Acknowledgments
- The open-source community for resources and inspiration.

## Notes
- When pressing menu commands (e.g, "r", "b", "s"), there might be a slight delay before the input is processed. Please wait a moment before pressing the key again to avoid unintended behavior.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.
---
Enjoy playing Pong!

