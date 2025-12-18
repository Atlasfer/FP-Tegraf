# FP TEORI GRAF

### Kelompok 15 :
1. Ahmad Habibie Dewa Pratama (5053241019)
2. Muhammad Zaki Alfikri (5053241034)
3. Ledwino Galih Wandanu (5053241017)

## The Knight's Tour
### Algoritma: Warnsdorff's Rule
1. Kuda selalu berpindah ke petak kosong yang memiliki jumlah gerakan lanjutan paling sedikit (derajat terendah)
2. Strategi ini secara drastis mengurangi kemungkinan kuda terjebak di sudut atau tepi papan, sehingga solusi ditemukan hampir seketika

### Cara Penggunaan
1. Jalankan kode python The Knight's Tour
2. Masukkan koordinat awal baris dan kolom (0-7)
3. Pilih jenis: 1 untuk Open Tour atau 2 untuk Closed Tour
4. Program menampilkan Output berupa visualisasi grafis

### Input
- Baris Awal (0-7): Indeks baris dimulainya kuda
- Kolom Awal (0-7): Indeks kolom dimulainya kuda
- Jenis Tur:
    - Open Tour (Berhenti disembarang tempat)
    - Closed Tour (Kembali ke titik awal)

### Output
Program akan menghasilkan output visualisasi grafis berupa:
- Papan Catur: Representasi visual papan 8 X 8 dengan warna yang selang-seling
- Nomor Urut: Setiap petak akan berisi angka (1-64) yang menunjukkan urutan kunjungan kuda
- Garis Jalur: Garis merah yang menghubungkan setiap langkah kuda
- Marker:
    - Bola Hijau: Titik awal
    - Bola Biru: Titik akhir
- Garis Putus-putus (Closed Tour): Menunjukkan koneksi dari langkah terakhir kembali ke langkah pertama

## Largest Monotonically Increasing Subsequence
### Algoritma 
1. Dynamic Programming (DP): Digunakan untuk menghitung panjang subsekuens maksimal yang berakhir di setiap indeks angka dan menyimpan daftar angka sebelumnya yang valid
2. Depth First Search (DFS): Digunakan untuk melakukan backtracking dari indeks akhir yang ditemukan untuk menyusun kembali semua kombinasi jalur yang mungkin

### Cara Penguunaan
1. Jalankan kode python Largest Monotonically Increasing Subsequence
2. Masukkan urutan angka
3. Program menampillkan hasil analisis L.M.I.S dari urutan angka yang dberikan

### Input
Urutan angka yang dipisahkan oleh spasi atau koma<br>
Contoh : 4, 1, 13, 7, 0, 2, 8, 11, 3

### Output
- Menampilkan kembali list angka yang dimasukkan
- Panjang L.M.I.S. berupa nilai numerik panjang barisan terpanjang
- Jumlah Variasi dari kombinasi jalur unik yang ditemukan
- List detail dari setiap variasi yang ditemukan