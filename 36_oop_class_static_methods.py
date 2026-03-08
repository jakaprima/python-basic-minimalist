# TUTORIAL: Class Method dan Static Method

class Kalkulator:
    """Contoh class dengan berbagai jenis method."""
    
    # Ini adalah instance method biasa.
    # Butuh `self` untuk mengakses data instance.
    def tambah(self, a, b):
        print(f"Menjalankan instance method tambah: {a} + {b}")
        return a + b

    # Ini adalah class method.
    # Ditandai dengan @classmethod dan menerima `cls` (class itu sendiri) sebagai argumen pertama.
    # Berguna untuk factory method, yaitu method yang membuat instance class dengan cara tertentu.
    @classmethod
    def dari_string_angka(cls, string_angka):
        """Membuat instance dari string seperti '5,3'."""
        a, b = map(int, string_angka.split(','))
        # cls() sama seperti memanggil Kalkulator()
        instance = cls()
        print(f"Class method membuat instance dari string '{string_angka}'")
        return instance, a, b

    # Ini adalah static method.
    # Ditandai dengan @staticmethod. Tidak menerima `self` atau `cls`.
    # Seperti fungsi biasa yang "menumpang" di dalam class.
    # Berguna untuk utility function yang berhubungan dengan class tapi tidak butuh data instance/class.
    @staticmethod
    def info():
        """Memberikan informasi tentang class ini."""
        return "Ini adalah class Kalkulator sederhana."

# --- Penggunaan ---

# 1. Static method bisa dipanggil tanpa membuat instance
print(Kalkulator.info())

# 2. Class method untuk membuat instance dari string
k, angka1, angka2 = Kalkulator.dari_string_angka("10,5")

# 3. Instance method dipanggil dari instance yang sudah ada
hasil = k.tambah(angka1, angka2)
print(f"Hasilnya: {hasil}")