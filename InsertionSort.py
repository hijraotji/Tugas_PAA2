import time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()  # Waktu mulai eksekusi

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

            # Menampilkan proses iterasi
            print(arr)

        arr[j + 1] = key

    end_time = time.time()  # Waktu selesai eksekusi
    execution_time = end_time - start_time  # Menghitung waktu eksekusi

    return arr, execution_time


# Contoh penggunaan:
arr = [4, 1, 2, 3, 5]
sorted_arr, execution_time = insertion_sort(arr)
print("Hasil akhir:", sorted_arr)
print("Waktu eksekusi:", execution_time, "detik")
