lisx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 'don']
]
# 2d list ialah list didalam list
# Reminder: type value dalam list dapat berupa str, int, bool, dsb.
print(lisx[0][1])
# menampilkan list index [1] didalam var listx index [0]
for x in lisx:
    # var x mengambil list dari var lisx
    for y in x:
        # var y mengambil setiap nilai dari list var x
        print(y)