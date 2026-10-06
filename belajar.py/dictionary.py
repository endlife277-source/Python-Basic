siswa = {
    "nama": "joko",
    "umur": 20,
    "kelas": "4A"
}

print(siswa)

print(siswa["nama"])

#mengubah nilai
siswa["umur"] = 21
print(siswa)

#menghapus key-value
del siswa["kelas"]
print(siswa)

#mengiterasi keys
for key in siswa:
    print(key, ":", siswa[key])

#mengiterasi key-value pairs
for key, value in siswa.items():
    print(key, "=", value)