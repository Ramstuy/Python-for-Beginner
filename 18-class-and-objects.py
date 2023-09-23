class Peps:
    pass
# agar tidak terjadi error jika kita belum ingin mengisi classnya
    def __init__(self, name, age):
        # menginisiasi fungsi untuk class Peps
        # self biasa digunakan sebagai constructor parameter untuk class
        self.name = name
        self.age = age

name = input('Input your name: ')
age = input('Input your age: ')
p1 = Peps(name, age)
# memanggil var p1 sebagai class Peps dan parameter fungsi yang ada di dalamnya
print(p1.name)
print(p1.age)