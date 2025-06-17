# data_siswa.py

# data dalam  dictionary
siswa = {
    "nama" : "Alya",
    "umur" : 17,
    "nilai" : [85, 90, 98],
    "alamat" : ("Jakarta", "Indonesia")
}
# Menampilkan data

print("==== DATA SISWA ====")
print("Nama :", siswa["Alya"])
print("Umur :", siswa["17"])
print("Nilai", siswa["85, 90,88"])
print("Alamat", siswa[0]) + "," + siswa[1]

#Hitung Rata Rata
sum(siswa["85, 90,88"]) / len(siswa["85, 90, 88"])

#logika kelulusan
if rata_rata >= 75:
    print("status : lulus")
else :
    print("status : tidak lulus")
