import os

import arcade_tests.draw_moving_sprites
import pygame_1_9_tests.draw_moving_sprites

import arcade_tests.collision
import pygame_1_9_tests.collision

import generate_graphs


# Draw Moving Sprites Tests
print("--- Draw Moving Arcade")
arcade_tests.draw_moving_sprites.main()

# print("--- Draw Moving Pygame")
pygame_1_9_tests.draw_moving_sprites.main()

# Collision tests
print("--- Collision Arcade")
arcade_tests.collision.main()
print("--- Collision Pygame")
pygame_1_9_tests.collision.main()

# Generate the graphs
generate_graphs.main()

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path + "/../doc")
os.system('make html')