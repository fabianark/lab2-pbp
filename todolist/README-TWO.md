# Tugas 6 PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Jawaban Pertanyaan

1.  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

    Asynchronous programming adalah model multi-threaded dalam suatu pemrograman sehingga program dapat mengeksekusi beberapa task dalam satu waktu (multitasking). Dalam web programming, asynchronous programming digunakan agar pengguna tetap dapat berinteraksi dengan website walaupun sedang ada proses eksekusi task lain yang dilakukan oleh program di belakang layar. Pada dasarnya, asynchronous programming melakukan loading data lalu melakukan refresh terhadap bagian tertentu pada halaman. Oleh karena itu, asynchronous programming disebut sebagai nonblocking architecture. Asynchronous programming sering digunakan dalam program untuk komunikasi seperti WhatsApp, Instagram, dan Gmail.

    Sementara itu, synchronous programming adalah model pemrograman single-threaded yang menggunakan urutan dalam mengerjakan lebih dari satu task (sequential tasking). Akibatnya, task lain yang ada di belakang antrian harus menunggu task-task yang ada di depannya untuk diselesaikan terlebih dahulu. Dalam web programming, dampak yang diberikan dari model synchronous adalah pengguna tidak dapat berinteraksi dengan web tersebut sampai web berhasil memberikan halaman result dari task yang sebelumnya. Pengguna harus menunggu lalu melakukan refresh keseluruhan halaman secara manual.

2.  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

    Paradigma pemrograman event-driven programming adalah konsep pemrograman yang baru akan dijalankan ketika terjadi event tertentu. Event tersebut dapat berupa aksi yang dilakukan pengguna seperti klik tombol atau hover mouse di area tertentu atau event yang dilempar oleh program lain. Konsep event-driven programming sering dipakai dalam menerapkan Graphical User Interface (GUI).

    Contoh konsep event-driven programming yang dipakai dalam tugas ini adalah klik tombol "Add task" yang dilakukan oleh pengguna. Ketika pengguna melakukan klik terhadap tombol "Add task", website akan menampilkan modal untuk mengisi form penambahan task. Kemudian, setelah selesai mengisi judul dan deskripsi tugas, user akan melakukan klik tombol "Add" yang membuat program melakukan penambahan task ke dalam database task milik pengguna, menampilkan alert berhasil, menutup modal, dan me-refresh elemen div bagian todolist.

3.  Jelaskan penerapan asynchronous programming pada AJAX.

    AJAX adalah singkatan dari "Asynchronous JavaScript and XML". Namanya disebut begitu karena JavaScript akan mengambil database dari XML untuk diproses. Walaupun namanya mengandung XML, AJAX juga bisa dilakukan dengan mengganti XML dengan JSON seperti yang dilakukan pada tugas ini. AJAX akan mengupdate data pada bagian tertentu pada halaman website sehingga pengguna tidak perlu melakukan reload halaman website. Kode JavaScript yang dibuat akan memanggil JQuery.ajax() dengan method "GET" dan "POST" yang memproses data tanpa mengganggu interaktivitas website. Alur proses dalam AJAX asynchronous programming adalah pengguna memicu event untuk melakukan perubahan data pada website, lalu program meng-handle proses task tersebut secara asinkronus sehingga terpisah dengan implementasi tampilan website yang membuat website menjadi tetap interaktif, program akan mengirimkan hasil dari proses task tersebut ke halaman HTML ketika sudah selesai, dan terakhir halaman HTML akan ter-update secara otomatis pada bagian yang datanya diproses tadi.

4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    1.  Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
        Membuat fungsi baru di views.py bernama show_json() yang mengambil data object-object Task lalu menyajikannya dalam format JSON dengan serializer. Jika ada user yang sedang login, maka show_json() menunjukkan hanya database task yang dimiliki user tersebut. Namun, jika tidak ada user yang sedang login, mengakses path show_json() akan menunjukkan seluruh database task milik semua pengguna

    2.  Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.
        Menambahkan path '/json' di urls.py pada todolist untuk memanggil fungsi show_json().

    3.  Lakukan pengambilan task menggunakan AJAX GET.
        Membuat fungsi JavaScript untuk melakukan render todolist yaitu dengan melakukan method JQuery.get() yang mengambil database task yang ada di path '/todolist/json' dan menampilkannya dengan cara melakukan concate string yang berisi kode HTML untuk menampilkan todolist kemudian memasukkannya ke tag div dengan id 'ajax-todolist' dengan set innerHTML menjadi kode HTML todolist yang sudah di concate tadi.

    4.  Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
        Tombol "Add Task" dibuat dengan komponen Button di Bootstrap. Kemudian pada button tersebut atribut toggle di-set ke "modal" dan target nya di-set ke nama class dari komponen Modal yang sudah dibuat dengan Bootstrap. Komponen Modal berisi Card yang kurang lebih sama dengan yang ada di halaman path '/todolist/create-task' pada tugas sebelumnya.

    5.  Buatlah view baru untuk menambahkan task baru ke dalam database.
        Menambahkan fungsi add_task_ajax() ke views.py di todolist. Fungsi ini melakukan instruksi yang sama dengan fungsi create_task() pada tugas sebelumnya, tetapi perbedaannya fungsi ini akan mengembalikan pesan berhasil menambahkan task untuk ditampilkan pada alert setelah melakukan penambahan task pada komponen Modal.

    6.  Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
        Menambahkan path '/add' di urls.py pada todolist yang menunjuk ke fungsi add_task_ajax() yang tadi telah dibuat.

    7.  Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
        Form penambahan task pada modal diberi id 'add-task'. Kemudian, pada kode JavaScript dibuat fungsi yang akan menangkap form submit dan memproses penambahan task tersebut dengan "$('#add-task').submit(function())". Di dalam fungsi tersebut ditambahkan method JQuery.ajax() yang atribut methodnya di-set ke "POST" dan url menunjuk ke path '/todolist/add'. Ketika sudah berhasil menambahkan, maka web akan melakukan tampilan alert berhasil.

    8.  Tutup modal setelah penambahan task telah berhasil dilakukan.
        Menutup komponen modal dengan method "$('#addTaskModal').modal('hide')" untuk kembali menyembunyikan komponen modal.

    9.  Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.
        Me-refresh elemen div bagian todolist secara asinkronus dengan kembali memanggil fungsi renderTodolist() yang dipakai untuk menampilkan todolist dengan AJAX GET di tahap sebelumnya.

## Credits

TUGAS 6 PBP by ARK