'''
================
Exercise 3
================ 


Use a dictionary to represent the file system shown

Update the functions implementig the breadth-first and depth-first search algorithms to navigate the file system representation and:
a) stop when the file week1.pdf is found
b) return the file path to it
c) which function do you think is better suited to this task and why? 

Now consider if a file with the same name exists in two different locations e.g. a file named week1.pdf is in directory CPA and directory MDM
d) Update your functions to print all file paths that exist to a file named week1.pdf (you may add a file called week1.pdf to the CPA directory and any other locations in the file system to test your code works) 


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
    Uses the breadth-first search algorithm to print the items of a graph/netork level by level
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

# -------------------------------------------
# a
# -------------------------------------------
"""
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
"""

file_system = {
    "home": ["documents", "photos", "downloads"],
    "documents": ["CPA", "MDM"],
    "photos": ["weekend.jpg", "me.png"],
    "downloads": ["application_form.docx", "schedule.png"],
    "CPA": ["week0.ipynb", "week1.ipynb", "week2.ipynb"],
    "MDM": ["week1.pdf", "week2.pdf"]
}