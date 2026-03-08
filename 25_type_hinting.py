# TUTORIAL: Type Hinting (Modern Python)
# Membantu dokumentasi dan auto-completion di text editor.
# Catatan: Python tetap dynamic typing, ini hanya "petunjuk" (hint).

from typing import List, Dict, Optional, Union

# 1. Dasar Type Hinting pada Fungsi
# format -> def nama_fungsi(parameter: tipe) -> tipe_return:

def sapa_user(nama: str, umur: int) -> str:
    return f"Halo {nama}, umur kamu {umur} tahun."

# Editor akan memberi warning jika kita tulis: sapa_user("Budi", "duapuluh")
print(sapa_user("Budi", 20))


# 2. List dan Dictionary yang kompleks
def hitung_rata_rata(nilai: List[int]) -> float:
    return sum(nilai) / len(nilai)

scores = [80, 90, 100]
print(f"Rata-rata: {hitung_rata_rata(scores)}")


# 3. Optional dan Union
# Optional[str] artinya bisa string, bisa None
# Union[int, float] artinya bisa int atau float

def proses_data(data: Union[int, float], prefix: Optional[str] = None) -> str:
    if prefix:
        return f"{prefix}: {data}"
    return str(data)

print(proses_data(10.5, "Harga"))
print(proses_data(100))

# Tips Project:
# Gunakan Type Hinting terutama pada fungsi yang dipanggil oleh file lain.