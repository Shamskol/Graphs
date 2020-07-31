from util import Queue

# Build our graph
# Could filter our word list by length
## remember to lower case stuff

# BFS
def word_ladders(start_word, end_word):
    q = Queue()

    visited = set()

    q.enqueue([start_word])
    while q.size > 0:

        current_path = q.enqueue()
        current_word = current_path[-1]

        if  current_word ==  end_word:
            return current_path
        if current_word == end_word:
            return current_path
        if current_word not in visited:
            visited.add(current_word)

            neighbors = get_neighbors(current_word) 

            for neigbor in neighbors:
                new_path = current_path + [neigbor]   
                q.enqueue(new_path)    

