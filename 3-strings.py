name = 'marksiman'

print('Hola.\nAmigos')
# \n digunakan untuk membuat baris baru

print(name.upper())
# Digunakan untuk mengubah string menjadi huruf kapital semua
# gunakan variable.lower() untuk mengubah string menjadi huruf kecil semua

print(name.islower())
# Digunakan untung mengecek apakah value string dari variable menggunakan huruf kecil atau tidak
# gunakan variable.isUpper() untuk mengecek string sebaliknya
# Output dalam bentuk boolean

print(len(name))
# untuk menghitung ada berapa karakter pada value yang terdapat di variable

print(name.index('a'))
# mengecek nomor index suatu karakter
# misal dalam case ini sring 'a'
# jika terdapat dua karakter yang sama misal 'a' ada 2 maka hanya akan mengambil karakter pertama

print(name.replace('m', 't'))
# mengubah karakter sesuai dengan permintaan menjadi karakter yang sesuai permintaan juga
# misal mengubah semua karakter 'm' pada string menjadi karakter 't'