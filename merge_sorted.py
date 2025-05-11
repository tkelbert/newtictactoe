from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge two sorted arrays into the first array.
    
    Args:
        nums1 (List[int]): The first array with initial size m and to be filled up to size m + n.
        m (int): The number of elements initially in nums1.
        nums2 (List[int]): The second array with n elements.
        n (int): The number of elements in nums2.
    
    Returns:
        None
    """
    # Fill the end of nums1 with zeros to make space for the second array, starting from the end of nums1 and moving backwards.
    for i in range(len(nums1) - m, len(nums1)):
        nums1[i] = 0

    # Reverse the second array to start comparing elements from both arrays from the largest values first.
    nums2.reverse()
    
    i = m - 1
    j = n - 1
    
    # Now, compare each element of both arrays and fill up nums1 accordingly.
    while i >= 0 and j >= 0:
        if nums1[i] <= nums2[j]:
            i -= 1
        else:
            nums1[len(nums1) - n + j] = nums2[j]
            j -= 1
    
    # Fill up any remaining space with elements from the second array.
    while j >= 0 and len(nums1) > m + n:
        nums1[len(nums1) - j - 1] = nums2[j]
        j -= 1
def remove_number(lst):
    """
    Removes all occurrences of numbers in the list.
     
    Args:
        lst (list): The input list containing at least one number and other elements.

    Returns:
        list: A new list with no numbers.
    """

    # Iterate over a copy of the original list to avoid issues when modifying
    # while iterating. Return as soon as we find an item that is not a number.
    return [x for x in lst if x != 0]

def main():
    nums1 = [1, 2, 3, 0, 0, 0, 0, 0]
    m = 3
    nums2 = [7, 8, 9]
    n = 3
    
    merge(nums1, m, nums2, n)
    print(nums1)

    # Remove numbers from the first array.
    result = remove_number(nums1)
    print(result)

if __name__ == "__main__":
    main()