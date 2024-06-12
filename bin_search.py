import time
import random

def binary_search(arr, target):

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # Check if the target is at mid
        if arr[mid] == target:
            return mid
        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1
    # If target is not present in the array, returns "-1"
    return -1

def main():
    # Create a sorted dataset of 1000000 values
    dataset = sorted(random.sample(range(1, 2000000), 1000000))
    # Asks user for the value to search
    target = int(input("Enter the value you want to search for: "))
    # Measure the start time
    start_time = time.time()
    # Perform binary search
    result_index = binary_search(dataset, target)
    # Measure the end time
    end_time = time.time()
    # Calculate the time taken for the search
    time_taken = end_time - start_time
    # Output the result
    if result_index != -1:
        print(f"Value {target} was found at index {result_index}.")
    else:
        print(f"Value {target} was not found in the dataset.")
    # Output the time taken for the search
    print(f"Time taken to search: {time_taken} seconds")

main()
