'''
================
Exercise 5
================

Consider a road network represented by the dictionary below. 

In this network some roads are one way (e.g. "M": ["L", "N"] means you can travel from M to N, but because "N": [], you cannot travel from N to M.)

a) Use bfs or dfs (or both if you have time!) to check whether all areas of the network are reachable from a given starting point. 
Print any starting points from which all areas of the network are NOT reachable

b) Write a function to test whether the network remains connected after closing a specified road


'''
roads = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F", "G"],
    "F": ["D", "E", "G", "H"],
    "G": ["E", "F", "H"],
    "H": ["F", "G", "I"],
    "I": ["H", "J"],
    "J": ["I", "K"],
    "K": ["J", "L"],
    "L": ["K", "M"],
    "M": ["L", "N"],
    "N": []
}

def bfs(graph, start):
    """
    Uses the breadth-first search algorithm to print the 
    items of a graph/network level by level
    """

    queue = [start]

    # [UPDATE] Mark each node as visited when it is added to the queue
    visited = [start]

    # Keep going while there are still nodes waiting to be visited
    while queue:
        print('queue:', queue)

        # Remove the FIRST node added to the queue
        node = queue.pop(0)
        print('node visited:', node)

        # Add all the node's children to the queue [UPDATE] if they haven't been visited
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)



def dfs(graph, start):
    """
    Uses the depth-first search algorithm to print the items of a graph/netork branch by branch
    """
    # Start with a stack containing the node we want to visit first
    stack = [start]

    # [UPDATE] Mark each node as visited when it is added to the stack
    visited = [start]

    # Keep going while there are still nodes waiting to be visited
    while stack:
        print('stack:',end="\n")
        for i in reversed(stack):
            print(i)
        print()

        # Remove the LAST node added to the stack
        node = stack.pop()
        print('node visited:', node)
        
        # Add all the node's children to the stack
        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.append(neighbour)
            
        # # To traverse in the same order as breadth first search
        # for neighbour in reversed(graph[node]):
        #     if neighbour not in visited:
        #         stack.append(neighbour)
        #         visited.append(neighbour)

# -------------------------------------------
# a
# -------------------------------------------

def test_reachable_with_bfs(graph, start):
    """
    Uses the breadth-first search algorithm to print the 
    items of a graph/network level by level
    """

    queue = [start]

    # [UPDATE] Mark each node as visited when it is added to the queue
    visited = [start]

    # Keep going while there are still nodes waiting to be visited
    while queue:
        print('queue:', queue)

        # Remove the FIRST node added to the queue
        node = queue.pop(0)
        print('node visited:', node)

        # Add all the node's children to the queue [UPDATE] if they haven't been visited
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

    if sorted(visited) == sorted(graph.keys()):
            print('All cities reachable from', start)



def test_reachable_with_dfs(graph, start):
    """
    Uses the depth-first search algorithm to print the items of a graph/netork branch by branch
    """
    # Start with a stack containing the node we want to visit first
    stack = [start]

    # [UPDATE] Mark each node as visited when it is added to the stack
    visited = [start]

    # Keep going while there are still nodes waiting to be visited
    while stack:
        print('stack:',end="\n")
        for i in reversed(stack):
            print(i)
        print()

        # Remove the LAST node added to the stack
        node = stack.pop()
        print('node visited:', node)
        
        # Add all the node's children to the stack
        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.append(neighbour)
            
        # # To traverse in the same order as breadth first search
        # for neighbour in reversed(graph[node]):
        #     if neighbour not in visited:
        #         stack.append(neighbour)
        #         visited.append(neighbour)

    
    if sorted(visited) == sorted(graph.keys()):
        print('All cities reachable from', start)


test_reachable_with_dfs(roads, "B")
test_reachable_with_dfs(roads, "J")
