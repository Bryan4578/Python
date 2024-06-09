# Sorting a names list
names = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
bubble_sort(names)
print("\nSorted list of names:")
print(names)
names.reverse()
print("\nReversed list of names:")
print(names)
