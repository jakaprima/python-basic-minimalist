# TUTORIAL: 80 Data Transformation & Model Persistence
# Sebelum data dimasukkan ke model Machine Learning, ia harus diubah menjadi format numerik
# yang sesuai. Ini melibatkan:
# 1. Scaling: Mengubah skala data numerik (misal: Gaji, Umur).
# 2. Encoding: Mengubah data kategorikal menjadi angka (misal: 'Jakarta', 'Bandung').
# Setelah model dilatih, kita perlu menyimpannya agar bisa digunakan lagi nanti.

# Prasyarat: pip install pandas scikit-learn joblib

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# --- Setup Data Dummy ---
data = {
    'Pengalaman_Tahun': [1, 2, 3, 4, 5, 6, 7, 8],
    'Kota': ['Jakarta', 'Bandung', 'Jakarta', 'Surabaya', 'Bandung', 'Jakarta', 'Surabaya', 'Bandung'],
    'Gaji': [60, 75, 80, 95, 110, 120, 135, 150] # dalam Juta IDR
}
df = pd.DataFrame(data)

print("--- Data Awal ---")
print(df)

# Pisahkan fitur (X) dan target (y)
X = df.drop('Gaji', axis=1)
y = df['Gaji']

# --- 1. Data Transformation (Scaling & Encoding) ---
print("\n--- 1. Data Transformation ---")

# Tentukan kolom numerik dan kategorikal
numeric_features = ['Pengalaman_Tahun']
categorical_features = ['Kota']

# Buat "preprocessor" menggunakan ColumnTransformer
# Ini akan menerapkan transformer yang berbeda ke kolom yang berbeda.
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features), # Scaling untuk data numerik
        ('cat', OneHotEncoder(), categorical_features) # Encoding untuk data kategorikal
    ])

# StandardScaler: Mengubah data agar memiliki mean=0 dan std=1.
# OneHotEncoder: Mengubah 'Jakarta', 'Bandung' menjadi kolom-kolom biner [1,0], [0,1], dll.


# --- 2. Membuat Pipeline ---
# Pipeline menggabungkan langkah-langkah (preprocessor, model) menjadi satu.
# Ini sangat penting untuk mencegah "data leakage".

model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# --- 3. Melatih Model ---
print("\n--- 2. Melatih Model ---")

# Membagi data menjadi data latih dan data tes
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Melatih pipeline dengan data latih
model_pipeline.fit(X_train, y_train)

print("Model berhasil dilatih.")
score = model_pipeline.score(X_test, y_test)
print(f"Skor R^2 model pada data tes: {score:.2f}")


# --- 4. Menyimpan Model dengan Joblib ---
print("\n--- 3. Menyimpan Model (Persistence) ---")

# Joblib lebih efisien untuk menyimpan objek Python yang berisi array NumPy besar (seperti model scikit-learn).
model_filename = "gaji_predictor.joblib"
joblib.dump(model_pipeline, model_filename)

print(f"Pipeline model telah disimpan ke '{model_filename}'")


# --- 5. Memuat Model dan Membuat Prediksi Baru ---
print("\n--- 4. Memuat Model dan Prediksi ---")

if os.path.exists(model_filename):
    # Muat kembali pipeline yang sudah dilatih
    loaded_pipeline = joblib.load(model_filename)
    print("Pipeline model berhasil dimuat.")
    
    # Buat data baru untuk diprediksi
    data_baru = pd.DataFrame({
        'Pengalaman_Tahun': [10],
        'Kota': ['Jakarta']
    })
    
    print("\nData baru untuk prediksi:")
    print(data_baru)
    
    # Gunakan pipeline yang dimuat untuk prediksi
    # Pipeline akan otomatis menerapkan scaling dan encoding yang sama seperti saat latihan.
    prediksi_gaji = loaded_pipeline.predict(data_baru)
    
    print(f"\nPrediksi Gaji: {prediksi_gaji[0]:.2f} Juta IDR")

    # Cleanup
    os.remove(model_filename)
    print(f"\nFile model '{model_filename}' dihapus.")