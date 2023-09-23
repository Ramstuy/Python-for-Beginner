countries = ['US', 'Indonesia', 'Makasssar']
# Contoh list 1D

print(countries[2])
# Menampilkan Index 2 dari List
# Index selalui dimulai dari 0

print(countries[2][1])
# Menampilkan huruf kedua dari list (index 1) dari valur list index 2

print(countries[0:2])
# Menampilkan value list dari index 0 sampai 2 exclude index 2

countries[0] = 'Morocco'
countries[2] = 'Nepal'
# Mengganti Nilai dari List countries
# Dalam contoh ini mengganti nilai dari index [0] dan index [2]

print(countries[-1])
# Menampilkan index sebelum index [0]
# Misal index [0] sama dengan Morocco, [1] Indonesia, dan [2] Nepal
# Maka [-1] ialah Nepal (Mundur, lalu terulang kedepan)

print(type(countries))
# Mengecek tipe variabel, dalam konteks ini adalah Variabel List

print(len(countries))
# Mengecek banyak data dalam list

listry = list(('Nepal', 10, True))
print(listry)
# Type nilai dalam list dapat beragam

# =================================================================

list1 = [3, 4, 5, 1, 2]
list2 = ['', 'Grape', 'Mango', 'Orange']

print(list2)
inpu = input('Enter to list: ')
list2[0] = inpu
print(list2[0],'is inserted into the list')
print(list2)

# =================================================================
# Beberapa line diatas adalah contoh code cara user menginput value manual ke dalam list

list1.extend(list2)
# Menggabungkan value dari list 1 dan list 2 dalam 1 list

list2.append('Banana')
# Menambahkan value ke list 2

list2.insert(1, 'Banana')
# Memasukkan value '' ke dalam index 1

list2.remove('Apple')
# Menghapus nilai '' dari var list2

list2.clear()
# Menhapus semua value yang ada di list2

print(list2.index('Grape'))
# Mengecek index berapa nilai dari ''

print(list2.count('Mango'))
# Mengecek jumlah karakter dari nilai ''

list1.sort()
# Mengurutkan nilai list (int) dari terkecil ke terbesar

list1.sort(reverse=True)
# Mengurutkan nilai list (int) dari terbesar ke terkecil

list2.reverse()
# Membalikkan posisi nilai 
# misal dari ['', 'Grape', 'Mango', 'Orange'] ke ['Orange', 'Mango', 'Grape', '']

list3 = list2.copy()
# Membuat variabel list baru yang menyalin semua nilai dari list sebelumnya

list2.pop()
# Menghapus nilai list index terakhir

list2.pop(1)
# Menghapus nilai list index []

list2.remove('Mango')
# Menghapus langsung nilai dari list

del list2[0]
# Menghapus nilai dari list spesifik melalui index[]

del list2
# Menghapus langsung keseluruhan var list termasuk nilai nilai di dalamnya