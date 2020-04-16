import timeit
import time
import collections
import statistics

class FPSCounter:
    def __init__(self, results_file):
        self.time = time.perf_counter()
        self.frame_times = collections.deque(maxlen=60)
        self.results_file = results_file

    def tick(self):
        t1 = time.perf_counter()
        dt = t1 - self.time
        self.time = t1
        self.frame_times.append(dt)

    def get_fps(self):
        total_time = sum(self.frame_times)
        if total_time == 0:
            return 0
        else:
            return len(self.frame_times) / sum(self.frame_times)

class PerformanceTiming:
    def __init__(self, results_file):
        self.draw_start_time = None
        self.draw_time = None
        self.update_start_time = None
        self.update_time = None
        self.program_start_time = timeit.default_timer()
        self.processing_time = None
        self.results_file = open(results_file, "w")
        self.last_report = 0
        self.draw_time_list = []
        self.update_time_list = []
        self.frame_count = 0

    @property
    def total_program_time(self):
        total_program_time = timeit.default_timer() - self.program_start_time
        return total_program_time

    @property
    def target_n(self):
        return int(self.total_program_time + 0.5) * 100

    def end_run(self):
        if self.total_program_time > 60:
            return True
        else:
            return False

    def start_draw_timer(self):
        self.draw_start_time = timeit.default_timer()

    def stop_draw_timer(self):
        self.draw_time = timeit.default_timer() - self.draw_start_time
        self.draw_time_list.append(self.draw_time)
        self.frame_count += 1
        self.report()


    def start_update_timer(self):
        self.update_start_time = timeit.default_timer()

    def stop_update_timer(self):
        self.update_time = timeit.default_timer() - self.update_start_time
        self.update_time_list.append(self.update_time)
        self.report()

    def report(self):
        current_time = self.total_program_time
        if int(current_time) > int(self.last_report):
            exact_time = current_time - self.last_report
            self.last_report = current_time
            draw_time = statistics.mean(self.draw_time_list)
            update_time = statistics.mean(self.update_time_list)
            fps = self.frame_count / exact_time
            self.frame_count = 0
            output = f"{int(current_time)}, {fps:.1f}, {self.target_n}, {draw_time:.6f}, {update_time:.6f}"
            print(output)
            self.results_file.write(output)
            self.results_file.write("\n")
