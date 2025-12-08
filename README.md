| Nama                | NRP        | Kelas
| --- | --- | --- |
| Devina Balqis Aurora | 5025241034 | D |
| Via Hana Nurma Putri | 5025241048 |  D |

# Tugas Praktikum Teori Graf

## Knight's Tour Problem
Mencari lintasan langkah kuda yang mampu mengunjungi semua 64 petak tepat satu kali pada papan catur 8x8. Kuda dapat ditempatkan di petak awal mana saja, lalu dicari urutan langkah sampai seluruh petak terlewati.
Lintasan bisa bersifat:
- Open tour: langkah terakhir boleh di kotak mana saja.
- Closed tour: langkah terakhir harus berada di kotak yang satu langkah kuda dari kotak awal.

### Konsep & Algoritma yang Digunakan
Program akan menyelesaikan Knight’s Tour dengan memodelkan papan catur sebagai matriks 8×8, di mana setiap petak berisi 0 jika belum dikunjungi dan 1–64 sebagai urutan langkah kuda. 
Gerakan kuda direpresentasikan sebagai delapan kombinasi perpindahan baris–kolom sesuai pola langkah kuda pada permainan catur (L).

Algoritma yang digunakan adalah backtracking yang dipandu heuristik Warnsdorff dengan alur penyelesaian sebagai berikut:
-  Mulai dari petak awal, beri nomor langkah 1.
- Dari posisi sekarang, cari semua langkah kuda yang masih di dalam papan dan belum pernah dikunjungi.
- Untuk setiap kandidat, hitung berapa banyak langkah lanjutan yang masih mungkin (degree).
- Pilih dan kunjungi terlebih dahulu petak dengan degree paling kecil (Warnsdorff’s Rule).
- Ulangi proses hingga semua 64 petak terisi.
- Untuk closed tour, setelah langkah ke-64 dicek apakah posisi terakhir masih satu langkah kuda dari petak awal.
  
Jika suatu jalur buntu sebelum semua petak terkunjungi, program melakukan backtracking dan mencoba alternatif jalur yang lain.
