# TUTORIAL: Module `random`
# Module ini digunakan untuk menghasilkan angka acak dan memilih data secara acak.
# Sangat berguna untuk game, simulasi, testing, atau kriptografi sederhana.

import random

# --- 1. Menghasilkan Angka Acak ---

print("--- 1. Angka Acak ---")

# a. random(): Float antara 0.0 s/d 1.0
print(f"random(): {random.random()}")

# b. randint(min, max): Integer antara min s/d max (inklusif)
print(f"randint(1, 10): {random.randint(1, 10)}")

# c. uniform(min, max): Float antara min s/d max
print(f"uniform(1.5, 5.5): {random.uniform(1.5, 5.5)}")


# --- 2. Memilih dari Sequence (List/Tuple/String) ---

buah = ["Apel", "Jeruk", "Mangga", "Pisang", "Anggur"]
print(f"\nList Buah: {buah}")

print("\n--- 2. Pilihan Acak ---")

# a. choice(): Memilih SATU elemen secara acak
pilihan = random.choice(buah)
print(f"choice(): {pilihan}")

# b. choices(): Memilih k elemen DENGAN pengembalian (bisa kembar)
#    Berguna untuk gacha atau simulasi dadu.
pilihan_banyak = random.choices(buah, k=3)
print(f"choices(k=3): {pilihan_banyak}")

# c. sample(): Memilih k elemen TANPA pengembalian (unik)
#    Berguna untuk lotre atau pembagian tim.
sample_unik = random.sample(buah, k=3)
print(f"sample(k=3): {sample_unik}")


# --- 3. Mengacak Urutan (Shuffle) ---

print("\n--- 3. Shuffle ---")
# shuffle() mengubah list asli (in-place)
kartu = [1, 2, 3, 4, 5]
print(f"Sebelum shuffle: {kartu}")
random.shuffle(kartu)
print(f"Sesudah shuffle: {kartu}")


# --- 4. Seed (Reproducibility) ---
# Jika kita set seed, urutan acak akan selalu sama setiap kali program dijalankan.
# Sangat penting untuk debugging atau machine learning.

print("\n--- 4. Random Seed ---")
random.seed(42)
print(f"Angka acak dengan seed 42 (1): {random.random()}")
print(f"Angka acak dengan seed 42 (2): {random.random()}")

random.seed(42)
print(f"Angka acak dengan seed 42 (1) lagi: {random.random()} (Sama persis!)")