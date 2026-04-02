total_hari = int(input("Masukkan jumlah hari proyek : "))

tahun = total_hari // 365
sisa_setelah_tahun = total_hari % 365
bulan = sisa_setelah_tahun // 30
hari = sisa_setelah_tahun % 30

print("_" * 30)
print(f"Hasil konversi untuk {total_hari} hari:")
print(f"Tahun : {tahun}")
print(f"Bulan : {bulan}")
print(f"Hari  : {hari}")
print("_" * 30)