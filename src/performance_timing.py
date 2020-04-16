import timeit
import statistics


class PerformanceTiming:
    def __init__(self, results_file):
        self.program_start_time = timeit.default_timer()
        self.results_file = open(results_file, "w")
        self.last_report = 0
        self.start_timers = {}
        self.timing_lists = {}
        self.first_line = True

    @property
    def total_program_time(self):
        total_program_time = timeit.default_timer() - self.program_start_time
        return total_program_time

    @property
    def target_n(self):
        return int(self.total_program_time + 0.5) * 100

    def end_run(self):
        if self.total_program_time > 60:
            self.results_file.close()
            return True
        else:
            return False

    def start_timer(self, timer_name):
        self.start_timers[timer_name] = timeit.default_timer()

    def stop_timer(self, timer_name):
        time = timeit.default_timer() - self.start_timers[timer_name]
        if timer_name not in self.timing_lists:
            self.timing_lists[timer_name] = []
        self.timing_lists[timer_name].append(time)
        self.report()

    def report(self):
        current_time = self.total_program_time
        if self.first_line:
            self.first_line = False
            output = f"Time, FPS, Sprite Count, Draw Time, Update Time"
            print(output)
            self.results_file.write(output)
            self.results_file.write("\n")

        if int(current_time) > int(self.last_report):
            exact_time = current_time - self.last_report
            self.last_report = current_time
            draw_time = statistics.mean(self.timing_lists['draw'])
            update_time = statistics.mean(self.timing_lists['update'])
            fps = len(self.timing_lists['draw']) / exact_time
            output = f"{int(current_time)}, {fps:.1f}, {self.target_n}, {draw_time:.6f}, {update_time:.6f}"
            print(output)
            self.results_file.write(output)
            self.results_file.write("\n")

            # Reset timers
            self.timing_lists = {}
