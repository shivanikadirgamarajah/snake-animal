#  Snake-Animal

A fun twist on the classic Snake game! Instead of a simple snake, you control adorable animals that grow as they eat animal-themed foods. Created by Shivani Kadirgamarajah.

## Features

- **Unique Animal Twist** - Play as different animals (rabbit, pig, panda, monkey) instead of a traditional snake
- **Themed Food Items** - Match foods to your animals (carrots, apples, bamboo, bananas)
- **Colorful Graphics** - Custom sprite-based gameplay with background imagery
- **Score Tracking** - Keep track of your high score as you play

##  Prerequisites

- Python 3.x
- pygame library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shivanikadirgamarajah/snake-animal
   cd snake-animal
   ```

2. **Install dependencies**:
   ```bash
   pip install pygame
   ```

3. **Ensure image assets are present**:
   - `rabbit.png`, `pig.png`, `panda.png`, `monkey.png` (animal sprites)
   - `carrot.png`, `apple.png`, `bamboo.png`, `banana.png` (food sprites)
   - `grass.png` (background image)

##  How to Run

```bash
python snake.py
```

The game window will open and you can start playing immediately!

##  Gameplay

- Use **arrow keys** to control the movement of your animal
- Eat food items to grow your animal and increase your score
- Avoid hitting the walls or yourself
- Try to achieve the highest score!


##  Game Customization

You can customize the game by modifying these variables in `snake.py`:
- `snake_speed` - Adjust game difficulty (higher = faster)
- `snake_block` - Change size of animals
- `dis_width` and `dis_height` - Modify game window dimensions

## Author

Created by Shivani Kadirgamarajah

##  License

Feel free to fork and enjoy!
