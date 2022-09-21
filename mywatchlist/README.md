# Tugas 3 PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Aplikasi Heroku (Katalog)

https://ark-tugas2pbp.herokuapp.com/mywatchlist/

## Jawaban Pertanyaan

1. Jelaskan perbedaan antara JSON, XML, dan HTML!

   JSON (JavaScript Object Notation):
   - JSON adalah format untuk merepresentasikan objek data yang bersifat ringan
   - Data dalam format JSON bisa langsung di-parse dengan fungsi JavaScript parse()
   - Karena sifatnya yang ringan (lightweight), transfer data dalam format JSON lebih cepat daripada XML
   - JSON didesain khusus untuk data interchange
   - Secara umum, JSON juga lebih mudah untuk dibaca oleh manusia dibandingkan dengan XML
   - Support data berbentuk array
   - Hanya support UTF-8 encoding
   - Tidak menggunakan end tag

   XML (Extensible Markup Language):
   - XML adalah markup language yang digunakan untuk mendeskripsikan suatu data terstruktur dalam data encoding
   - Data dalam format XML harus di-parse menggunakan XML parser khusus
   - Ukuran datanya lebih besar dibandingkan dengan JSON, sehingga transfer data menjadi lebih lambat
   - XML didesain untuk melakukan banyak hal lain selain data interchange
   - XML agak lebih sulit untuk dibaca jika dibandingkan dengan JSON
   - Tidak support data berbentuk array
   - Support encoding UTF-8 dan UTF-16
   - Menggunakan start tag dan end tag

   HTML (Hypertext Markup Language):
   - HTML adalah markup language yang digunakan untuk mempresentasikan data dan teks dengan berbagai struktur dan layout
   - Tag dalam HTML sudah predefined (sudah didefinisikan secara built in), berbeda dengan XML dan JSON
   - Sifatnya case insensitive, sedangkan JSON dan XML case sensitive
   - Ada beberapa elemen yang tidak menggunakan closing tag, contohnya "br" atau break line
   - Data dapat dilakukan parsing dengan fungsi JavaScript eval()

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

   Dalam suatu platform (tidak hanya platform web), terutama yang memiliki data dinamis (dapat berubah seiring waktu), kita perlu melakukan data delivery untuk meng-update database atau menerima input data dari user. Proses mentransfer data dari client ke server adalah salah satu contoh data delivery. Misalkan saja, dalam aplikasi media sosial seperti Instagram, kita membuat postingan baru di akun kita. Ketika kita mempersiapkan untuk melakukan posting (memasukkan foto atau video, menulis caption, tag akun, dll.), Data post tersebut pada awalnya hanya disimpan di aplikasi smartphone kita. Namun, begitu kita klik tombol "Post", maka aplikasi akan mengirimkan data ke server Instagram agar data tersebut disimpan dalam akun Instagram kita yang terletak di server. Setelah itu, akun lain pun dapat melihat postingan kita karena data sudah tersimpan di server dan bukan hanya di device yang kita gunakan. Pada zaman sekarang, hampir seluruh platform menggunakan data dinamis dan tidak statis sehingga diperlukan update database seiring waktu menggunakan implementasi data delivery.

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    1. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu.

    Melakukan command "django-admin startapp mywatchlist" pada direktori repository Tugas 2 kemarin dalam virtual environment. Kemudian menambahkan mywatchlist ke installed apps di settings.py pada folder project_django.

    2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist.

    Menambahkan pattern URL di urls.py pada folder project_django dengan path "mywatchlist/" yang merujuk ke routing path yang ada di urls.py pada folder mywatchlist. Lalu, membuat variabel "app_name" dan "urlpatterns" pada file urls.py di folder mywatchlist. "app_name" yang digunakan adalah "mywatchlist". Pattern URL yang ditambahkan pertama kali adalah path "" (string kosong) yang akan mengarahkan pengguna ke homepage dari aplikasi mywatchlist dengan memanggil show_watchlist. Homepage tersebut berisi link-link yang mengarah ke tampilan data dalam HTML, tampilan data dalam XML, dan tampilan data dalam JSON.

    3. Membuat sebuah model MyWatchList yang memiliki atribut sebagai berikut: watched, title, rating, release_date, dan review.

    Membuat model class MyWatchlistItem di file models.py pada folder mywatchlist. Tipe data watched adalah boolean, title adalah char (max. 255 karakter), rating adalah float (nilai rating dalam skala 0-5), release_date adalah date, dan review adalah text.

    4. Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas.

    Membuat file initial_mywatchlist_data.json untuk memasukkan database secara lokal yang berada di folder fixtures. Menggunakan format JSON, ditambahkan 10 objek watchlist yang berisi datafield/atribut sesuai dengan yang ada di models.py. Data-data tersebut diambil dari https://www.imdb.com. Terakhir, tidak lupa untuk melakukan command "python manage.py loaddata initial_wishlist_data.json" untuk memasukkan data dari fixtures.

    5. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format: HTML, XML, dan JSON.

    Membuat fungsi show_watchlist_html untuk menampilkan data dalam format HTML, show_watchlist_xml untuk menampilkan data dalam format XML, show_watchlist_json untuk menampilkan data dalam format JSON pada file views.py di folder mywatchlist. Fungsi show_watchlist_html menerima HTTP request dan mengembalikan hasil render data response yang akan ditampilkan di mywatchlist.html. Fungsi show_watchlist_xml akan mengembalikan HTTP response berupa data yang diurutkan berdasarkan key dengan format XML menggunakan serialize(). Fungsi show_watchlist_json akan mengembalikan HTTP response berupa data yang diurutkan berdasarkan key dengan format JSON menggunakan serialize().

    6. Membuat routing sehingga data di atas dapat diakses melalui URL: http://localhost:8000/mywatchlist/html (untuk akses format HTML), http://localhost:8000/mywatchlist/xml (untuk akses format XML), dan http://localhost:8000/mywatchlist/json (untuk akses format JSON)

    Pattern URL yang ditambahkan pada urls.py pada folder mywatchlist adalah "html/" (merujuk ke akses watchlist dalam HTML dengan memanggil show_watchlist_html), "xml/" (merujuk ke akses watchlist dalam XML dengan memanggil show_watchlist_xml), "json/" (merujuk ke akses watchlist dalam JSON dengan memanggil show_watchlist_json).

    7. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

    Melakukan push ke repository GitHub melalui source control di Visual Studio Code

## Credits

TUGAS 3 PBP by ARK