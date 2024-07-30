from sys import stdin

r, c = stdin.readline().split()
r = int(r)
c = int(c)

grid = []
for i in range(r):
    temp = [dir for dir in stdin.readline().strip()]
    grid.append(temp)

sight_seeing_count = 0
sight_seeing_coords = []
for i in range(r):
    for j in range(c):
        if grid[i][j] == "#":
            sight_seeing_count += 1
            sight_seeing_coords.append([i,j])


#Gets path from given grid location
def get_path(row, col, grid):
    current = grid[row][col]
    next_spot = [row,col]
    path = [next_spot,]

    while current != "." or current != "#":
        next_spot = [next_spot[0], next_spot[1]]
        #print(current, next_spot)
        #Up
        if current == "^":
            next_spot[0] -= 1
        #Down
        if current == "v":
            next_spot[0] += 1
        #Right
        if current == ">":
            next_spot[1] += 1
        #Left
        if current == "<":
            next_spot[1] -= 1

        #Inside top and bottom of grid
        if next_spot[0] < r and next_spot[0] >= 0:
            #Inside left and right of grid
            if next_spot[1] < c and next_spot[1] >= 0:
                #If looping
                if next_spot in path:
                    #print("Looping")
                    break
                else:
                    path.append(next_spot)
                    current = grid[next_spot[0]][next_spot[1]]
            else:
                #print("Outside Columns")
                break
        else:
            #print("Outside Rows")
            break

    if grid[path[-1][0]][path[-1][1]] == "#" or grid[path[-1][0]][path[-1][1]] == ".":
        path = path[0:-1]
    return path

#Old
def get_core_paths(grid):
    visited = []
    paths = []

    for i in range(r):
        for j in range(c):
            #Check for only river locations
            if grid[i][j] in ['^', 'v', '<', '>']:
                #Check if node has already been visited on a different path
                if [i,j] not in visited:
                    current_path = get_path(i, j, grid)
                    paths.append(current_path)
                    for coords in current_path:
                        if coords not in visited:
                            visited.append(coords)
    
    return paths

#Gets adjacent river sqaures from sight seeing locations
def sight_seeing_adjacent(sight_coords, grid):
    check_coords = []
    for sight in sight_coords:
        y = sight[0]
        x = sight[1]
        #Up
        if y - 1 >= 0:
            if grid[y - 1][x] in ['^', 'v', '<', '>']:
                check_coords.append([y - 1, x])

        #Down
        if y + 1 < r:
            if grid[y + 1][x] in ['^', 'v', '<', '>']:
                check_coords.append([y + 1, x])
        
        #Right
        if x + 1 < c:
            if grid[y][x + 1] in ['^', 'v', '<', '>']:
                check_coords.append([y, x + 1])

        #Left
        if x - 1 >= 0:
            if grid[y][x - 1] in ['^', 'v', '<', '>']:
                check_coords.append([y, x - 1])

    return check_coords

def get_max_sights(check_coords, max_sights, grid):
    visited = []
    current_max = 0

    for coords in check_coords:
        current_path = get_path(coords[0], coords[1], grid)
        #print(coords)
        sight_count = get_sights_on_path(current_path)

        if sight_count == max_sights:
            return max_sights
        
        current_max = max(current_max, sight_count)


        for sub_coords in current_path:
            if sub_coords not in visited:
                visited.append(sub_coords)

    return current_max
        



def get_sights_on_path(path):
    sight_count = 0
    seen = []
    for coords in path:
        row = coords[0]
        col = coords[1]
        #Up
        if row - 1 >= 0:
            if grid[row - 1][col] == "#" and [[row - 1, col]] not in seen:
                sight_count += 1
                seen.append([[row - 1, col]])
                
        #Down
        if row + 1 < r:
            if grid[row + 1][col] == "#" and [[row + 1, col]] not in seen:
                sight_count += 1
                seen.append([[row + 1, col]])

        #Right
        if col + 1 < c:
            if grid[row][col + 1] == "#" and [[row, col + 1]] not in seen:
                sight_count += 1
                seen.append([[row, col + 1]])

        #Left
        if col - 1 >= 0:
            if grid[row][col - 1] == "#" and [[row, col - 1]] not in seen:
                sight_count += 1
                seen.append([[row, col - 1]])
    return sight_count


print(get_max_sights(sight_seeing_adjacent(sight_seeing_coords, grid), sight_seeing_count, grid))