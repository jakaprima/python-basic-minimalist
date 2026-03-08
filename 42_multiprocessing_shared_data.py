# TUTORIAL: Sharing Data Between Processes
# Unlike threads, processes do NOT share memory by default.
# Global variables in one process are not visible to others.

import multiprocessing

# --- 1. The Problem: Global Variables Don't Work ---
result = []

def worker_fail(data):
    global result
    result.append(data)
    print(f"Worker: Added {data}, result is now {result}")

def run_fail_demo():
    print("--- Demo: Global Variables (Fail) ---")
    p = multiprocessing.Process(target=worker_fail, args=(10,))
    p.start()
    p.join()
    # The main process's 'result' is still empty!
    print(f"Main: Result is {result} (Expected [10])")
    print("Reason: The worker process had its own copy of 'result'.\n")

# --- 2. Solution A: Shared Memory (Value & Array) ---
# Best for simple data types (numbers, arrays of numbers).
# Fast, but limited types.

def worker_shared_memory(number, array):
    # number and array are special shared objects
    # We access the value via the .value attribute
    with number.get_lock(): # Best practice to use lock for atomic updates
        number.value += 1
    
    # Arrays are thread/process-safe for individual index access
    for i in range(len(array)):
        array[i] *= 2

def run_shared_memory_demo():
    print("--- Demo: Shared Memory (Value & Array) ---")
    # 'i' = integer, 'd' = double (float)
    shared_number = multiprocessing.Value('i', 10)
    shared_array = multiprocessing.Array('i', [1, 2, 3])

    p = multiprocessing.Process(target=worker_shared_memory, args=(shared_number, shared_array))
    p.start()
    p.join()

    print(f"Shared Number: {shared_number.value}")
    print(f"Shared Array: {list(shared_array)}")
    print()

# --- 3. Solution B: Server Process (Manager) ---
# Best for complex data types (List, Dict).
# Slower than shared memory, but more flexible.

def worker_manager(shared_list, shared_dict):
    shared_list.append("New Item")
    shared_dict["status"] = "Updated"

def run_manager_demo():
    print("--- Demo: Manager (List & Dict) ---")
    with multiprocessing.Manager() as manager:
        # Create shared objects using the manager
        shared_list = manager.list(["Init"])
        shared_dict = manager.dict({"status": "Original"})

        p = multiprocessing.Process(target=worker_manager, args=(shared_list, shared_dict))
        p.start()
        p.join()

        # Note: We must print/use data inside the 'with' block or convert to standard types
        # because the manager shuts down when exiting the block.
        print(f"Shared List: {shared_list}")
        print(f"Shared Dict: {shared_dict}")

if __name__ == "__main__":
    run_fail_demo()
    run_shared_memory_demo()
    run_manager_demo()