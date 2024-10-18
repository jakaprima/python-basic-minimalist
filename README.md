## running code
* python nama_file
* jupyter notebook

TIPE DATA PYTHON
INT, FLOAT, STR, BOOL, LIST, TUPLE, SET, DICTIONARY, NONE TYPE


Dalam Python, *args dan **kwargs digunakan untuk menangani sejumlah argumen tak terbatas pada fungsi. Namun, ada perbedaan antara keduanya:

1. *args (Positional Arguments)
*args digunakan untuk menerima sejumlah argumen posisi (positional arguments) yang tidak terbatas dalam bentuk tuple.

Cara Kerja: Saat Anda menggunakan *args, fungsi tersebut bisa menerima argumen dalam jumlah berapa pun dan semuanya akan dikemas menjadi satu tuple.

Contoh:

python
Salin kode
def contoh_args(*args):
    for arg in args:
        print(arg)

contoh_args(1, 2, 3, "Python", True)
Output:

graphql
Salin kode
1
2
3
Python
True
Dalam contoh di atas, semua argumen yang diberikan ke fungsi contoh_args akan dimasukkan ke dalam args sebagai tuple (args = (1, 2, 3, "Python", True)), dan dapat diiterasi satu per satu.

2. **kwargs (Keyword Arguments)
**kwargs digunakan untuk menerima sejumlah argumen kata kunci (keyword arguments) yang tidak terbatas dalam bentuk dictionary.

Cara Kerja: Saat Anda menggunakan **kwargs, fungsi tersebut bisa menerima argumen dengan kata kunci dalam jumlah berapa pun, yang kemudian dikemas menjadi dictionary.

Contoh:

python
Salin kode
def contoh_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

contoh_kwargs(nama="Wanda", umur=30, bahasa="Python")
Output:

makefile
Salin kode
nama = Wanda
umur = 30
bahasa = Python
Dalam contoh di atas, semua argumen yang diberikan dalam bentuk pasangan kunci-nilai akan dimasukkan ke dalam kwargs sebagai dictionary (kwargs = {"nama": "Wanda", "umur": 30, "bahasa": "Python"}), dan dapat diiterasi melalui kunci dan nilainya.

Perbedaan Utama:
*args mengumpulkan argumen posisi (positional arguments) ke dalam tuple.
**kwargs mengumpulkan argumen kata kunci (keyword arguments) ke dalam dictionary.
Contoh Penggunaan *args dan **kwargs Bersamaan:
python
Salin kode
def contoh_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

contoh_args_kwargs(1, 2, 3, nama="Wanda", bahasa="Python")
Output:

css
Salin kode
Positional arguments: (1, 2, 3)
Keyword arguments: {'nama': 'Wanda', 'bahasa': 'Python'}
Dalam kasus ini, *args akan menangani argumen posisi (1, 2, 3), sementara **kwargs akan menangani argumen kata kunci (nama="Wanda", bahasa="Python").


Kata Pembuka:
"Selamat datang di channel IT Mentor Apps! Saya Wanda, dan di sini kita akan belajar bersama tentang Python, salah satu bahasa pemrograman paling populer di dunia. Pada video ini, kita akan membahas [tema tutorial] yang bisa membantu Anda mengembangkan skill coding Anda. Jangan lupa subscribe dan aktifkan notifikasinya, supaya tidak ketinggalan tutorial menarik lainnya. Yuk, kita mulai!"

Kata Penutup:
"Terima kasih sudah menonton video ini! Semoga bermanfaat dan bisa membantu Anda dalam memahami Python lebih baik. Jangan ragu untuk tinggalkan komentar jika ada pertanyaan atau topik yang ingin dibahas lebih lanjut. Jangan lupa like, share, dan subscribe untuk mendukung channel ini. Sampai jumpa di video berikutnya di IT Mentor Apps!"

Dengan menggunakan pembuka dan penutup ini, Anda bisa menarik perhatian penonton dan memberikan kesan yang ramah serta profesional.