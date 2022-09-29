# Tugas 3 PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Aplikasi Heroku (To-Do List)

https://ark-tugas2pbp.herokuapp.com/todolist/

## Jawaban Pertanyaan

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

   Tag {% csrf_token %} digunakan untuk meng-generate token di server saat me-render halaman HTML. Token ini dipakai untuk mencegah serangan CSRF (Cross-Site Request Forgery) pada web. CSRF token diperlukan pada elemen form karena input pada elemen ini dapat mengubah data di database server dan kita tidak ingin orang sembarangan dapat mengubah-ubah data di server seenaknya. Lebih parahnya lagi jika hacker berhasil masuk ke akun administrator, maka ia punya akses untuk mengotak-atik web application tersebut sehingga hacker bisa mengambil kontrol keseluruhan aplikasi web tersebut. Efeknya jika kita tidak mengimplementasikan CSRF token, maka bisa saja hacker tersebut mengubah-ubah data pada akun seorang pengguna tanpa sepengetahuan orang tersebut dengan mengubah request dan juga merampas data tersebut untuk diperjualbelikan atau hal-hal lainnya sehingga terjadi yang disebut dengan data breach.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

   Tentu saja bisa, caranya adalah kita harus membuat elemen form pada file html yang akan ditampilkan dengan menambahkan start tag <form> dan end tag </form>. Pada start tag perlu ditambahkan "method='POST'" agar data input pada form yang sudah diisi akan dikirim ke server oleh HTTP client. Di dalam elemen <form> kita perlu menambahkan elemen <input> untuk mengambil data yang akan dimasukkan oleh pengguna. Selain itu, kita juga perlu menambahkan label di sebelah input field agar pengguna tahu data apa yang harus ia masukkan. Untuk mempermudah dalam menyajikan tampilan form biasanya elemen-elemen ini disusun dalam tabel yang dapat kita buat dengan elemen <table>. Data-data yang telah diisi di form nantinya dapat diakses dengan memanggil "request.POST.get()".

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

    1. Pengguna mengisi form pada input field yang disediakan.
    2. Django melakukan validasi pada data yang dimasukkan, jika tidak valid maka Django akan mengirim error message.
    3. HTTP client mengirim data form ke server melalui HTTP method "POST".
    4. Pada views.py, data akan diambil dengan method "request.POST.get()".
    5. Data disimpan pada model yang telah dibuat di models.py dengan method "save()".
    6. Data disimpan dalam context, lalu kemudian dilakukan render halaman HTML.
    7. Data dapat dicetak dalam halaman HTML dengan mengakses key data tersebut pada context.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.

    Melakukan command "django-admin startapp todolist" pada direktori repository Tugas 2 kemarin dalam virtual environment. Kemudian menambahkan todolist ke daftar installed apps di settings.py pada folder project_django.

    2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.

    Menambahkan pattern URL di urls.py pada folder project_django dengan path "todolist/" yang merujuk ke routing path yang ada di urls.py pada folder todolist. Lalu, membuat variabel "app_name" dan "urlpatterns" pada file urls.py di folder todolist. "app_name" yang digunakan adalah "todolist". Untuk mengakses http://localhost:8000/todolist, maka pattern URL yang perlu ditambahkan pertama kali adalah path "" (string kosong) yang akan mengarahkan pengguna ke halaman todolist.html dari aplikasi todolist dengan memanggil show_todolist. Halaman tersebut akan berisi task-task yang dimasukkan oleh pengguna ke aplikasi todolist.

    3. Membuat sebuah model Task yang memiliki atribut sebagai berikut: user, date, title, description.

    Membuat model class Task di file models.py pada folder todolist. Field user adalah ForeignKey yang parameternya adalah User dan models.CASCADE, date adalah tipe data date, title adalah tipe data char (max. 255 karakter), dan description adalah tipe data text.

    4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.

    - Form registrasi dibuat dengan cara membuat fungsi register_account() menggunakan template form UserCreationForm(), lalu data input dikirim ke server dengan method HTTP request POST dan terakhir data disimpan ke database dengan method save() pada model Task. Kemudian setelah selesai, fungsi akan redirect ke halaman login.
    - Implementasi login dibuat dengan cara membuat fungsi user_login(), lalu data input dikirim ke server dengan method HTTP request POST. Data username dan password diambil dengan "request.POST.get()". Setelah itu, akan dilakukan authentication user dengan mengecek apakah username dan password ada di database. Jika ada, maka fungsi "login(request, user)" akan dipanggil. Fungsi juga akan mengecek session terakhir dengan implementasi cookies. Terakhir, fungsi akan redirect ke halaman utama todolist.
    -Implementasi logout dibuat dengan cara membuat fungsi user_logout() yang akan memanggil fungsi "logout(request)", lalu redirect ke halaman login.

    5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.

    Membuat fungsi show_todolist() yang akan mengambil username milik user yang sedang menggunakan aplikasi. Kemudian context yang dikirim ke halaman HTML adalah username dan daftar task yang dimiliki pengguna (menggunakan method filter()). Langkah berikutnya adalah render halaman HTML "todolist.html". Username pengguna ditampilkan dengan memasukkan "{{ username }}" pada HTML. Tombol "Add task" dibuat dengan membuat elemen <input> dengan type "submit" dan value "Add task" di dalam elemen form dengan action di set ke URL routing "create_task". Sementara itu, untuk tombol "Logout" dibuat dengan membuat elemen <input> dengan type "submit" dan value "Logout" di dalam elemen form dengan action di set ke URL routing "user_logout". Untuk mencetak tabel, digunakan elemen <table> dimana pada baris pertama (elemen <tr> pertama) ada "Title", "Description", "Date", "Status", "Change Status", dan "Delete Task" sebagai judul tiap kolom. Selanjutnya, dilakukan iterasi untuk tiap-tiap task yang dimiliki pengguna dengan for-each loop untuk mencetak data pada masing-masing object task. Pada dua kolom terakhir, ditambahkan button "Change" untuk mengubah status task dan "Delete" untuk menghapus task.

    6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

    Membuat fungsi create_task() yang akan mengambil user menggunakan "request.user" dan data input dari form melalui "request.POST.get()" setelah dilakukan method HTTP request POST untuk mengirim data pada form ke server. Langkah berikutnya, object Task baru akan dibuat dengan parameter data yang sudah diambil dari form tadi dan satu parameter tanggal yang diambil dari "date.today". Kemudian, data tersebut disimpan ke database dengan method "save()". Terakhir, fungsi akan redirect ke halaman utama todolist.

    7. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut: http://localhost:8000/todolist/login (untuk login akun), http://localhost:8000/todolist/register (untuk registrasi akun), http://localhost:8000/todolist/create-task (untuk pembuatan task dengan form), dan http://localhost:8000/todolist/logout (untuk logout akun).

    Pattern URL yang ditambahkan pada urls.py pada folder todolist adalah "" (string kosong) (merujuk ke akses halaman utama todolist yang berisi task pengguna dengan memanggil show_todolist), "register/" (merujuk ke akses halaman registrasi akun dengan memanggil register_account), "login/" (merujuk ke akses halaman login akun dengan memanggil user_login), "logout/" (merujuk ke implementasi logout akun dengan memanggil user_logout), "create-task/" (merujuk ke akses halaman pembuatan task dengan memanggil create_task), "change-status/" (merujuk ke implementasi pengubahan status task dengan memanggil change_status), "delete-task/" (merujuk ke implementasi penghapusan task dengan memanggil delete_task).

    8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

    Melakukan push ke repository GitHub melalui source control di Visual Studio Code

    9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

    Akun test:
    1. cicakbinkadal, password: thisistheway
    2. dekdepe, password: ihatetpsomuch

    Dummy data task sudah ditambahkan ke akun masing-masing.

    Catatan: isi folder fixtures tidak jadi dipakai.

## Credits

TUGAS 4 PBP by ARK