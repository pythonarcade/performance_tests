import os
import csv
import matplotlib.pyplot as plt

FPS = 1
SPRITE_COUNT = 2
DRAWING_TIME = 3
PROCESSING_TIME = 4


def read_results(filename):
    results = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = True
        for row in csv_reader:
            if first_row:
                first_row = False
            else:
                results.append([float(cell) for cell in row])

        return results


def chart_stress_test_draw_moving():
    results_arcade = read_results("../result_data/arcade/draw_moving_sprites.csv")
    results_pygame = read_results("../result_data/pygame/draw_moving_sprites.csv")

    sprite_count_arcade = [row[SPRITE_COUNT] for row in results_arcade]
    processing_time_arcade = [row[PROCESSING_TIME] for row in results_arcade]
    drawing_time_arcade = [row[DRAWING_TIME] for row in results_arcade]
    fps_arcade = [row[FPS] for row in results_arcade]

    sprite_count_pygame = [row[SPRITE_COUNT] for row in results_pygame]
    processing_time_pygame = [row[PROCESSING_TIME] for row in results_pygame]
    drawing_time_pygame = [row[DRAWING_TIME] for row in results_pygame]
    fps_pygame = [row[FPS] for row in results_pygame]

    # Arcade timings
    plt.title("Moving and Drawing Sprites In Arcade")
    plt.plot(sprite_count_arcade, processing_time_arcade, label="Processing Time")
    plt.plot(sprite_count_arcade, drawing_time_arcade, label="Drawing Time")

    plt.legend(loc='upper left', shadow=True, fontsize='x-large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_moving_sprites/arcade.svg")
    plt.clf()

    # Pygame timings
    plt.title("Moving and Drawing Sprites In Pygame")
    plt.plot(sprite_count_pygame, processing_time_pygame, label="Processing Time")
    plt.plot(sprite_count_pygame, drawing_time_pygame, label="Drawing Time")

    plt.legend(loc='upper left', shadow=True, fontsize='x-large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_moving_sprites/pygame.svg")
    plt.clf()

    # Time to move comparison
    plt.title("Time to Move Sprites Comparison")
    plt.plot(sprite_count_pygame, processing_time_pygame, label="Pygame")
    plt.plot(sprite_count_arcade, processing_time_arcade, label="Arcade")

    plt.legend(loc='upper left', shadow=True, fontsize='x-large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_moving_sprites/time_to_move_comparison.svg")
    plt.clf()

    # Time to draw comparison
    plt.title("Time to Draw Sprites Comparison")
    plt.plot(sprite_count_pygame, drawing_time_pygame, label="Pygame")
    plt.plot(sprite_count_arcade, drawing_time_arcade, label="Arcade")

    plt.legend(loc='upper left', shadow=True, fontsize='x-large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_moving_sprites/time_to_draw_comparison.svg")
    plt.clf()

    # FPS comparison
    # Some of the initial values are often wonky, so skip those
    plt.title("FPS Comparison")
    plt.plot(sprite_count_arcade[4:], fps_arcade[4:], label="Arcade")
    plt.plot(sprite_count_pygame[4:], fps_pygame[4:], label="Pygame")

    plt.legend(loc='lower left', shadow=True, fontsize='x-large')

    plt.ylabel('FPS')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_moving_sprites/fps_comparison.svg")
    plt.clf()


def chart_collision():
    results_arcade = read_results("../result_data/arcade/collision.csv")
    results_pygame = read_results("../result_data/pygame/collision.csv")

    sprite_count_arcade = [row[SPRITE_COUNT] for row in results_arcade]
    processing_time_arcade = [row[PROCESSING_TIME] for row in results_arcade]
    drawing_time_arcade = [row[DRAWING_TIME] for row in results_arcade]
    fps_arcade = [row[FPS] for row in results_arcade]

    sprite_count_pygame = [row[SPRITE_COUNT] for row in results_pygame]
    processing_time_pygame = [row[PROCESSING_TIME] for row in results_pygame]
    drawing_time_pygame = [row[DRAWING_TIME] for row in results_pygame]
    fps_pygame = [row[FPS] for row in results_pygame]

    # Time to move comparison
    plt.title("Time To Move And Detect Collisions")
    plt.plot(sprite_count_pygame, processing_time_pygame, label="Pygame")
    plt.plot(sprite_count_arcade, processing_time_arcade, label="Arcade")

    plt.legend(loc='upper left', shadow=True, fontsize='x-large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/collision/time_to_move.svg")
    plt.clf()

    # FPS comparison
    # Some of the initial values are often wonky, so skip those
    plt.title("FPS Comparison")
    plt.plot(sprite_count_arcade[4:], fps_arcade[4:], label="Arcade")
    plt.plot(sprite_count_pygame[4:], fps_pygame[4:], label="Pygame")

    plt.legend(loc='lower left', shadow=True, fontsize='x-large')

    plt.ylabel('FPS')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/collision/fps_comparison.svg")
    plt.clf()

def chart_shapes():
    results_arcade_buffered = read_results("../result_data/arcade/moving_shapes_buffered.csv")
    results_arcade_unbuffered = read_results("../result_data/arcade/moving_shapes_unbuffered.csv")
    results_pygame = read_results("../result_data/pygame/moving_shapes.csv")

    shape_count_arcade_buffered = [row[SPRITE_COUNT] for row in results_arcade_buffered]
    processing_time_arcade_buffered = [row[PROCESSING_TIME] for row in results_arcade_buffered]
    drawing_time_arcade_buffered = [row[DRAWING_TIME] for row in results_arcade_buffered]
    fps_arcade_buffered = [row[FPS] for row in results_arcade_buffered]

    shape_count_arcade_unbuffered = [row[SPRITE_COUNT] for row in results_arcade_unbuffered]
    processing_time_arcade_unbuffered = [row[PROCESSING_TIME] for row in results_arcade_unbuffered]
    drawing_time_arcade_unbuffered = [row[DRAWING_TIME] for row in results_arcade_unbuffered]
    fps_arcade_unbuffered = [row[FPS] for row in results_arcade_unbuffered]

    shape_count_pygame = [row[SPRITE_COUNT] for row in results_pygame]
    processing_time_pygame = [row[PROCESSING_TIME] for row in results_pygame]
    drawing_time_pygame = [row[DRAWING_TIME] for row in results_pygame]
    fps_pygame = [row[FPS] for row in results_pygame]

    # FPS comparison
    # Some of the initial values are often wonky, so skip those
    plt.title("FPS Comparison")
    plt.plot(shape_count_arcade_buffered[4:], fps_arcade_buffered[4:], label="Arcade Buffered")
    plt.plot(shape_count_arcade_unbuffered[4:], fps_arcade_unbuffered[4:], label="Arcade Unbuffered")
    plt.plot(shape_count_pygame[4:], fps_pygame[4:], label="Pygame")

    plt.legend(loc='upper right', shadow=True, fontsize='x-large')

    plt.ylabel('FPS')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/shapes/fps_comparison.svg")
    plt.clf()


def main():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    chart_stress_test_draw_moving()
    chart_collision()
    chart_shapes()


if __name__ == "__main__":
    main()
