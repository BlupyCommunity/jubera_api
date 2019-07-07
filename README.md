## Jubera API

Jubera API merupakan application programming interface untuk sistem informasi pembelian, 
penjualan dan laporan laba rugi. Target pengguna yang akan menggunakan aplikasi ini 
adalah pengguna yang memiliki bisnis pibadi level awal dan menengah.

### Spesifikasi Kebutuhan

- Linux Ubuntu 18.04 (varian linux) `sangat direkomendasikan`.
- Mac OS
- Windows 8, 10
- Python 3.6

### Dependensi

- Aplikasi Admin Jubera



### Instalasi 

> Disarankan menggunakan virtualenv.

Clone API Jubera lalu masuk ke direktori project:

```
$ pip install -r requirements.txt
```

Lakukan migrasi:

```
$ python manage.py makemigrations
```

Jalankan server:

```
$ python manage.py runserver
```

API bisa digunakan. Untuk dokumentasi lengkapnya silahkan kunjungi:

- [Dokumentasi API Jubera](https://gitlab.com/jubera-app/jubera_api/wikis/home)