# memasukkan data yang diketahui di soal
p = 11.5
l = 1.99
t = 25.87

# memproses data berdasarkan pertanyaan
diagonal_sisi_depan = ((p**2) + (t**2))**0.5
diagonal_sisi_samping = ((l**2) + (t**2))**0.5
diagonal_sisi_bawah = ((p**2) + (l**2))**0.5
diagonal_ruang = ((diagonal_sisi_bawah**2) + (t**2))**0.5
luas_permukaan_depan = (p*t)
luas_permukaan_samping = (l*t)
luas_permukaan_bawah = (p*l)
luas_permukaan_total = ((2*luas_permukaan_depan + 2*luas_permukaan_samping + luas_permukaan_bawah))

# menampilkan hasil perhitungan
print("Diagonal sisi depan aquarium : ", diagonal_sisi_depan)
print("Diagonal sisi samping aquarium : ", diagonal_sisi_samping)
print("Diagonal sisi bawah aquarium : ", diagonal_sisi_bawah)
print("Diagonal ruang aquarium : ", diagonal_ruang)
print("Luas permukaan depan aquarium : ", luas_permukaan_depan)
print("Luas permukaan samping aquarium : ", luas_permukaan_samping)
print("Luas permukaan bawah aquarium : ", luas_permukaan_bawah)
print("Luas permukaan total aquarium : ", luas_permukaan_total)