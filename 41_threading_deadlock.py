# TUTORIAL: Deadlocks in Threading

import threading
import time

# --- The Problem: Deadlock ---
# A deadlock is a situation where two or more threads are blocked forever,
# waiting for each other to release the resources (locks) that they need.

# Let's simulate two critical resources, like a hammer and a drill.
hammer_lock = threading.Lock()
drill_lock = threading.Lock()

def worker_alex_deadlock():
    """Alex acquires the hammer, then the drill."""
    print("Alex: Mencoba mengambil palu...")
    hammer_lock.acquire()
    print("Alex: Berhasil mengambil palu.")
    
    time.sleep(1) # Simulate some work, giving Ben time to grab the drill
    
    print("Alex: Mencoba mengambil bor...")
    # This line will block if Ben has the drill
    drill_lock.acquire()
    print("Alex: Berhasil mengambil bor.")
    
    # Release locks
    drill_lock.release()
    hammer_lock.release()
    print("Alex: Selesai dan melepaskan semua alat.")

def worker_ben_deadlock():
    """Ben causes a deadlock by acquiring the drill, then the hammer."""
    print("Ben: Mencoba mengambil bor...")
    drill_lock.acquire()
    print("Ben: Berhasil mengambil bor.")
    
    time.sleep(1) # Simulate some work
    
    print("Ben: Mencoba mengambil palu...")
    # This line will block forever because Alex is holding the hammer
    # and waiting for Ben to release the drill. DEADLOCK!
    hammer_lock.acquire()
    print("Ben: Berhasil mengambil palu.")
    
    # Release locks
    hammer_lock.release()
    drill_lock.release()
    print("Ben: Selesai dan melepaskan semua alat.")

def run_deadlock_demo():
    print("--- Demonstrating a Deadlock ---")
    print("Program akan 'hang' dan Anda perlu menghentikannya secara manual (Ctrl+C).\n")
    
    t1 = threading.Thread(target=worker_alex_deadlock)
    t2 = threading.Thread(target=worker_ben_deadlock)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Selesai demo deadlock. (Pesan ini tidak akan pernah tercetak)")

# --- The Solution: Lock Ordering ---
# The rule: Always acquire the hammer_lock BEFORE the drill_lock.

def worker_ben_safe():
    """Ben avoids deadlock by following the lock order rule."""
    print("Ben (Aman): Mencoba mengambil palu...")
    hammer_lock.acquire() # Follows the rule: hammer first
    print("Ben (Aman): Berhasil mengambil palu.")
    
    time.sleep(1)
    
    print("Ben (Aman): Mencoba mengambil bor...")
    drill_lock.acquire() # Then drill
    print("Ben (Aman): Berhasil mengambil bor.")
    
    # Release locks (order of release doesn't matter as much, but reverse is good practice)
    drill_lock.release()
    hammer_lock.release()
    print("Ben (Aman): Selesai dan melepaskan semua alat.")

def run_safe_demo():
    print("\n--- Demonstrating Deadlock Avoidance (Lock Ordering) ---")
    t1 = threading.Thread(target=worker_alex_deadlock) # Alex's code is already correct
    t2 = threading.Thread(target=worker_ben_safe)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Selesai demo aman. Semua proses berjalan dengan lancar.")

if __name__ == "__main__":
    # run_deadlock_demo() # Uncomment this to see the deadlock in action
    run_safe_demo()