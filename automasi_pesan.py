import pywhatkit as kit

# Ganti dengan nomor telepon tujuan dan pesan
phone_number = "+62xxxxxxxxxx"  # Format: +62 untuk Indonesia
message = "Hello! This is a test message sent using pywhatkit."
hour = 16  # Jam dalam format 24-jam
minute = 8  # Menit (pastikan beberapa menit ke depan dari waktu saat ini)

try:
    # Mengirim pesan WhatsApp
    kit.sendwhatmsg(phone_number, message, hour, minute)
    print("Pesan berhasil dijadwalkan!")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")

