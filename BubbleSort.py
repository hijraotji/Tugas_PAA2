import time

def bubble_sort(arr):
    n = len(arr)

    start_time = time.time()  # Waktu mulai eksekusi

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # Menampilkan proses iterasi
            print(arr)

    end_time = time.time()  # Waktu selesai eksekusi
    execution_time = end_time - start_time  # Menghitung waktu eksekusi

    return arr, execution_time


# Contoh penggunaan:
arr = [4, 1, 2, 3, 5]
sorted_arr, execution_time = bubble_sort(arr)
print("Hasil akhir:", sorted_arr)
print("Waktu eksekusi:", execution_time, "detik")
