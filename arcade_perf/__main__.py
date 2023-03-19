import sys
import argparse
from datetime import datetime
from arcade_perf.manager import TestManager


def main():
    args = parse_args(sys.argv[1:])
    print(f"Session name: '{args.session}'")
    manager = TestManager(args.session, debug=True)
    manager.find_test_classes(args.type, args.name)
    manager.create_test_instances()
    manager.run()

    # -- Graphs  --
    # draw_stationary_sprites [pygame, arcade]

    # draw_moving_sprites [pygame, arcade[basic, sprite]]

    # collision
    # Time To Detect Collisions
    # - arcade.collision-2 Arcade GPU
    # - arcade.collision-3 Arcade Simple

    # shapes


# run -s test -t arcade, -n collision
def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--session",
        help="Session name",
        type=str,
        default=datetime.now().strftime("%Y-%m-%dT%H-%M-%S"),
    )
    parser.add_argument("-t", "--type", help="Test type", type=str)
    parser.add_argument("-n", "--name", help="Test name", type=str)
    return parser.parse_args(args)


if __name__ == "__main__":
    main()
