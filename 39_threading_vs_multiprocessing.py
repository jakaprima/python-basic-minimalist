# TUTORIAL: Threading vs. Multiprocessing

import time
import threading
import multiprocessing

# --- 1. A CPU-Bound Task ---
# A task that performs heavy calculations and keeps the CPU busy.
def cpu_bound_task(n):
    while n > 0:
        n -= 1

# --- 2. An I/O-Bound Task ---
# A task that waits for an external resource (e.g., network, disk).
# We simulate this with time.sleep().
def io_bound_task(name):
    print(f"Starting I/O task {name}...")
    time.sleep(2) # Simulate waiting for a 2-second download
    print(f"Finished I/O task {name}.")

def measure_time(name, func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    print(f"{name}: {end_time - start_time:.4f} seconds")

def run_cpu_bound_tests():
    COUNT = 100_000_000
    print(f"--- CPU-BOUND TASKS (Counting to {COUNT:,}) ---")

    # a. Sequential (Baseline)
    measure_time("Sequential", lambda: (cpu_bound_task(COUNT), cpu_bound_task(COUNT)))

    # b. Threading (No speed-up due to GIL)
    def threaded_cpu():
        t1 = threading.Thread(target=cpu_bound_task, args=(COUNT,))
        t2 = threading.Thread(target=cpu_bound_task, args=(COUNT,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    measure_time("With Threading", threaded_cpu)

    # c. Multiprocessing (Significant speed-up)
    def multiprocess_cpu():
        p1 = multiprocessing.Process(target=cpu_bound_task, args=(COUNT,))
        p2 = multiprocessing.Process(target=cpu_bound_task, args=(COUNT,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    measure_time("With Multiprocessing", multiprocess_cpu)

def run_io_bound_tests():
    print("\n--- I/O-BOUND TASKS (Simulating 2 downloads of 2s each) ---")

    # a. Sequential (Baseline)
    measure_time("Sequential", lambda: (io_bound_task("A"), io_bound_task("B")))

    # b. Threading (Significant speed-up)
    def threaded_io():
        t1 = threading.Thread(target=io_bound_task, args=("A",))
        t2 = threading.Thread(target=io_bound_task, args=("B",))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    measure_time("With Threading", threaded_io)

    # c. Multiprocessing (Also works, but is heavier than needed)
    def multiprocess_io():
        p1 = multiprocessing.Process(target=io_bound_task, args=("A",))
        p2 = multiprocessing.Process(target=io_bound_task, args=("B",))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    measure_time("With Multiprocessing", multiprocess_io)

if __name__ == "__main__":
    run_cpu_bound_tests()
    run_io_bound_tests()