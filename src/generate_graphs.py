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

    # Time to move comparison
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


def main():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    chart_stress_test_draw_moving()


if __name__ == "__main__":
    main()
