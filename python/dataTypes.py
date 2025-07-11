# TEXT TYPE
print("===== TEXT (str) =====")
nama = "Radya"
print("Nama:", nama)

# NUMERIC TYPES
print("\n===== NUMERIC =====")
umur = 20                      # int
tinggi = 1.75                  # float
z = 3 + 4j                     # complex
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Bilangan kompleks:", z)
print("Bagian real:", z.real)
print("Bagian imajiner:", z.imag)

# SEQUENCE TYPES
print("\n===== SEQUENCE =====")
list_hobi = ["coding", "gaming", "makan"]
tuple_hari = ("Senin", "Selasa", "Rabu")
range_angka = range(1, 4)
print("List hobi:", list_hobi)
print("Tuple hari:", tuple_hari)
print("Range angka:", list(range_angka))

# MAPPING TYPE
print("\n===== MAPPING (dict) =====")
mahasiswa = {
    "nama": "Radya",
    "umur": 20,
    "jurusan": "Informatika"
}
print("Data mahasiswa:", mahasiswa)
print("Nama mahasiswa:", mahasiswa["nama"])

# SET TYPES
print("\n===== SET =====")
set_unik = {1, 2, 3, 3, 2}
frozenset_unik = frozenset([1, 2, 3, 3, 2])
print("Set (otomatis unik):", set_unik)
print("Frozenset:", frozenset_unik)

# BOOLEAN TYPE
print("\n===== BOOLEAN =====")
lulus = True
print("Apakah lulus?", lulus)

# BINARY TYPES
print("\n===== BINARY =====")
data_byte = b"Halo"
data_bytearray = bytearray(b"Halo")
data_memoryview = memoryview(data_byte)
print("Bytes:", data_byte)
print("Bytearray:", data_bytearray)
print("Memoryview (byte pertama):", data_memoryview[0])
print("Memoryview:", data_memoryview)

# NONE TYPE
print("\n===== NONE =====")
nilai = None
print("Nilai belum diisi:", nilai)
