import os

import arcade.key

import arcade_tests.draw_moving_sprites
import pygame_tests.draw_moving_sprites

import arcade_tests.collision
import pygame_tests.collision

import arcade_tests.draw_shapes
import pygame_tests.draw_shapes

import generate_graphs

print("--- Draw Stationary Arcade")
# arcade_tests.draw_stationary_sprites.main()
# arcade.cleanup_texture_cache()

print("--- Draw Stationary Pygame")
# pygame_tests.draw_stationary_sprites.main()

# Draw Moving Sprites Tests
print("--- Draw Moving Arcade")
# arcade_tests.draw_moving_sprites.main()
# arcade.cleanup_texture_cache()

print("--- Draw Moving Pygame")
# pygame_tests.draw_moving_sprites.main()

# Collision tests
print("--- Collision Arcade")
# arcade_tests.collision.main()
# arcade.cleanup_texture_cache()

print("--- Collision Pygame")
# pygame_tests.collision.main()

# Shape tests
print("--- Shape test Arcade Buffered")
# arcade_tests.draw_shapes.main(buffered=True)
# arcade.cleanup_texture_cache()

print("--- Shape test Arcade UnBuffered")
# arcade_tests.draw_shapes.main(buffered=False)

print("--- Shape test Pygame")
# pygame_tests.draw_shapes.main()

# Generate the graphs
print("--- Generating Graphs")
generate_graphs.main()

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path + "/../doc")
os.system('make html')