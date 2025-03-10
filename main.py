from bubble_sort import bubble_sort
from merge_sort import merge_sort


def sorting_example():
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", numbers)
    print("Bubble Sort:", bubble_sort(numbers.copy()))
    print("Merge Sort:", merge_sort(numbers))

if __name__ == '__main__':
    sorting_example()
