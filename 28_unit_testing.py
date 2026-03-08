# TUTORIAL: Unit Testing dengan module `unittest`
# Unit testing adalah cara menguji bagian-bagian kecil (unit) dari kode secara terisolasi.

import unittest

# --- Kode yang akan kita tes ---
# Misalkan kita punya file `kalkulator.py` dengan fungsi ini.

def tambah(a, b):
    """Fungsi untuk menjumlahkan dua angka."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Input harus berupa angka")
    return a + b

def kurang(a, b):
    """Fungsi untuk mengurangkan dua angka."""
    return a - b

# --- Script untuk testing ---
# Biasanya ini dibuat di file terpisah, misal `test_kalkulator.py`

class TestKalkulator(unittest.TestCase):

    # Nama method harus diawali dengan 'test_'
    def test_tambah(self):
        """Test untuk fungsi tambah."""
        self.assertEqual(tambah(5, 3), 8)       # 5 + 3 harusnya 8
        self.assertEqual(tambah(-1, 1), 0)      # -1 + 1 harusnya 0
        self.assertEqual(tambah(2.5, 2.5), 5.0) # Test dengan float

    def test_tambah_error_tipe_data(self):
        """Test jika input bukan angka, harusnya error."""
        # `assertRaises` memeriksa apakah error tertentu muncul saat fungsi dipanggil.
        with self.assertRaises(TypeError):
            tambah("dua", 3)

# Baris ini membuat script test bisa dijalankan langsung dari terminal
if __name__ == '__main__':
    unittest.main()