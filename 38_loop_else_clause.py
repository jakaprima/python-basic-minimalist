# TUTORIAL: Klausa `else` pada Loop
# Python memiliki fitur unik di mana `for` dan `while` loop bisa memiliki klausa `else`.
# Blok `else` akan dieksekusi HANYA jika loop selesai secara normal
# (tidak dihentikan oleh `break`).

# --- Contoh 1: `for...else` ---
# Mencari bilangan prima

print("--- Mencari bilangan prima dengan for...else ---")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} sama dengan {x} * {n//x}")
            break  # Loop dihentikan, `else` tidak akan jalan
    else:
        # Loop selesai tanpa menemukan faktor, artinya ini bilangan prima
        print(f"{n} adalah bilangan prima")

# --- Contoh 2: `while...else` ---
# Game tebak angka dengan batas percobaan

print("\n--- Game tebak angka dengan while...else ---")
angka_rahasia = 7
percobaan = 3
while percobaan > 0:
    tebakan = int(input(f"Tebak angka (sisa {percobaan} percobaan): "))
    if tebakan == angka_rahasia:
        print("Selamat, tebakanmu benar!")
        break # Loop dihentikan, `else` tidak akan jalan
    percobaan -= 1
else:
    # Loop selesai karena percobaan habis (bukan karena `break`)
    print("Maaf, kesempatanmu habis. Kamu gagal.")