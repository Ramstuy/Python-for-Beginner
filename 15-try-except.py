try:
    x = int(input('Input an integer: '))
    print(x)
except ValueError:
# akan menjelankan code ini jika value yang di input tidak sesuai
# misal var x diatas meminta input tipe integer
# jika kita memasukkan inputan yang non integer maka akan menjalankan code except
    print('Invalid input')
else:
    print('No error')
# jika perintah except tidak dijalankan, maka perintah else akan dijalankan