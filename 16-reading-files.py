pal_file = open('16-reading-files.txt', 'r')
# pastikan file yang ingin di buka berada di folder yang sama
# jika tidak berada di folder yang sama, masukkan juga direktori file nya
# tanda 'r' berarti read
print(pal_file.readlines()[1])
# membaca line 2 (index 1)
for lines in pal_file.readlines():
    print(lines)
    # membaca semua line yang ada di file
pal_file.close()
# menutup file