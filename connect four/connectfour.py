
import pygame, random
pygame.init()

clock = pygame.time.Clock()
FPS = 60

WIN_WIDTH = 850
WIN_HEIGHT = 700
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Connect Four')

SIDE = 60
RED_COIN_IMAGE = pygame.image.load('RED_COIN_IMAGE.png')
RED_COIN_IMAGE = pygame.transform.scale(RED_COIN_IMAGE, (SIDE, SIDE))
YELLOW_COIN_IMAGE = pygame.image.load('YELLOW_COIN_IMAGE.png')
YELLOW_COIN_IMAGE = pygame.transform.scale(YELLOW_COIN_IMAGE, (SIDE, SIDE))
EMPTY_COIN_IMAGE = pygame.image.load('EMPTY_COIN_IMAGE.png')
EMPTY_COIN_IMAGE = pygame.transform.scale(EMPTY_COIN_IMAGE, (SIDE, SIDE))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY = (0, 255, 255)

class Coin:
    SPACING = EMPTY_COIN_IMAGE.get_width() * 1.5
    WIDTH = EMPTY_COIN_IMAGE.get_width()
    def __init__(self, color, x, y):
        self.img = None
        self.x = x
        self.y = y
        if color == 'EMPTY':
            self.img = EMPTY_COIN_IMAGE
        elif color == 'RED':
            self.img = RED_COIN_IMAGE
        elif color == 'YELLOW':
            self.img = YELLOW_COIN_IMAGE

    def draw(self):
        WIN.blit(self.img, (self.x, self.y))

class Board:
    WIDTH = Coin.WIDTH * 2
    x = WIN_WIDTH - WIDTH - 30
    y = 30
    color = BLACK

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.WIDTH, self.WIDTH))


def draw_message(text, x, y, color, font_size = 40):
    font_style = pygame.font.SysFont('FUTURAM.ttf', font_size)
    b = font_style.render(text, True, color)
    WIN.blit(b, [x, y])

NUMBER_OF_COLUMNS = 7
NUMBER_OF_ROWS = 6
COLORS_LIST = ['RED', 'YELLOW']

def main():
    done = False
    play_color = random.choice(COLORS_LIST)
    picked = False
    release = False

    moving_coin = Coin(play_color, WIN_WIDTH - 2 * Coin.WIDTH - 10,  50)
    board = Board()


    def new_grid():
        grid = []
        for i in range(NUMBER_OF_ROWS):
            r = []
            for ii in range(NUMBER_OF_COLUMNS):
                r += ['EMPTY']
            grid += [r]
        return grid
    grid = new_grid()
    def draw_grid(grid):
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                color = grid[row][column]
                coin = Coin(color, Coin.SPACING * (column + 1) - Coin.WIDTH, WIN_HEIGHT - Coin.SPACING * (row + 1))
                coin.draw()

    while not done:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    release = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_pos[0] > moving_coin.x and mouse_pos[0] - moving_coin.x < Coin.WIDTH:
                        if mouse_pos[1] > moving_coin.y and mouse_pos[1] - moving_coin.y < Coin.WIDTH:
                            picked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    picked = False
                    if mouse_pos[0] > Coin.SPACING * (NUMBER_OF_COLUMNS + 1) - Coin.WIDTH:
                        moving_coin.x = WIN_WIDTH - 2 * Coin.WIDTH - 10
                        moving_coin.y = 50
                    elif mouse_pos[0] > Coin.SPACING * (NUMBER_OF_COLUMNS) - Coin.WIDTH:
                        moving_coin.x = Coin.SPACING * (NUMBER_OF_COLUMNS) - Coin.WIDTH
                        moving_coin.y = WIN_HEIGHT - Coin.SPACING * (NUMBER_OF_ROWS + 1)
                    elif mouse_pos[0] > Coin.SPACING * (NUMBER_OF_COLUMNS - 1) - Coin.WIDTH:
                        moving_coin.x = Coin.SPACING * (NUMBER_OF_COLUMNS - 1) - Coin.WIDTH
                        moving_coin.y = WIN_HEIGHT - Coin.SPACING * (NUMBER_OF_ROWS + 1)
                    elif mouse_pos[0] > Coin.SPACING * (NUMBER_OF_COLUMNS - 2) - Coin.WIDTH:
                        moving_coin.x = Coin.SPACING * (NUMBER_OF_COLUMNS - 2) - Coin.WIDTH
                        moving_coin.y = WIN_HEIGHT - Coin.SPACING * (NUMBER_OF_ROWS + 1)
                    elif mouse_pos[0] > Coin.SPACING * (NUMBER_OF_COLUMNS - 3) - Coin.WIDTH:
                        moving_coin.x = Coin.SPACING * (NUMBER_OF_COLUMNS - 3) - Coin.WIDTH
                        moving_coin.y = WIN_HEIGHT - Coin.SPACING * (NUMBER_OF_ROWS + 1)
                    elif mouse_pos[0] > Coin.SPACING * (NUMBER_OF_COLUMNS - 4) - Coin.WIDTH:
                        moving_coin.x = Coin.SPACING * (NUMBER_OF_COLUMNS - 4) - Coin.WIDTH
                        moving_coin.y = WIN_HEIGHT - Coin.SPACING * (NUMBER_OF_ROWS + 1)
                    elif mouse_pos[0] > Coin.SPACING * (NUMBER_OF_COLUMNS - 5) - Coin.WIDTH:
                        moving_coin.x = Coin.SPACING * (NUMBER_OF_COLUMNS - 5) - Coin.WIDTH
                        moving_coin.y = WIN_HEIGHT - Coin.SPACING * (NUMBER_OF_ROWS + 1)
                    else:
                        moving_coin.x = Coin.SPACING * (NUMBER_OF_COLUMNS - 6) - Coin.WIDTH
                        moving_coin.y = WIN_HEIGHT - Coin.SPACING * (NUMBER_OF_ROWS + 1)


        for row in range(len(grid)):
            for column in range(len(grid[0])):
                color = grid[row][column]
                if color != 'EMPTY':

                    if column <= 3:
                        first_color = grid[row][column]
                        color_count = 1
                        for i in range(1, 4):
                            if first_color != grid[row][column + i]:
                                break
                            color_count += 1
                        if color_count == 4:
                            return first_color

                    if row <= 2:
                        first_color = grid[row][column]
                        color_count = 1
                        for i in range(1, 4):
                            if first_color != grid[row + i][column]:
                                break
                            color_count += 1
                        if color_count == 4:
                            return first_color

                    if column <= 3 and row <= 2:
                        first_color = grid[row][column]
                        color_count = 1
                        for i in range(1, 4):
                            if first_color != grid[row + i][column + i]:
                                break
                            color_count += 1
                        if color_count == 4:
                            return first_color

                    if column >= 3 and row <= 2:
                        first_color = grid[row][column]
                        color_count = 1
                        for i in range(1, 4):
                            if first_color != grid[row + i][column - i]:
                                break
                            color_count += 1
                        if color_count == 4:
                            return first_color

        if picked:
            moving_coin.x = mouse_pos[0] - Coin.WIDTH/2
            moving_coin.y = mouse_pos[1] - Coin.WIDTH/2
        if release and not picked:
            release = False
            if moving_coin.x <= Coin.SPACING * (NUMBER_OF_COLUMNS) - Coin.WIDTH:
                playing_column = int(((moving_coin.x + Coin.WIDTH) / Coin.SPACING) - 1)
                for row in range(len(grid)):
                    if grid[row][playing_column] == 'EMPTY':
                        grid[row][playing_column] = play_color
                        break
                moving_coin.x = WIN_WIDTH - 2 * Coin.WIDTH - 10
                moving_coin.y = 50
                if play_color == 'RED':
                    play_color = 'YELLOW'
                    moving_coin.img = YELLOW_COIN_IMAGE
                elif play_color == 'YELLOW':
                    play_color = 'RED'
                    moving_coin.img = RED_COIN_IMAGE

        WIN.fill(BLUE)
        board.draw()
        draw_grid(grid)
        draw_message('press space to release', 20, 20, WHITE)

        moving_coin.draw()
        pygame.display.flip()


def gameloop():
    game = True
    player_won = None
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    player_won = main()
                    draw_message(player_won + ' player won!', WIN_WIDTH/6, 100, WHITE, 60)
                    pygame.display.flip()
                    pygame.time.wait(7000)

        WIN.fill(BLACK)
        if player_won != None:
            draw_message(player_won + ' player won!', WIN_WIDTH/8, 100, WHITE, 60)
        draw_message('press " t " to play...', 100, 200, WHITE)
        pygame.display.flip()


gameloop()




