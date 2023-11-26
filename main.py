import pygame
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


RAIN_IMG = pygame.image.load(os.path.join('Assets', 'raindrop.png'))
RAIN_WIDTH, RAIN_HEIGHT = 12, 8


BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'back.jpg'))
BACKGROUND_MAIN = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))

def draw_window(plant):
    WIN.blit(BACKGROUND_MAIN, (0,0))
    
    WIN.blit(PLANT, (plant.x, plant.y))
    pygame.display.update()



def main():
    plant = pygame.Rect(100, 600, PLANT_WIDTH, PLANT_HEIGHT)

    clock = pygame.time.Clock()
    run = True 
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

        draw_window(plant)

    pygame.quit()

if __name__ == "__main__":
    main()