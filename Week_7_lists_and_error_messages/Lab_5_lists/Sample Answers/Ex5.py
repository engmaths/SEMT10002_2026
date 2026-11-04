"""
================
Exercise 5
================
Build a sorting algorithm, inspired by Timsort, that takes advantage of the fact that real-world data is often already partly sorted

Breaking the problem down into steps...

Can you:
- Idenitify the start and end positions of runs of 3 or more ascending values in a list 
- Find the sequences of unordered data in the gaps between runs
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



def my_timsort(numbers):
    """
    Sorts a list of values in ascending order in-place
    by sorting sections of data of maximum length 4 using 
    insertion sort, then merging increasingly large sections until a 
    single merged list achieved 
    """

    run_starts = []
    run_ends = []
    run = []
    # count = 1

    for i, j in enumerate(numbers):

        # Add item to the run
        run.append(j)
        # print(run)

        if len(run)>1:

            # If two sequential descending values are detected
            if run[-1]<run[-2]:

                # Remove the last value from the run
                run.pop(-1)

                # Test if the run contains 3 or more values
                if len(run) >= 3:
                    print("run of", len(run), run)

                    # Store the start and end of the run in the list
                    run_ends.append(i)
                    run_starts.append(i-len(run))
      
                run = [j]
    
    # If list termintes part-way through a run, record the run
    if len(run) > 2:
        print("run of", len(run), run)
        run_ends.append(i+1)
        run_starts.append(i+1-len(run))

    print('starts', run_starts)
    print('ends', run_ends)

    # Insertion sort all unsorted sections and record start and end values
    list_length = len(numbers)
    size = 4

    # Include the start and final values in the list of run start and ends
    run_ends.insert(0,0)
    run_starts.append(len(numbers))

    # An array to store the starts of both the sections and the sorted sections 
    all_starts = run_starts.copy()

    # Find gaps between runs 
    for e, s in zip(run_ends, run_starts):

        # Break the unsorted gaps down into secions of a specified maximum size 
        for start in range(e, s, size):

            # The end is first of the end of the list or the specified length
            end = min(s, start+size)

            # Section to sort
            section = numbers[start:end]
            # print('section', section)

            # Store the start of the section 
            all_starts.append(start)

            # Insertion sort each section
            insertion_sort(section)
            # print(section)

            # Replace section of original list with sorted section
            numbers[start:end] = section

        print('numbers', numbers)

    # Merge nieghbouring sections 
    # print(all_starts)
    insertion_sort(all_starts)
    print(all_starts)

    # Merge increasingly large sections until single merged list achieved
    while len(all_starts) > 2:

        # Get pairs of neighbouring sections  
        for i in range(0,len(all_starts),2):
            if len(all_starts[i:i+3])==3:
                s = all_starts[i]
                m = all_starts[i+1]
                e = all_starts[i+2]

                left = numbers[s:m]
                right = numbers[m:e]

                # Merge neighbouring section
                merged = merge(left, right)

                # Replace in list 
                numbers[s:e] = merged

                # print(numbers)

        # Remove the middle index form the list of indexes
        all_starts = all_starts[::2]

        # Make sure the last value hasn't been omitted
        if len(numbers) not in all_starts:
            all_starts.append(len(numbers))

        # print(all_starts)

    print(numbers)

nums = [4,1,2,3,5,3,4, 6, 3, 7, 3, 5,3,1,2,8,5,6,7]
# nums = [4,1,2,3,5,3,4,6,3,7,2,3,4,5]
print(nums)
my_timsort(nums)