import unittest
import random

def bubble_sort(arr):
    # Check for arrays with 1 element or less
    if len(arr) <= 1:
        return
    
    # get length of the array
    n = len(arr)

    # Iterate through all elements
    for i in range(n):
        # flag for optimization
        swapped = False

        for j in range(0, n-i-1):
            # Swap if the element found is greater than the element than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # if elements were not swapped, the array is sorted
        if not swapped:
            break
class TestBubbleSort(unittest.TestCase):

    def test_random_array(self):
        # Test Case 1: Random array
        arr1 = [random.randint(1, 100) for _ in range(10)]
        sorted_arr = sorted(arr1)
        bubble_sort(arr1)
        self.assertEqual(arr1, sorted_arr)

    def test_sorted_array(self):
        # Test Case 2: Array already sorted in ascending order
        arr2 = [5, 15, 25, 35, 45, 55]
        bubble_sort(arr2)
        self.assertEqual(arr2, [5, 15, 25, 35, 45, 55])

    def test_decending_array(self):
        # Test Case 3: Array sorted in descending order
        arr3 = [55, 45, 35, 25, 15, 5]
        bubble_sort(arr3)
        self.assertEqual(arr3, [5, 15, 25, 35, 45, 55])

    def test_same_elements_array(self):
        # Test Case 4: Array with all elements the same
        arr4 = [5, 5, 5, 5, 5, 5]
        bubble_sort(arr4)
        self.assertEqual(arr4, [5, 5, 5, 5, 5, 5])

    def test_empty_array(self):
        # Test Case 5: Empty Array
        arr5 = []
        bubble_sort(arr5)
        self.assertEqual(arr5, [])

    def test_single_element_array(self):
        # Test Case 6: Array with one element
        arr6 = [58]
        bubble_sort(arr6)
        self.assertEqual(arr6, [58])

if __name__ == '__main__':
    unittest.main()
