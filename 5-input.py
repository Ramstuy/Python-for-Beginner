name = input('Input name: ')
# User dapat menginput nilai variable

age = int(input('Input age: '))
# Inputan yang dimasukkan oleh user akan terbaca sebagai Integer

print('Hello',name+', you are',age,'years old')

# Contoh penerapan input dan replace input
# =================================================================

sentc = input('enter yout sentences: ')
print('your sentece is '+sentc)

word1 = input('Enter word to replace: ')
word2 = input('Enter word to replace it with: ')
print(sentc.replace(word1, word2))
# Nilai inputan var sentc akan diganti dengan nilai var word1
# lalu sentc.replace(word1, word2) digunakan untuk mengganti nilai var word1 menjadi nilai var word 2