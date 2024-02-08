import pygame
import random
import os


WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grow The Plant!")

BLACK = (0,0,0)

FPS = 60
VEL = 5

PLANT_IMG = pygame.image.load(os.path.join('Assets', 'sadPlant.png'))
PLANT_WIDTH, PLANT_HEIGHT = 100, 85
PLANT = pygame.transform.scale(PLANT_IMG, (PLANT_WIDTH, PLANT_HEIGHT))


RAINDROP_IMG = pygame.image.load(os.path.join('Assets', 'raindrop.png'))
RAINDROP_WIDTH, RAINDROP_HEIGHT = 15, 15
BLACKDROP_IMG = pygame.image.load(os.path.join('Assets', 'blackdrop.png'))

BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'background.jpg'))
BACKGROUND_MAIN = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))

# Title screen
def draw_title_screen():
    WIN.blit(BACKGROUND_MAIN, (0, 0))

    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("Grow The Plant!", True, BLACK)
    WIN.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 4))

    start_font = pygame.font.Font(None, 36)
    start_text = start_font.render("Press SPACE to start", True, BLACK)
    WIN.blit(start_text, ((WIDTH - start_text.get_width()) // 2, HEIGHT // 2))

    pygame.display.update()


# End Screen
def draw_end_screen(score):
    WIN.blit(BACKGROUND_MAIN, (0, 0))

    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render(f"Your Score: {score}", True, BLACK)
    WIN.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 4))

    play_again_font = pygame.font.Font(None, 36)
    play_again_text = play_again_font.render("Press SPACE To Go To Main Page", True, BLACK)
    WIN.blit(play_again_text, ((WIDTH - play_again_text.get_width()) // 2, HEIGHT // 2))

    pygame.display.update()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                reset_game()
                waiting_for_input = False

# Reset the game   
def reset_game():
    global score, lives, raindrops, blackdrops
    score = 0
    lives = 3
    raindrops = []
    blackdrops = []
    
# Start window
def draw_window(plant, raindrops, blackdrops, score, lives):

    WIN.blit(BACKGROUND_MAIN, (0,0))
    
    WIN.blit(PLANT, (plant.x, plant.y))
    
    for raindrop in raindrops:
        WIN.blit(raindrop['image'], (raindrop['x'], raindrop['y']))
        
    for drop in blackdrops:
        WIN.blit(drop['image'], (drop['x'], drop['y']))
        
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives Left: {lives}", True, BLACK)
    WIN.blit(score_text, (10, 10))
    WIN.blit(lives_text, (550,10))

    pygame.display.update()
    
    
def create_drops(IMG):
    return {
        'image': pygame.transform.scale(IMG, (RAINDROP_WIDTH, RAINDROP_HEIGHT)),
        'x': random.randint(0, WIDTH - RAINDROP_WIDTH),
        'y': -RAINDROP_HEIGHT
    }

def game_loop():
    global run
    plant = pygame.Rect(100, 600, PLANT_WIDTH, PLANT_HEIGHT)
    score = 0
    lives = 3
    raindrops = []
    blackdrops = []



    clock = pygame.time.Clock()
    title_screen = True

    while title_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                title_screen = False

        draw_title_screen()

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and plant.x - VEL > 0:  # LEFT KEY
            plant.x -= VEL
        elif keys_pressed[pygame.K_RIGHT] and plant.x + VEL < WIDTH - PLANT_WIDTH:  # RIGHT KEY
            plant.x += VEL

        #New Raindrops
        if random.random() < .02:
            raindrops.append(create_drops(RAINDROP_IMG))
             
        if random.random() < .02:
            blackdrops.append(create_drops(BLACKDROP_IMG))
            
        for raindrop in raindrops:
            raindrop['y'] += VEL
        
            if plant.colliderect(pygame.Rect(raindrop['x'], raindrop['y'], RAINDROP_WIDTH, RAINDROP_HEIGHT)):
                score += 1
                raindrops.remove(raindrop)
            
        for drop in blackdrops:
            drop['y'] += VEL
            
            if plant.colliderect(pygame.Rect(drop['x'], drop['y'], RAINDROP_WIDTH, RAINDROP_HEIGHT)):
                lives -= 1
                blackdrops.remove(drop)
                
                if lives == 0:
                    run = False
            
        #clear raindrops afterwords
        raindrops = [raindrop for raindrop in raindrops if raindrop['y'] < HEIGHT]
        blackdrops = [drop for drop in blackdrops if drop['y'] < HEIGHT]


        draw_window(plant, raindrops, blackdrops, score, lives)

        if not run:
            draw_end_screen(score)
            reset_game()  # Reset the game state


def main():
    pygame.font.init()
    
    global run
    title_screen = True

    while title_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                title_screen = False

        draw_title_screen()

    while True:
        reset_game() 
        game_loop()



if __name__ == "__main__":
    main()
