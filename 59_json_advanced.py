# TUTORIAL: JSON Lanjutan (Serializing Custom Objects)
# Secara default, module `json` tidak tahu cara mengubah custom object (class)
# menjadi format JSON. Kita perlu memberitahunya caranya.

import json

# --- 1. Custom Object yang akan kita serialize ---
class User:
    def __init__(self, name, email, is_active):
        self.name = name
        self.email = email
        self.is_active = is_active

    def __repr__(self):
        # Representasi string agar mudah dibaca
        return f"User(name='{self.name}', email='{self.email}')"

# --- 2. Masalah: TypeError saat mencoba dump custom object ---
user = User("Jaka", "jaka@example.com", True)

print("--- 1. Mencoba dump object secara langsung (akan gagal) ---")
try:
    json.dumps(user)
except TypeError as e:
    print(f"Gagal! Error: {e}\n")


# --- 3. Solusi A: Serialization dengan parameter `default` ---
# Kita membuat fungsi yang mengubah object kita menjadi dictionary.

def encode_user(obj):
    """Encoder function untuk object User."""
    if isinstance(obj, User):
        # Beritahu JSON cara mengubah User menjadi dict
        return {
            "__type__": "User", # Tambahkan penanda tipe
            "name": obj.name,
            "email": obj.email,
            "is_active": obj.is_active
        }
    # Jika bukan tipe User, biarkan default encoder yang handle
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

print("--- 2. Serialization dengan `default` ---")
user_json_string = json.dumps(user, default=encode_user, indent=4)
print("Hasil JSON String:")
print(user_json_string)


# --- 4. Solusi B: Deserialization dengan parameter `object_hook` ---
# Kita membuat fungsi yang mengubah dictionary kembali menjadi object User.

def decode_user(dct):
    """Decoder function untuk object User."""
    # Cek apakah dictionary ini adalah representasi dari User
    if "__type__" in dct and dct["__type__"] == "User":
        # Buat instance User dari dictionary
        return User(dct["name"], dct["email"], dct["is_active"])
    # Jika bukan, kembalikan dictionary apa adanya
    return dct

print("\n--- 3. Deserialization dengan `object_hook` ---")

# Mengubah JSON string kembali menjadi object Python
user_object_loaded = json.loads(user_json_string, object_hook=decode_user)

print(f"Object yang di-load: {user_object_loaded}")
print(f"Tipe object: {type(user_object_loaded)}")
print(f"Apakah object aktif? {user_object_loaded.is_active}")

# Alternatif lain yang lebih kompleks adalah membuat subclass dari
# json.JSONEncoder dan json.JSONDecoder untuk logika yang lebih reusable.