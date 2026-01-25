import pygame

import math as m
import sim_loop as sim

#Initial Steps
pygame.init()
WIDTH, HEIGHT = 600, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Elevation Map!")

clock = pygame.time.Clock()

#Load map image
map_img = pygame.image.load("terrain.png").convert()
map_img = pygame.transform.scale(map_img, (WIDTH, HEIGHT))


#Create robot sprite (Triangle pointing up)

size = 20
def create_robot_surface():
    global size

    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.polygon(surf, (255, 0, 0), [(size/2, 0), (0, size), (size, size)])

    return surf

robot_base = create_robot_surface()

def draw_robot(x, y, yaw):
    rotated = pygame.transform.rotate(robot_base, -m.degrees(yaw))
    rect = rotated.get_rect(center = (x, y))
    screen.blit(rotated, rect)

def icon_to_screen(x, y):
    screen_x = int(x / sim.map_size * WIDTH)
    screen_y = HEIGHT - int(y / sim.map_size * HEIGHT)
    return screen_x, screen_y









