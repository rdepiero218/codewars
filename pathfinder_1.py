# navigating a maze



# maze = "\n".join([
#         ".W.",
#         ".W.",
#         "..."
#     ])

# maze = "\n".join([
#         "......",
#         "......",
#         "......",
#         "......",
#         ".....W",
#         "....W."
#     ])

# start_pos = (0,0)


# maze = [list(row) for row in maze_string.split('\n')]

# print(maze)



def path_finder(maze_string):
    maze = [list(row) for row in maze_string.split('\n')]
    start_pos = (0,0)
    visited = set([start_pos])
    queue = [start_pos]
    
    while queue:

        (this_row, this_col) = queue.pop()
        visited.add((this_row,this_col))
        print(visited)

        for dir_row, dir_col in [(0,1), (-1,0), (0, 1), (0,-1)]:
            next_row, next_col = this_row + dir_row, this_col + dir_col
            print('i =', next_row, 'j =', next_col)
            
            if (next_row, next_col) in visited:
                continue

            if next_row < 0 or next_col < 0 or next_row >= len(maze) or next_col >= len(maze):
                continue

            if maze[next_row][next_col] == 'W':
                
                continue
                # result = True
                # return True

            if dir_row == (len(maze)-1) and dir_col == (len(maze)-1):
                return False
            
            if maze[next_row][next_col] == '.':
                visited.add((next_row, next_col))
                queue.append((next_row, next_col))

    return True # can go to lower right corner from upper left one

## trivial case
maze_string = "\n".join([
        "...",
        "...",
        "..."
    ])

path_finder(maze_string)