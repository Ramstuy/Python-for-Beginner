def greetings(name, numb):
# contoh function
# yang di dalam kurung itu parameter

    print('Welcome to Mobillejeng',name+', Hari ini adalah hari ke-'+str(numb)+'mu Disini')
    print('Welcome '+name[1])

name = input('What is your name: ')
numb = input('How long youve been here: ')
greetings(name, numb)