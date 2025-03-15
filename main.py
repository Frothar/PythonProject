from sorting.bubble_sort import bubble_sort
from sorting.merge_sort import merge_sort

def main():
    # Przykładowa lista
    numbers = [64, 25, 12, 22, 11, 90, 3, 10]
    print("Oryginalna lista:", numbers)

    # Bubble sort
    bubble_sorted_numbers = numbers[:]
    bubble_sort(bubble_sorted_numbers)
    print("Po bubble sort:", bubble_sorted_numbers)

    # Merge sort
    merge_sorted_numbers = merge_sort(numbers)
    print("Po merge sort:", merge_sorted_numbers)

if __name__ == "__main__":
    main()
