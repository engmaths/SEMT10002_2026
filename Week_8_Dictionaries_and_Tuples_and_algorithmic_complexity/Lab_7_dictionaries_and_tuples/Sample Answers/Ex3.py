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
    "MDM": ["week1.pdf", "week2.pdf"],
    "week0.ipynb": [],
    "week1.ipynb": [],
    "week2.ipynb": [],
    "weekend.jpg": [],
    "me.png": [],
    "week1.pdf": [],
    "week2.pdf": [],
    "application_form.docx": [],
    "schedule.png": []
}


def bfs_updated(tree, start, item_to_find=None):
    """
    Uses the breadth-first search algorithm to search a graph/network 
    level by level and return the path to a specified file
    """
    # A counter for files in the root directory
    pdf_count = 0
    found = False

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

        # Check for the file to find
        if node == item_to_find:
            print(node, 'found!')
            found = True

        # If item is a pdf file, increase the count 
        if node[-4:] == ".pdf":
            pdf_count += 1

        # Add all the node's children to the stack
        for child in tree[node]:
            queue.append(child)

    # Add item to starting directory if not found 
    if found==False and item_to_find!= None:
        tree[start].append(item_to_find)

    return pdf_count


def dfs_updated(tree, start, item_to_find=None):
    """
    Uses the depth-first search algorithm to print the items of a graph/netork branch by branch
    """
    # A counter for files in the root directory
    pdf_count = 0
    found = False
    
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
        
        # Check for the file to find
        if node == item_to_find:
            print(node, 'found!')
            found = True

        # If item is a pdf file, increase the count 
        if node[-4:] == ".pdf":
            pdf_count += 1
        
        # Add all the node's children to the stack
        for child in tree[node]:
            stack.append(child)

        # To traverse in the same order as depth first search
        # for child in reversed(tree[node]):
        #     stack.append(child)

    # Add item to starting directory if not found 
    if found==False and item_to_find!= None:
        tree[start].append(item_to_find)

    return pdf_count

   




start="CPA"
n_pdfs = bfs_updated(file_system, start, item_to_find="week1.ipynb")
print("Number of pdfs in", start, "is", n_pdfs)

start="home"
n_pdfs = bfs_updated(file_system, start, item_to_find="Movies")
print("Number of pdfs in", start, "is", n_pdfs)

for i in file_system.items():
    print(i)

start="home"
n_pdfs = dfs_updated(file_system, start, item_to_find="week1.ipynb")
print("Number of pdfs in", start, "is", n_pdfs)  

n_pdfs = dfs_updated(file_system, start, item_to_find="movies")
print("Number of pdfs in", start, "is", n_pdfs)  

for i in file_system.items():
    print(i)