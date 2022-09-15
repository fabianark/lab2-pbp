# Tugas 2 PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Aplikasi Heroku (Katalog)

https://ark-tugas2pbp.herokuapp.com/katalog/

## Jawaban Pertanyaan

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan
   tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa
   menggunakan virtual environment?

   Virtual environment digunakan dalam melakukan pemrograman agar bisa memisahkan implementasi suatu proyek dari sistem operasi yang dimiliki oleh local host yang dipakai oleh si pembuat program. Tujuannya adalah untuk membedakan versi software yang digunakan dalam mengembangkan suatu proyek. Misalkan, kita ingin membuat suatu aplikasi yang berbasis python 3.8, padahal sistem yang kita gunakan menggunakan python 3.10, maka daripada kita mengubah versi python yang ada pada sistem device yang dipakai akan lebih mudah jika kita membuat suatu virtual environment yang dikhususkan untuk proyek yang saat ini kita kerjakan sehingga kita lebih leluasa dalam menginstall software-software yang dibutuhkan untuk membuat suatu proyek pemrograman. Selain itu, virtual environment juga menghindari terjadinya kerusakan atau error pada sistem yang kita pakai ketika menjalankan testing suatu proyek. Walaupun begitu, sebenarnya kita tetap dapat bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi hal tersebut tidak dianjurkan karena alasan-alasan yang sudah disebutkan sebelumnya. Jadi, menggunakan virtual environment merupakan best practice dalam mengembangkan aplikasi web berbasis Django.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

   1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam
      sebuah HTML.

      Mendefinisikan suatu fungsi show_items() dengan parameter suatu request dan menyimpan dictionary response yang berisi list item yang ada di class CatalogItem, nama mahasiswa, dan NPM. Response tersebut kemudian ditampilkan di katalog.html

   2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.

      Menambahkan pattern url yang baru di urls.py, yaitu adalah path string kosong setelah /katalog (https://ark-tugas2pbp.herokuapp.com/katalog/) yang menunjuk ke fungsi show_items() di views.py

   3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.

      Melakukan iterasi tiap item pada CatalogItem dan mencetak atributnya sesuai urutan yang akan ditampilkan pada tabel, yaitu item_name, item_price, item_stock, ratings, description, dan item_url. Sintaks yang dipakai untuk menuliskan suatu variabel pada html adalah {{ var_name }}

   4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh
      teman-temanmu melalui Internet.

      Menambahkan secret pada setting repository di GitHub, yaitu app name Heroku yang akan di-deploy dan API key yang didapat dari account settings di Heroku. Setelah itu, melakukan proses add/stage, commit, dan push ke GitHub melalui source control di Visual Studio Code.

## Credits

TUGAS 2 PBP by ARK