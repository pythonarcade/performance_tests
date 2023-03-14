import sys
import argparse
from datetime import datetime
from . import OUT_DIR
from arcade_perf.tests.arcade import collision
from arcade_perf import manager

# Create test instances
collision_0 = collision.Test(method=0)
collision_1 = collision.Test(method=1)
collision_2 = collision.Test(method=2)
collision_3 = collision.Test(method=3)


def main():
    session_name = "test"
    session_dir = OUT_DIR / session_name
    session_dir.mkdir(parents=True, exist_ok=True)

    # Run tests
    # collision_0.run(session_dir)
    # collision_1.run(session_dir)
    # collision_2.run(session_dir)
    # collision_3.run(session_dir)

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
    args = parse_args(sys.argv[1:])
