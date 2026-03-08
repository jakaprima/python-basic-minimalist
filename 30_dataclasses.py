# TUTORIAL: Dataclasses (Modern OOP)
# Cara modern dan ringkas membuat class yang tujuan utamanya menyimpan data.
# Otomatis membuat __init__, __repr__, __eq__, dll.

from dataclasses import dataclass

# --- Cara Lama (Boilerplate banyak) ---
class ProdukLama:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    
    def __repr__(self):
        return f"ProdukLama(nama={self.nama}, harga={self.harga})"

# --- Cara Modern (Dataclass) ---
@dataclass
class Produk:
    nama: str
    harga: int
    stok: int = 0  # Default value

    def total_aset(self) -> int:
        return self.harga * self.stok

# Penggunaan
p1 = Produk("Laptop", 15000000, 5)
p2 = Produk("Mouse", 100000, 10)
p3 = Produk("Laptop", 15000000, 5)

# 1. Otomatis punya representasi string yang bagus (__repr__)
print(p1) 
# Output: Produk(nama='Laptop', harga=15000000, stok=5)

# 2. Otomatis bisa dibandingkan (__eq__)
print(f"Apakah p1 sama dengan p3? {p1 == p3}") # True (karena isinya sama)
print(f"Total aset p1: {p1.total_aset()}")