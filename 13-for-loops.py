lister = ['la', 'li', 'lo']

for x in lister:
# X disini sebagai variabel for baru
    print(x)
    if x == 'li':
        break
    # Break untuk menghentikan proses looping pada kondisi yang sudah ditetapkan
    print(x)

for x in range(2, 8):
# code diatas akan menampilkan angka dari 2 sampai 8 tapi tidak mengambil 8
    print(x)
else:
    print('done ga bang, don')