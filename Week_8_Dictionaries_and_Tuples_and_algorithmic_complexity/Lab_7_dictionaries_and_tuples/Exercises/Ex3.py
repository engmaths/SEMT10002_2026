'''
================
Exercise 3
================ 


a) Use a dictionary to represent the file system shown

b) Update the function for breadth-first OR depth-first search algorithms (or try both if you have time!):
i) check if a specified file/directory (let's use week1.pdf as an example) exists in the starting directory including within any subdirectories
ii) count all .pdf files within the starting directory including within any subdirectories
ii) if the specified file/directory does not exist, create a new  file/directory with the specified name in the starting directory

home/
├── documents/
│   ├── CPA/
│   │   ├── week0.ipynb
│   │   ├── week1.ipynb
│   │   └── week2.ipynb
│   └── MDM/
│       ├── week1.pdf
│       └── week2.pdf
├── photos/
│   ├── weekend.png
│   └── me.jpg
└── downloads/
    ├── application_form.docx
    └── schedule.png

'''


def bfs(tree, start):
    """
    Uses the breadth-first search algorithm to print the items of a graph/network level by level
    """

    # Start with a queue containing the node we want to visit first 
    queue = [start]

    # Keep going while there are still nodes waiting to be visited
    while queue:
        print('queue:', queue)
        print()

        # Remove the FIRST node added to the queue
        node = queue.pop(0)
        print('node visited:', node)
        print()

        # Add all the node's children to the stack
        for child in tree[node]:
            queue.append(child)


def dfs(tree, start):
    """
    Uses the depth-first search algorithm to print the items of a graph/netork branch by branch
    """
    # Start with a stack containing the node we want to visit first
    stack = [start]

    # Keep going while there are still nodes waiting to be visited
    while stack:
        print('stack:',end="\n")
        for i in reversed(stack):
            print(i)

        # Remove the LAST node added to the stack
        node = stack.pop()
        print()
        print('node visited:', node)
        print()
        
        # Add all the node's children to the stack
        for child in tree[node]:
            stack.append(child)

        # To traverse in the same order as depth first search
        # for child in reversed(tree[node]):
        #     stack.append(child)