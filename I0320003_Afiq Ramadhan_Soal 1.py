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
print("Diagonal sisi depan aquarium : ", format(diagonal_sisi_depan,'.3f'))
print("Diagonal sisi samping aquarium : ", format(diagonal_sisi_samping,'.3f'))
print("Diagonal sisi bawah aquarium : ", format(diagonal_sisi_bawah,'.3f'))
print("Diagonal ruang aquarium : ", format(diagonal_ruang,'.3f'))
print("Luas permukaan depan aquarium : ", format(luas_permukaan_depan,'.3f'))
print("Luas permukaan samping aquarium : ", format(luas_permukaan_samping,'.3f'))
print("Luas permukaan bawah aquarium : ", format(luas_permukaan_bawah,'.3f'))
print("Luas permukaan total aquarium : ", format(luas_permukaan_total,'.3f'))