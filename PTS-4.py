def cek_ganjil_genap(n):
# Mendefinisikan fungsi bernama cek_ganjil_genap yang memerlukan satu parameter n. Fungsi ini berguna untuk menentukan apakah n adalah bilangan ganjil atau genap.

    return "Ganjil" if n % 2 != 0 else "Genap"
# Pernyataan ini menggunakan operator ternary. Jika n tidak habis dibagi 2 (n % 2 != 0), maka fungsi mengembalikan string "Ganjil". Jika sebaliknya (artinya n habis dibagi 2), maka mengembalikan string "Genap".
print(cek_ganjil_genap(7))
# Baris ini memanggil fungsi cek_ganjil_genap dengan argumen 7 dan mencetak hasilnya ke layar. Karena 7 adalah angka ganjil, maka akan mencetak "Ganjil".
print(cek_ganjil_genap(10))
#  Baris ini memanggil fungsi cek_ganjil_genap dengan argumen 10 dan mencetak hasilnya. Karena 10 adalah angka genap, maka akan mencetak "Genap".
# Dengan demikian, program ini secara keseluruhan berfungsi untuk mengecek dan mencetak apakah angka yang diberikan adalah ganjil atau genap.