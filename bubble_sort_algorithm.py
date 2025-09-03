def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # number of passes
        print(f"\nPass {i+1}:")
        for j in range(0, n-i-1):  # move pointers left to right
            print(f"Comparing {arr[j]} and {arr[j+1]}")  # show pointers
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap
                print("  Swapped:", arr)
            else:
                print("  No swap:", arr)
    return arr

numbers = [5, 3, 8, 2]
sorted_array = bubble_sort(numbers)
print("\nFinal sorted array:", sorted_array)
