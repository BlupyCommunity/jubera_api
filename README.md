## Jubera API

Jubera API merupakan API (application programming interface) untuk sistem informasi pembelian, 
penjualan dan laporan laba rugi. 

### Instalasi 

Clone API Jubera lalu masuk ke direktori project:

```
$ pip install -r requirements.txt
```

Lakukan migrasi:

```
$ python manage.py migrate
```

Jalankan server:

```
$ python manage.py runserver
```

### Dokumentasi API

Anda bisa membaca dokumentasi API Jubera di:

[Dokumentasi API](https://github.com/blupybusiness/jubera_api/wiki)


### Lisensi

```
MIT License

Copyright (c) 2019 Blupy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```