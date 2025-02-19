import random
# Mengimpor modul random, yang menyediakan berbagai fungsi untuk menghasilkan angka acak dan pilihan acak dari list.
def sapa_acak():
# Mendefinisikan sebuah fungsi baru dengan nama sapa_acakFungsi ini tidak menerima argumen dan berfungsi untuk menghasilkan sapaan acak.

 sapaan = ["Assalamualaikum", "Halo", "Selamat pagi"]
# Membuat list bernama sapaan yang berisi tiga pilihan sapaan dalam bahasa Indonesia. digunakan dalam proses pemilihan acak.
nama = ["teman-teman", "kawan", "rekan-rekan", "sobat"]
#Mendefinisikan list bernama nama yang berisi beberapa istilah untuk menyapa sekelompok orang.untuk dipilih secara acak
pilihan_sapaan = random.choice(sapaan)
# random.choice() dari modul random untuk memilih satu elemen secara acak dari list sapaan. Hasilnya disimpan dalam variabel pilihan_sapaan.
pilihan_nama = random.choice(nama)
# fungsi random.choice() digunakan untuk memilih satu elemen acak dari list nama,disimpan dalam variabel pilihan_nama.

pesan = f"{pilihan_sapaan}, {pilihan_nama}! Semangat belajar Python!"
# Variabel pesan akan berisi kalimat sapaan yang siap ditampilkan, misalnya "Halo, teman-teman! Semangat belajar Python!".
return pesan
# Mengembalikan nilai dari variabel pesan saat fungsi sapa_acak dipanggil.

 print(sapa_acak())
# Memanggil fungsi sapa_acak dan mencetak hasil yang dikembalikan oleh fungsi tersebut ke konsol.