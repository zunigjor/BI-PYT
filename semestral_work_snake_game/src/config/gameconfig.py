# Game settings
SCREEN_WIDTH = 840   # Window width, in px
SCREEN_HEIGHT = 840  # Window height, in px
SQUARE_SIZE = 60       # Size of each square, in px
GRID_WIDTH = int(SCREEN_WIDTH / SQUARE_SIZE)  # Grid width, in squares
GRID_HEIGHT = int(SCREEN_HEIGHT / SQUARE_SIZE)  # Grid height, in squares
GRID_SIZE = int(SCREEN_WIDTH / SQUARE_SIZE * SCREEN_HEIGHT / SQUARE_SIZE)

# Max score, after this many points the victory screen appears
MAX_SCORE = GRID_SIZE

# COLORS
COLOR_RED = (235, 73, 52)

COLOR_DARK_GREEN = (74, 179, 39)
COLOR_GREEN = (97, 235, 52)

COLOR_BLUE = (52, 190, 235)
COLOR_LIGHT_BLUE = (52, 206, 235)
COLOR_DARK_BLUE = (32, 117, 145)
COLOR_DARKER_BLUE = (24, 88, 110)

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

COLOR_ORANGE = (255, 119, 0)
COLOR_YELLOW = (255, 252, 84)
COLOR_PINK = (255, 0, 123)

# CONSTANTS, DO NOT CHANGE THESE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
