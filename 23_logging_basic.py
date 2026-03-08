import logging

# Konfigurasi logging
# level=logging.DEBUG artinya semua pesan dari level debug ke atas akan dicatat
# format menentukan tampilan pesan log
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def pembagian(a, b):
    logging.info(f"Mencoba membagi {a} dengan {b}")
    try:
        hasil = a / b
        logging.info("Pembagian berhasil")
        return hasil
    except ZeroDivisionError:
        logging.error("Error: Tidak bisa membagi dengan nol!")
        return None

print(pembagian(10, 2))
print("---")
print(pembagian(10, 0))
