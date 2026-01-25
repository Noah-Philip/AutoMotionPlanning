import pygame
import sim_loop as sim
from robotIcon import screen, clock, map_img, draw_robot, icon_to_screen
import mazeSolver as ms

start = (sim.startX, sim.startY)
end = (sim.endX, sim.endY)

path = ms.mazeSolve(sim.cells, start, end)
if path is None:
    print("no valid path!")
    exit()

path_index = 0

pygame.init()

running = True

while(running):
    clock.tick(50) #50 hz

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    #Advance simulation by 1 step
    sim.Robot.step()

    #Draw the icon onto the map
    screen.blit(map_img, (0, 0))
    sx, sy = icon_to_screen(sim.Robot.x, sim.Robot.y)

    #Draw a path from the start to end
    path_screen = [icon_to_screen(x, y) for x, y in path]
    pygame.draw.lines(screen, (255, 0, 0), False, path_screen, 2)

    #Draw the robot
    draw_robot(sx, sy, sim.Robot.yaw)
    
    pygame.display.flip()