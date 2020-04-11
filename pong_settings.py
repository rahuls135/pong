
# Pong settings

# General settings
TITLE = "Pong"
WIDTH = 800
HEIGHT = 600
BUFFER = 5
NUM_ROUNDS = 3

# Background setings
img = 'pong_background.png'

# Font settings
FONTSIZE = 32
FONTNAME = "freesansbold.ttf"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# PADDLE attributes
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_SPEED = 250
PADDLE_LEFT_START = (25, (HEIGHT - PADDLE_HEIGHT) / 2)
PADDLE_RIGHT_START = (WIDTH - PADDLE_WIDTH - 25, (HEIGHT - PADDLE_HEIGHT) / 2)
BUFFER = 5

# Ball attributes
BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_SPEED = 250
BALL_SPEED_CHANGE = 25

# Game states
GAME_START = 'S'
GAME_PLAYING = 'P'
GAME_OVER = 'O'