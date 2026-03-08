# TUTORIAL: Race Conditions and Locks in Threading

import threading
import time

# --- The Problem: Race Condition ---
# A race condition occurs when multiple threads access a shared resource (like this counter)
# at the same time, leading to unpredictable and incorrect results.

# Shared resource
counter_unsafe = 0

def increment_counter_unsafe():
    global counter_unsafe
    # This operation is NOT atomic. It's three steps:
    # 1. Read the current value of 'counter_unsafe'.
    # 2. Add 1 to that value.
    # 3. Write the new value back to 'counter_unsafe'.
    # A thread can be interrupted by the OS between any of these steps!
    
    current_value = counter_unsafe
    current_value += 1
    time.sleep(0.001)  # A small delay to make the race condition more likely
    counter_unsafe = current_value

def run_race_condition_demo():
    print("--- Demonstrating a Race Condition ---")
    threads = []
    for _ in range(100):
        t = threading.Thread(target=increment_counter_unsafe)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Expected counter value: 100")
    print(f"Actual counter value: {counter_unsafe}")
    print("The actual value is lower because threads overwrote each other's work.\n")


# --- The Solution: Locks ---
# A Lock (also called a mutex) ensures that only one thread can execute a
# specific block of code (the "critical section") at a time.

counter_safe = 0
lock = threading.Lock()  # Create a lock object

def increment_counter_safe():
    global counter_safe
    
    # The 'with' statement is the best practice for using locks.
    # It automatically acquires the lock when entering the block
    # and releases it when exiting, even if an error occurs.
    with lock:
        # --- Critical Section Start ---
        # Only one thread can be in this block at any given time.
        current_value = counter_safe
        current_value += 1
        time.sleep(0.001)
        counter_safe = current_value
        # --- Critical Section End ---

def run_lock_demo():
    global counter_safe
    counter_safe = 0  # Reset for the demo
    print("--- Demonstrating a Lock to Prevent Race Conditions ---")
    threads = []
    
    for _ in range(100):
        t = threading.Thread(target=increment_counter_safe)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Expected counter value: 100")
    print(f"Actual counter value: {counter_safe}")
    print("The value is correct because the lock prevented threads from interfering.")


if __name__ == "__main__":
    run_race_condition_demo()
    run_lock_demo()