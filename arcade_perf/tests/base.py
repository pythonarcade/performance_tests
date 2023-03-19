import time
from pathlib import Path
from typing import Tuple
import pygame
import arcade
from arcade_perf.timing import PerformanceTiming


class PerfTest:
    """
    Base class for performance tests.

    This class is responsible for setting up the test, running the test, and
    saving the results.

    :param size: The size of the window to create.
    :param title: The title of the window.
    :param start_count: The number of objects to start with.
    :param increment_count: The number of objects to add each time.
    :param duration: The number of seconds to run the test.
    """
    name = "default"
    type = "default"
    series_name = "default"
    instances = []

    def __init__(
        self,
        size: Tuple[int, int],
        title: str = "Perf Test",
        start_count: int = 0,
        increment_count: int = 100,
        duration: float = 60.0,
        **kwargs,
    ):
        self.size = size
        self.title = title
        self.start_count = start_count
        self.increment_count = increment_count
        self.duration = duration
        self.frame = 0
        self.timing = None

    def get_instance_name(self, **kwargs):
        """Get information from the instance values"""
        for k, v in self.instances:
            if k == kwargs:
                return v

        raise ValueError(f"Unknown instance value: {kwargs}")

    def on_draw(self):
        pass

    def on_update(self, delta_time: float):
        self.frame += 1

    def update_state(self):
        pass

    def run(self, session_dir: Path):
        self.frame = 0
        session_dir.mkdir(parents=True, exist_ok=True)
        self.timing = PerformanceTiming(
            session_dir / f"{self.type}_{self.name}.csv",
            start_n=self.start_count,
            increment_n=self.increment_count,
            end_time=self.duration,
        )


class ArcadePerfTest(PerfTest):
    type = "arcade"

    def __init__(
        self,
        size: Tuple[int, int],
        title: str = "Perf Test",
        start_count: int = 0,
        increment_count: int = 100,
        duration: float = 60.0,
        **kwargs
    ):
        super().__init__(
            size, title, start_count, increment_count, duration, **kwargs
        )
        self.window = None

    def on_draw(self):
        pass

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def update_state(self):
        pass

    def run_test(self):
        """Run the test without collecting data"""
        super().run()
        self.create_window()
        self.setup()
        while not self.timing.end_run():
            self.window.dispatch_events()
            self.on_update(1 / 60)
            self.on_draw()
            self.update_state()
            self.window.flip()


    def run(self, session_dir: Path, screenshot: bool = True):
        """Run the test collecting data."""
        super().run(session_dir / "data")
        self.create_window()
        self.setup()

        # last_time = time.time()
        # current_time = time.time()

        while not self.timing.end_run():
            self.window.dispatch_events()

            self.timing.start_timer("update")
            self.on_update(1 / 60)
            self.timing.stop_timer("update")

            self.window.clear()

            self.timing.start_timer("draw")
            self.on_draw()
            self.timing.stop_timer("draw")

            self.update_state()

            self.window.flip()

        # Save screenshot
        if screenshot:
            path = session_dir / "images"
            path.mkdir(parents=True, exist_ok=True)
            arcade.get_image().save(
                path / f"{self.type}_{self.name}.png"
            )

    def create_window(self):
        try:
            self.window = arcade.get_window()
            self.window.set_size(*self.size)
        except RuntimeError:
            self.window = arcade.open_window(*self.size, self.title)
            # Run a few fames to warm up the window
            for _ in range(10):
                self.window.clear()
                self.window.flip()


class PygamePerfTest(PerfTest):
    type = "pygame"

    def __init__(
        self,
        size: Tuple[int, int],
        title: str = "Perf Test",
        start_count: int = 0,
        increment_count: int = 100,
        duration: float = 60.0,
        **kwargs
    ):
        super().__init__(
            size, title, start_count, increment_count, duration, **kwargs
        )
        self.window = None

    def on_draw(self):
        super().on_draw()
        self.window.fill((0, 0, 0))
    
    def on_update(self, delta_time: float):
        return super().on_update(delta_time)

    def run(self, session_dir: Path):
        """Run the test."""
        super().run(session_dir)
        self.window = None
        try:
            self.window = pygame.display.get_surface()
            self.window = pygame.display.set_mode(self.size)
        except pygame.error:
            self.window = pygame.display.set_mode(self.size)
            pygame.display.set_caption(self.title)

        self.setup()

        while not self.timing.end_run():
            pygame.event.get()

            self.timing.start_timer("update")
            self.on_update(1 / 60)
            self.timing.stop_timer("update")

            self.window.fill((59, 122, 87))

            self.timing.start_timer("draw")
            self.on_draw()
            self.timing.stop_timer("draw")

            self.update_state()
            pygame.display.flip()
