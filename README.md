# Simple Snake Game

## Overview

This is a classic Snake Game built using Python's `pygame` library. The player controls a snake to collect food (orange circles), and with each food item consumed, the snake grows in length. The game ends if the snake hits the borders of the window or collides with itself. The game also features particle effects when the snake eats food and a gradient effect on the snake's body for extra visual flair.

## Features

- **Dynamic Particle Effects**: When the snake eats food, random particles are generated, creating a visually pleasing explosion effect.
- **Gradient Snake Body**: The snake's body color changes gradually from one end to the other, adding a cool visual gradient effect.
- **Score Display**: The player's score, based on the number of food items collected, is displayed in real-time on the screen.
- **Game Over Animation**: A smooth fade-in animation appears when the player loses.

## Requirements

- **Python 3.x**: Make sure you have Python 3.x installed.
- **pygame**: Install the `pygame` library using the following command:
  ```bash
  pip install pygame
  ```

## How to Play

1. **Movement**: Use the arrow keys (`UP`, `DOWN`, `LEFT`, `RIGHT`) to move the snake.
2. **Objective**: Collect the food that randomly appears on the screen. Each time the snake eats, it grows in size.
3. **Game Over**: The game ends if the snake collides with the boundaries of the screen or its own body.
4. **Restart or Quit**: After a game over, press `C` to play again or `Q` to quit the game.

## Controls

- `UP`: Move snake upward.
- `DOWN`: Move snake downward.
- `LEFT`: Move snake to the left.
- `RIGHT`: Move snake to the right.
- `C`: Restart the game after losing.
- `Q`: Quit the game after losing.

## File Structure

- `game.py`: The main script file that contains all the code for running the game.

## Running the Game

To start the game, simply run the Python script:

```bash
python game.py
```

Enjoy the game!
