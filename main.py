import random
import numpy as np
import time

def draw(world, width, height):
    print('\033[H' + time.asctime(time.localtime()))
    time.sleep(1)
    for x in range(width):
        for y in range(height):
            if world[y][x] == 1:
                print('▉', end = '     ')
            else:
                print('  ', end = '     ')
        print('\n')

def evolution(world, width, height):
    newWorld = world
    for x in range(1, width-1):
        for y in range(1, height-1):
            lives = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if world[j][i]:
                        lives = lives + 1
            if world[y][x]:
                lives = lives - 1
            if lives == 3:
                newWorld[y][x] = 1
            elif lives == 2 and world[y][x] == 1:
                newWorld[y][x] = 1
            else:
                newWorld[y][x] = 0
    return newWorld


def main():
    width = 30
    height = 30
    world = np.zeros((height, width))

    for x in range(width):
        for y in range(height):
            if random.randrange(0, 32767) < 32767 / 10:
                world[y][x] = 1
            else:
                world[y][x] = 0
    
    for i in range(100):
        draw(world, width, height)
        world = evolution(world, width, height)

main()
