import os
import csv
import matplotlib.pyplot as plt
import seaborn as sns

FPS = 1
SPRITE_COUNT = 2
DRAWING_TIME = 3
PROCESSING_TIME = 4
PYGAME_VERSION = 20


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


def chart_stress_test_draw_stationary():
    results_arcade = read_results("../result_data/arcade/draw_stationary_sprites.csv")
    results_pygame20 = read_results(f"../result_data/pygame/draw_stationary_sprites.csv")

    sprite_count_arcade = [row[SPRITE_COUNT] for row in results_arcade]
    drawing_time_arcade = [row[DRAWING_TIME] for row in results_arcade]
    fps_arcade = [row[FPS] for row in results_arcade]

    sprite_count_pygame20 = [row[SPRITE_COUNT] for row in results_pygame20]
    drawing_time_pygame20 = [row[DRAWING_TIME] for row in results_pygame20]
    fps_pygame20 = [row[FPS] for row in results_pygame20]

    # Time to draw comparison
    plt.title("Time to Draw Sprites Comparison")
    plt.plot(sprite_count_pygame20, drawing_time_pygame20, label="Pygame")
    plt.plot(sprite_count_arcade, drawing_time_arcade, label="Arcade")

    plt.legend(loc='upper left', shadow=True, fontsize='large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_stationary_sprites/time_to_draw_comparison.svg")
    plt.clf()

    # FPS comparison
    # Some of the initial values are often wonky, so skip those
    plt.title("FPS Comparison")
    plt.plot(sprite_count_arcade[4:], fps_arcade[4:], label="Arcade")
    plt.plot(sprite_count_pygame20[4:], fps_pygame20[4:], label="Pygame")

    plt.legend(loc='lower left', shadow=True, fontsize='large')

    plt.ylabel('FPS')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_stationary_sprites/fps_comparison.svg")
    plt.clf()


def chart_stress_test_draw_moving():
    results_arcade = read_results("../result_data/arcade/draw_moving_sprites.csv")
    results_pygame20 = read_results(f"../result_data/pygame/draw_moving_sprites.csv")

    sprite_count_arcade = [row[SPRITE_COUNT] for row in results_arcade]
    processing_time_arcade = [row[PROCESSING_TIME] for row in results_arcade]
    drawing_time_arcade = [row[DRAWING_TIME] for row in results_arcade]
    fps_arcade = [row[FPS] for row in results_arcade]

    sprite_count_pygame20 = [row[SPRITE_COUNT] for row in results_pygame20]
    processing_time_pygame20 = [row[PROCESSING_TIME] for row in results_pygame20]
    drawing_time_pygame20 = [row[DRAWING_TIME] for row in results_pygame20]
    fps_pygame20 = [row[FPS] for row in results_pygame20]

    # Arcade timings
    plt.title("Moving and Drawing Sprites In Arcade")
    plt.plot(sprite_count_arcade, processing_time_arcade, label="Processing Time")
    plt.plot(sprite_count_arcade, drawing_time_arcade, label="Drawing Time")

    plt.legend(loc='upper left', shadow=True, fontsize='large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_moving_sprites/arcade.svg")
    plt.clf()

    # Pygame timings
    plt.title("Moving and Drawing Sprites In Pygame")
    plt.plot(sprite_count_pygame20, processing_time_pygame20, label="Processing Time")
    plt.plot(sprite_count_pygame20, drawing_time_pygame20, label="Drawing Time")

    plt.legend(loc='upper left', shadow=True, fontsize='large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig(f"../result_charts/draw_moving_sprites/pygame{PYGAME_VERSION}.svg")
    plt.clf()

    # Time to move comparison
    plt.title("Time to Move Sprites Comparison")
    plt.plot(sprite_count_pygame20, processing_time_pygame20, label="Pygame")
    plt.plot(sprite_count_arcade, processing_time_arcade, label="Arcade")

    plt.legend(loc='upper left', shadow=True, fontsize='large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_moving_sprites/time_to_move_comparison.svg")
    plt.clf()

    # Time to draw comparison
    plt.title("Time to Draw Sprites Comparison")
    plt.plot(sprite_count_pygame20, drawing_time_pygame20, label="Pygame")
    plt.plot(sprite_count_arcade, drawing_time_arcade, label="Arcade")

    plt.legend(loc='upper left', shadow=True, fontsize='large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_moving_sprites/time_to_draw_comparison.svg")
    plt.clf()

    # FPS comparison
    # Some of the initial values are often wonky, so skip those
    plt.title("FPS Comparison")
    plt.plot(sprite_count_arcade[4:], fps_arcade[4:], label="Arcade")
    plt.plot(sprite_count_pygame20[4:], fps_pygame20[4:], label="Pygame")

    plt.legend(loc='lower left', shadow=True, fontsize='large')

    plt.ylabel('FPS')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/draw_moving_sprites/fps_comparison.svg")
    plt.clf()


def chart_collision():
    results_arcade_0 = read_results("../result_data/arcade/collision-0.csv")
    results_arcade_1 = read_results("../result_data/arcade/collision-1.csv")
    results_arcade_2 = read_results("../result_data/arcade/collision-2.csv")
    results_arcade_3 = read_results("../result_data/arcade/collision-3.csv")
    results_pygame20 = read_results(f"../result_data/pygame/collision.csv")

    sprite_count_arcade_0 = [row[SPRITE_COUNT] for row in results_arcade_0]
    processing_time_arcade_0 = [row[PROCESSING_TIME] for row in results_arcade_0]
    drawing_time_arcade_0 = [row[DRAWING_TIME] for row in results_arcade_0]
    fps_arcade_0 = [row[FPS] for row in results_arcade_0]

    sprite_count_arcade_1 = [row[SPRITE_COUNT] for row in results_arcade_1]
    processing_time_arcade_1 = [row[PROCESSING_TIME] for row in results_arcade_1]
    drawing_time_arcade_1 = [row[DRAWING_TIME] for row in results_arcade_1]
    fps_arcade_1 = [row[FPS] for row in results_arcade_1]

    sprite_count_arcade_2 = [row[SPRITE_COUNT] for row in results_arcade_2]
    processing_time_arcade_2 = [row[PROCESSING_TIME] for row in results_arcade_2]
    drawing_time_arcade_2 = [row[DRAWING_TIME] for row in results_arcade_2]
    fps_arcade_2 = [row[FPS] for row in results_arcade_2]

    sprite_count_arcade_3 = [row[SPRITE_COUNT] for row in results_arcade_3]
    processing_time_arcade_3 = [row[PROCESSING_TIME] for row in results_arcade_3]
    drawing_time_arcade_3 = [row[DRAWING_TIME] for row in results_arcade_3]
    fps_arcade_3 = [row[FPS] for row in results_arcade_3]

    sprite_count_pygame20 = [row[SPRITE_COUNT] for row in results_pygame20]
    processing_time_pygame20 = [row[PROCESSING_TIME] for row in results_pygame20]
    drawing_time_pygame20 = [row[DRAWING_TIME] for row in results_pygame20]
    fps_pygame20 = [row[FPS] for row in results_pygame20]

    # Time to move comparison
    plt.title("Time To Detect Collisions")
    # plt.plot(sprite_count_pygame20, processing_time_pygame20, label="Pygame")
    # plt.plot(sprite_count_arcade_2, processing_time_arcade_0, label="Arcade default")
    # plt.plot(sprite_count_arcade_1, processing_time_arcade_1, label="Arcade spatial hashing")
    plt.plot(sprite_count_arcade_2, processing_time_arcade_2, label="Arcade GPU")
    plt.plot(sprite_count_arcade_3, processing_time_arcade_3, label="Arcade simple")

    plt.legend(loc='upper left', shadow=True, fontsize='large')

    plt.ylabel('Time')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/collision/collision.svg")
    plt.clf()

    # FPS comparison
    # Some of the initial values are often wonky, so skip those
    plt.title("FPS Comparison")
    plt.plot(sprite_count_arcade_1[4:], fps_arcade_1[4:], label="Arcade")
    plt.plot(sprite_count_arcade_2[4:], fps_arcade_2[4:], label="Arcade")
    plt.plot(sprite_count_arcade_3[4:], fps_arcade_3[4:], label="Arcade")
    plt.plot(sprite_count_pygame20[4:], fps_pygame20[4:], label="Pygame")

    plt.legend(loc='lower left', shadow=True, fontsize='large')

    plt.ylabel('FPS')
    plt.xlabel('Sprite Count')

    plt.savefig("../result_charts/collision/fps_comparison.svg")
    plt.clf()


def chart_shapes():
    results_arcade_buffered = read_results("../result_data/arcade/moving_shapes_buffered.csv")
    results_arcade_unbuffered = read_results("../result_data/arcade/moving_shapes_unbuffered.csv")
    results_pygame20 = read_results(f"../result_data/pygame/moving_shapes.csv")

    shape_count_arcade_buffered = [row[SPRITE_COUNT] for row in results_arcade_buffered]
    processing_time_arcade_buffered = [row[PROCESSING_TIME] for row in results_arcade_buffered]
    drawing_time_arcade_buffered = [row[DRAWING_TIME] for row in results_arcade_buffered]
    fps_arcade_buffered = [row[FPS] for row in results_arcade_buffered]

    shape_count_arcade_unbuffered = [row[SPRITE_COUNT] for row in results_arcade_unbuffered]
    processing_time_arcade_unbuffered = [row[PROCESSING_TIME] for row in results_arcade_unbuffered]
    drawing_time_arcade_unbuffered = [row[DRAWING_TIME] for row in results_arcade_unbuffered]
    fps_arcade_unbuffered = [row[FPS] for row in results_arcade_unbuffered]

    shape_count_pygame20 = [row[SPRITE_COUNT] for row in results_pygame20]
    processing_time_pygame20 = [row[PROCESSING_TIME] for row in results_pygame20]
    drawing_time_pygame20 = [row[DRAWING_TIME] for row in results_pygame20]
    fps_pygame20 = [row[FPS] for row in results_pygame20]

    # FPS comparison
    # Some of the initial values are often wonky, so skip those
    plt.title("FPS Comparison")
    plt.plot(shape_count_arcade_buffered[4:], fps_arcade_buffered[4:], label="Arcade Buffered")
    plt.plot(shape_count_arcade_unbuffered[4:], fps_arcade_unbuffered[4:], label="Arcade Unbuffered")
    plt.plot(shape_count_pygame20[4:], fps_pygame20[4:], label="Pygame")

    plt.legend(loc='upper right', shadow=True, fontsize='large')

    plt.ylabel('FPS')
    plt.xlabel('Shape Count')

    plt.savefig("../result_charts/shapes/fps_comparison.svg")
    plt.clf()


def main():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    sns.set_style("whitegrid")

    chart_stress_test_draw_stationary()
    chart_stress_test_draw_moving()
    chart_collision()
    chart_shapes()


if __name__ == "__main__":
    main()
