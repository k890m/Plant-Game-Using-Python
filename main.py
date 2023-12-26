import pygame
import random
import os


WIDTH, HEIGHT = 500, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grow The Plant!")

WHITE = (255,255,255)

FPS = 60
VEL = 5

PLANT_IMG = pygame.image.load(os.path.join('Assets', 'sadPlant.png'))
PLANT_WIDTH, PLANT_HEIGHT = 100, 85
PLANT = pygame.transform.scale(PLANT_IMG, (PLANT_WIDTH, PLANT_HEIGHT))


RAINDROP_IMG = pygame.image.load(os.path.join('Assets', 'raindrop.png'))
RAINDROP_WIDTH, RAINDROP_HEIGHT = 15, 15
BLACKDROP_IMG = pygame.image.load(os.path.join('Assets', 'blackdrop.png'))

BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'back.jpg'))
BACKGROUND_MAIN = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))


# Start window
def draw_window(plant, raindrops, blackdrops, score):

    WIN.blit(BACKGROUND_MAIN, (0,0))
    
    WIN.blit(PLANT, (plant.x, plant.y))
    
    for raindrop in raindrops:
        WIN.blit(raindrop['image'], (raindrop['x'], raindrop['y']))
        
    for drop in blackdrops:
        WIN.blit(drop['image'], (drop['x'], drop['y']))
        
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    WIN.blit(score_text, (10, 10))

    pygame.display.update()
    
# Making raindrops
def create_raindrops():
    return {
        'image': pygame.transform.scale(RAINDROP_IMG, (RAINDROP_WIDTH, RAINDROP_HEIGHT)),
        'x': random.randint(0, WIDTH - RAINDROP_WIDTH),
        'y': -RAINDROP_HEIGHT
    }

#Make black raindrops NOT DONE YET
def create_blackdrops():
    return {
        'image': pygame.transform.scale(BLACKDROP_IMG, (RAINDROP_WIDTH, RAINDROP_HEIGHT)),
        'x': random.randint(0, WIDTH - RAINDROP_WIDTH),
        'y': -RAINDROP_HEIGHT
    }


def main():
    pygame.font.init()
    
    plant = pygame.Rect(100, 600, PLANT_WIDTH, PLANT_HEIGHT)
    score = 0
    raindrops = []
    blackdrops = []

    clock = pygame.time.Clock()
    run = True 
    
    # Loop to Run Program
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and plant.x - VEL > 0: #LEFT KEY
            plant.x -= VEL
        elif keys_pressed[pygame.K_RIGHT] and plant.x + VEL < WIDTH - PLANT_WIDTH:  #RIGHT KEY
            plant.x += VEL

        #New Raindrops
        if random.random() < .02:
            raindrops.append(create_raindrops())
             
        if random.random() < .01:
            blackdrops.append(create_blackdrops())
            
        for raindrop in raindrops:
            raindrop['y'] += VEL
        
            if plant.colliderect(pygame.Rect(raindrop['x'], raindrop['y'], RAINDROP_WIDTH, RAINDROP_HEIGHT)):
                score += 1
                raindrops.remove(raindrop)
            
        for drop in blackdrops:
            drop['y'] += VEL
            
            if plant.colliderect(pygame.Rect(drop['x'], drop['y'], RAINDROP_WIDTH, RAINDROP_HEIGHT)):
                score -= 1
                blackdrops.remove(drop)
            
        #clear raindrops afterwords
        raindrops = [raindrop for raindrop in raindrops if raindrop['y'] < HEIGHT]
        blackdrops = [drop for drop in blackdrops if drop['y'] < HEIGHT]

        draw_window(plant, raindrops, blackdrops, score)

    pygame.quit()

if __name__ == "__main__":
    main()
