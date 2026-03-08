# TUTORIAL: Advanced *args and **kwargs
# *args dan **kwargs memungkinkan fungsi menerima jumlah argumen yang dinamis.
# Ini sangat penting untuk membuat kode yang fleksibel, decorator, dan inheritance.

# --- 1. Konsep Dasar (Review) ---

def jumlahkan_semua(*args):
    # args menjadi tuple: (1, 2, 3, ...)
    return sum(args)

def info_user(**kwargs):
    # kwargs menjadi dictionary: {'nama': 'Jaka', 'umur': 25}
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

print("--- 1. Basic Usage ---")
print(f"Sum: {jumlahkan_semua(1, 2, 3, 4, 5)}")
info_user(nama="Jaka", role="Admin", status="Active")


# --- 2. Ordering Rules (Aturan Urutan) ---
# Urutan wajib: (params biasa, *args, default/named params, **kwargs)
# Note: Parameter setelah *args menjadi "Keyword-Only Arguments".

def fungsi_kompleks(a, b, *args, mode="default", **kwargs):
    print(f"\na={a}, b={b}")
    print(f"args={args} (Sisa positional)")
    print(f"mode={mode} (Keyword-only)")
    print(f"kwargs={kwargs} (Sisa keyword)")

print("\n--- 2. Argument Ordering ---")
# 1, 2 masuk ke a, b
# 3, 4, 5 masuk ke *args
# mode="turbo" masuk ke mode
# setting="ON" masuk ke **kwargs
fungsi_kompleks(1, 2, 3, 4, 5, mode="turbo", setting="ON", target="CPU")


# --- 3. Unpacking Arguments (Spread Operator) ---
# Kita bisa menggunakan * dan ** untuk "membongkar" list/dict menjadi argumen fungsi.

def hitung_volume(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

ukuran_list = [10, 5, 2]
ukuran_dict = {"panjang": 10, "lebar": 5, "tinggi": 2}

print("\n--- 3. Unpacking ---")
# Tanpa unpacking: hitung_volume(ukuran_list[0], ukuran_list[1], ...)
# Dengan unpacking (*):
print(f"Volume (List Unpack): {hitung_volume(*ukuran_list)}")
# Dengan unpacking (**):
print(f"Volume (Dict Unpack): {hitung_volume(**ukuran_dict)}")


# --- 4. Real World Case 1: Decorators / Wrapper ---
# *args dan **kwargs sangat penting saat membuat wrapper function
# agar bisa menerima argumen APAPUN yang dimiliki fungsi aslinya.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Memanggil {func.__name__} dengan args={args} kwargs={kwargs}")
        result = func(*args, **kwargs) # Forwarding arguments apa adanya
        print(f"[LOG] Hasil: {result}")
        return result
    return wrapper

@logger
def register_user(username, email, is_admin=False):
    return f"User {username} registered."

print("\n--- 4. Wrapper/Decorator ---")
register_user("jaka_code", "jaka@email.com", is_admin=True)


# --- 5. Real World Case 2: Subclassing & Super() ---
# Meneruskan argumen ke parent class tanpa perlu tahu detail parameternya.

class Kendaraan:
    def __init__(self, merk, model):
        self.merk = merk
        self.model = model

class MobilListrik(Kendaraan):
    def __init__(self, battery_capacity, *args, **kwargs):
        self.battery_capacity = battery_capacity
        # Teruskan sisa argumen ke parent (Kendaraan)
        # MobilListrik tidak perlu tahu kalau Kendaraan butuh 'merk' dan 'model'
        super().__init__(*args, **kwargs)

print("\n--- 5. Subclassing ---")
# Kita bisa pass merk & model sebagai keyword arguments
tesla = MobilListrik(battery_capacity="100kWh", merk="Tesla", model="Model S")
print(f"Mobil: {tesla.merk} {tesla.model}, Baterai: {tesla.battery_capacity}")