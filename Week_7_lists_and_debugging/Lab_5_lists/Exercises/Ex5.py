"""
Build a sorting algorithm, inspired by Timsort, that takes advantage of the fact that real-world data is often already partly sorted

Breaking the problem down into steps...

Can you:
- Idenitify the start and end positions of runs of 3 or more ascending values in a list 
- Use insertion sort to sort the gaps (unordered sections between the runs)
- When sorting these gaps, can you break them down into sub-sections of data of maximum length 4 (look at how this is done in merge_sort function)
- Merge increasingly large sections until a single merged list achieved (look at how this is done in merge_sort function) 

Rules
- Don't use `sorted()`
- Don't use `.sort()`
- You may use functions you've written yourself
- Your algorithm should work for lists of arbitrary length
"""

def insertion_sort(numbers):
    """
    Sorts a list of values in ascending order in-place
    """

    for i in range(1, len(numbers)):

        value = numbers[i] # Store value at current postion in list

        j = i-1            

        # Shift earlier values in the list to the right if they are greater than the stored value
        while j>=0 and numbers[j]>value:
            numbers[j+1] = numbers[j]
            j -= 1

        # When a lower value is reached, insert the stored value after it
        numbers[j+1] = value


def merge(left, right):
    """
    Returns two already-sorted lists combined as a single sorted list
    """

    result = []
    i = 0
    j = 0
 
    while i < len(left) and j < len(right):
 
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1
 
    result += left[i:]
    result += right[j:]
 
    return result


def mergesort(numbers):
    """
    Sorts a list of values in ascending order in-place
    by sorting sections of data of maximum length 4 using 
    insertion sort, then merging increasingly large sections until a 
    single merged list achieved 
    """

    list_length = len(numbers)
    size = 4

    for start in range(0, list_length, size):

        section = numbers[start:start+size]

        # Insertion sort each section
        insertion_sort(section)

        # Replace section of original list with sorted section
        numbers[start:start+size] = section

    # Merge increasingly large sections until single merged list achieved 
    while size < list_length:
        for start in range(0, list_length, 2*size):
            left_section = numbers[start:start+size]
            right_section = numbers[start+size:start+2*size]

            merged = merge(left_section, right_section)

            numbers[start:start+len(merged)] = merged

        size *= 2