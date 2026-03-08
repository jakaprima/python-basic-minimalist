# TUTORIAL: @property Decorator (Getters, Setters, Deleters)
# @property mengubah method class menjadi "managed attribute".
# Ini memungkinkan kita menambahkan logika (validasi, komputasi) saat
# sebuah atribut diakses, diubah, atau dihapus, tanpa mengubah cara pemanggilannya.

class Produk:
    """
    Class Produk dengan harga yang di-manage oleh @property.
    """
    def __init__(self, harga: float):
        # Atribut internal, diawali underscore sebagai konvensi "private".
        # Setter akan dipanggil saat inisialisasi.
        self.harga = harga

    # 1. GETTER: Mengubah method `harga` menjadi atribut yang bisa dibaca.
    # Dipanggil saat kita melakukan: `print(produk.harga)`
    @property
    def harga(self) -> float:
        """Mendapatkan nilai harga."""
        print("-> Getter dipanggil...")
        return self._harga

    # 2. SETTER: Dipanggil saat kita melakukan assignment.
    # `produk.harga = 1500`
    @harga.setter
    def harga(self, nilai_baru: float):
        """Melakukan validasi sebelum mengubah nilai harga."""
        print(f"-> Setter dipanggil dengan nilai {nilai_baru}...")
        if not isinstance(nilai_baru, (int, float)):
            raise TypeError("Harga harus berupa angka.")
        if nilai_baru < 0:
            raise ValueError("Harga tidak boleh negatif!")
        self._harga = nilai_baru

    # 3. DELETER: Dipanggil saat kita melakukan `del`.
    # `del produk.harga`
    @harga.deleter
    def harga(self):
        """Mereset harga ke 0 saat dihapus."""
        print("-> Deleter dipanggil...")
        self._harga = 0

# --- Demo Penggunaan ---
if __name__ == "__main__":
    print("--- Membuat instance Produk ---")
    # Saat membuat instance, __init__ memanggil `self.harga = 1000`,
    # yang secara otomatis memicu SETTER.
    p = Produk(1000)

    print("\n--- Mengakses harga (memanggil GETTER) ---")
    print(f"Harga saat ini: {p.harga}")

    print("\n--- Mengubah harga (memanggil SETTER) ---")
    p.harga = 1500
    print(f"Harga baru: {p.harga}")

    print("\n--- Mencoba input tidak valid (memanggil SETTER) ---")
    try:
        p.harga = -50
    except ValueError as e:
        print(f"Error terdeteksi: {e}")

    print("\n--- Menghapus harga (memanggil DELETER) ---")
    del p.harga
    print(f"Harga setelah dihapus: {p.harga}")