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

def identify_runs(numbers):
    """
    Idenitifies runs of 3 or more ascending values in a list
    Returns the start and end indexes of any runs idenfified  
    """
    # Array to store sections of the list
    run = []

    # Arrays to store start and end of runs 
    run_start_idxs = []
    run_end_idxs = []
    run = []

    for i, j in enumerate(numbers):

        # Add item to the run
        run.append(j)

        if len(run)>1:

            # Terminate run if the last two items of the run are decending order
            if run[-1]<run[-2]:

                # If there is a run of 3 or more ascending items, store the run
                length_of_run = len(run)-1
                if length_of_run >= 3:

                    print("run of", length_of_run, run[:-1])
                    run_end_idxs.append(i)
                    run_start_idxs.append(i-length_of_run)

                # Start a new run
                run = [j]
    
    # If list termintes part-way through a run of 3 or more ascending items, store the run
    if len(run) > 2:
        print("run of", len(run), run)
        run_end_idxs.append(i+1)
        run_start_idxs.append(i+1-len(run))

    print('run start idxs', run_start_idxs)
    print('run end idxs', run_end_idxs)
    return run_start_idxs, run_end_idxs

def sort_unsorted_sections(run_start_idxs, run_end_idxs, numbers):
    """
    Insertion sorts all unsorted sections of a list, broken down into
    subsections of maximum length 4 values. 
    Returns record start value of all ordered sections in the list
    """

    # Maximum length of section
    size = 4
    
    # Use run start and end indexes to define gap start and end indexes 
    gap_start_idxs = run_end_idxs.copy()
    gap_end_idxs = run_start_idxs.copy()

    # Add the start and end of the list to the indexes
    gap_start_idxs.insert(0,0)
    gap_end_idxs.append(len(numbers))

    print('gap start idxs', gap_start_idxs)
    print('gap end idxs', gap_end_idxs)

    # An array to store all section starts
    section_start_idxs = run_start_idxs.copy()

    print('numbers', numbers)

    for gap_start, gap_end in zip(gap_start_idxs, gap_end_idxs):
        # print(gap_start, gap_end)

        for section_start in range(gap_start, gap_end, size):
            # Store start of each section of unsorted data
            section_start_idxs.append(section_start)

            # Determine section end
            section_end = min(section_start+size, gap_end)

            section = numbers[section_start:section_end]
            print(section)

            # Insertion sort section
            insertion_sort(section)
            print(section)

            numbers[section_start:section_end] = section

    # Sort section start indexes into ascending order
    # print(section_start_idxs)
    insertion_sort(section_start_idxs)
    print('section_start_idxs', section_start_idxs)

    # Add the end of the list to the indexes
    section_start_idxs.append(len(numbers))
    print('section_start_idxs',section_start_idxs)
    
    print('numbers', numbers)

    return section_start_idxs

def merge_sections(section_start_idxs, numbers):
    """
    Merge nieghbouring sections of a list until all values are ordered
    """
    # Until the only section start indexes are start and end of the list 
    while(len(section_start_idxs)>2):

        # Merge 
        for i in range(0, len(section_start_idxs)-2, 2):
            start = section_start_idxs[i]
            middle = section_start_idxs[i+1]
            end = section_start_idxs[i+2]

            merged_section = merge(numbers[start: middle],
                                   numbers[middle:end])
            
            numbers[start:end] = merged_section

        # Update section start indexes by removing middle index of each merge
        section_start_idxs = section_start_idxs[::2]

        # Check the end of the list is in the list of indexes
        if len(numbers) not in section_start_idxs:
            section_start_idxs.append(len(numbers))


def my_timsort(numbers):
    """
    Sorts a list of values in ascending order in-place
    by sorting sections of data of maximum length 4 using 
    insertion sort, then merging increasingly large sections until a 
    single merged list achieved 
    """
    # Idenitify runs of 3 or more ascending values and store start and end indexes of runs 
    run_start_idxs, run_end_idxs = identify_runs(numbers)

    # Insertion sort all unsorted sections and record start value of all ordered sections
    section_start_idxs = sort_unsorted_sections(run_start_idxs, run_end_idxs, numbers)

    # Merge neighbouring sections until all values are ordered
    merge_sections(section_start_idxs, numbers)


nums = [4, 3,1,2,3,5,3,4, 6, 3, 7, 3, 5,3,2, 4, 1,2,8,5,6,7]
nums = [4, 3,1,2,3,5,3,4, 6, 3, 7, 3, 5,3,2, 4, 1,2,8,5,6,7,1,2,3,1,2,3,2,4,5,3,6,9,1,3,1,3,1]
my_timsort(nums)
print(nums)

