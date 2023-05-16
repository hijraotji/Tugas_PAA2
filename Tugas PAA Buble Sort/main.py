def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Elemen terakhir sebanyak i sudah terurut
        for j in range(0, n-i-1):
            # Melakukan iterasi pada array dari 0 hingga n-i-1
            # Jika elemen saat ini lebih besar dari elemen berikutnya, tukar posisinya
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

print("Array terurut:")
for i in range(len(arr)):
    print("%d" % arr[i])