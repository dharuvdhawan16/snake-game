# Snake Game Readme

This is a simple implementation of the classic Snake game using the Pygame library in Python. The game features a snake that moves around the screen, trying to eat randomly positioned fruits while avoiding collisions with the screen edges and itself.

## Prerequisites

Before running the game, make sure you have Python installed on your machine. Additionally, you need to install the Pygame library. You can install Pygame using the following command:

```bash
pip install pygame
```

## How to Play

1. Run the Python script using a terminal or command prompt:

   ```bash
   python snake_game.py
   ```

2. Use the arrow keys to control the snake's direction:
   - Up arrow: Move the snake upward
   - Down arrow: Move the snake downward
   - Left arrow: Move the snake to the left
   - Right arrow: Move the snake to the right

3. The goal of the game is to eat the red fruits that appear randomly on the screen. Each time the snake eats a fruit, it grows longer.

4. Avoid collisions with the screen edges and the snake's own body. If the snake collides with the edges or itself, the game ends.

5. Press the 'ESC' key to exit the game at any time.

## Game Elements

- **Snake:** The player controls a snake composed of linked segments. The snake grows longer each time it consumes a fruit.

- **Fruit:** Red fruits appear randomly on the screen. The snake must eat these fruits to score points and increase its length.

- **Game Over:** The game ends if the snake collides with the screen edges or itself. In this case, the program will exit.

## Customization

Feel free to customize the game by adjusting parameters such as screen size, snake speed, and colors within the code.

```python
width = 1000
height = 1000

snake_speed = 10

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
```

## Dependencies

- Python 3.x
- Pygame library

## Acknowledgments

- This game is a simple implementation for educational purposes.
- Special thanks to the Pygame community for providing a user-friendly library for game development in Python.

Have fun playing the Snake game!
