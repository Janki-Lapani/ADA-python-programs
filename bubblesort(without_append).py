def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

size = int(input("How many numbers do you want to enter? "))
arr = [0] * size
for i in range(size):
    arr[i] = int(input(f"Enter number {i + 1}: "))

bubble_sort(arr)
print("Sorted list:", arr)
