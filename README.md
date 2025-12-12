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

## Largest Monotonically Increasing Subsequence (LMIS)
Mencari subsequence naik terpanjang dari suatu urutan bilangan. Subsequence berarti elemen diambil dari deret asal tanpa mengubah urutan, tetapi boleh loncat indeks. Syarat “monotonically increasing” artinya setiap elemen berikutnya harus lebih besar dari elemen sebelumnya.

Contoh (sesuai soal):
<br>
Urutan: 4, 1, 13, 7, 0, 2, 8, 11, 3
<br>
Salah satu LMIS: [4, 7, 8, 11] 
<br>
(panjang = 4)

## Konsep & Algoritma yang Digunakan
Program menyelesaikan LMIS dengan memodelkan proses pencarian sebagai state space tree:
- Root: subsequence masih kosong.
- Cabang: memilih sebuah angka pada indeks tertentu yang memenuhi syarat lebih besar dari angka terakhir yang dipilih.
- Node: representasi subsequence sementara yang sedang dibangun.
- Pencarian hanya maju ke kanan (indeks lebih besar), supaya urutan subsequence tetap sesuai deret awal.

Algoritma yang digunakan adalah backtracking dengan alur penyelesaian:
- Mulai dari indeks 0 dengan last_val = -∞ dan current_seq = [].
- Telusuri semua elemen dari start_idx sampai akhir.
- Jika arr[i] > last_val, maka elemen tersebut boleh dipilih:
  tambahkan ke current_seq
  lanjut rekursi dari indeks i + 1 dengan last_val = arr[i]
- Setiap kali panjang current_seq lebih besar dari best_seq, program menyimpan sebagai jawaban terbaik sementara.
- Jika sudah tidak ada pilihan yang valid dari posisi tertentu, program melakukan backtrack (menghapus pilihan terakhir) lalu mencoba cabang lain.

Jika ada beberapa subsequence dengan panjang sama, program akan mengembalikan subsequence terbaik yang pertama kali ditemukan sesuai urutan eksplorasi backtracking.

