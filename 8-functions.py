def greetings(name, numb):
# function ialah sekumpulan kode yang melakukan tugas tertentu
# yang di dalam kurung itu parameter

    print('Welcome to Mobillejeng',name+', Hari ini adalah hari ke-'+str(numb)+'mu Disini')
    print('Welcome '+name[1])

name = input('What is your name: ')
numb = input('How long youve been here: ')
greetings(name, numb)